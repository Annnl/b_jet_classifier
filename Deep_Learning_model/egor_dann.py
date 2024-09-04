# source :
# https://github.com/wikibook/dl-vision/blob/master/Chapter07/ch7_nb5_train_a_simple_domain_adversarial_network_(dann).ipynb
# DANN model setup by Egor
import ROOT
import os
from datetime import datetime
import numpy as np
import pandas as pd
import uproot as ur
import awkward as ak
import tensorflow as tf
from tensorflow.keras import Sequential, Model
import matplotlib.pyplot as plt
import time
import yaml
import argparse
import collections

pd.set_option('display.max_columns', None)
np.random.seed(31415)

print('ROOT version: ', ROOT.__version__)
print('numpy version: ', np.__version__)
print('pandas version: ', pd.__version__)
print('uproot version: ', ur.__version__)
print('awkward version: ', ak.__version__)
print('Tensorflow version: ', tf.__version__)
print(tf.config.list_physical_devices('GPU'))


batch_size = 50 # put to config file!

###
# Get arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config_file', type = str, help = 'config file in .yml format')
args = parser.parse_args()


###
# Create output directory for plots
os.system('mkdir figures/' + datetime.now().strftime('%d_%m_%Y_%H%M'))
plot_dir = 'figures/' + datetime.now().strftime('%d_%m_%Y_%H%M') + "/"


###
# Open config file
with open(args.config_file, 'r') as file:
    config = yaml.safe_load(file)


###
# Define a few learning rate functions
initial_learning_rate = 0.001
decay = initial_learning_rate / config['model']['epochs']

def lr_time_based_decay(epoch, lr):
    learning_rate = lr * 1 / (1 + decay * epoch)
    tf.summary.scalar('learning rate', data=learning_rate, step=epoch)
    return learning_rate

def lr_step_decay(epoch, lr):
    drop_rate = 0.5
    epochs_drop = 10.0
    learning_rate = initial_learning_rate * math.pow(drop_rate, math.floor(epoch/epochs_drop))
    tf.summary.scalar('learning rate', data=learning_rate, step=epoch)
    return learning_rate

def lr_exp_decay(epoch, lr):
    k = 0.1
    learning_rate = initial_learning_rate * math.exp(-k*epoch)
    tf.summary.scalar('learning rate', data=learning_rate, step=epoch)
    return learning_rate


###
# Load events
def get_prepared_data(root_file, silent=True):
    """
    :root_file: from the config, 'in_{}_file' (come up with a better var name)
    :silent:    prints out intermediate info if False
    """

    if not silent: print('\n\nPreparing data for {}\n'.format(root_file))
    root_file = 'in_{}_file'.format(root_file)

    inFileName = config[root_file]['name']
    inFile = ur.open(inFileName)
    if not silent: print(inFile.classnames())

    tree = inFile[config[root_file]['tree']]
    if not silent: print('Tree keys: \n', tree.keys())
    if not silent: print(type(tree))
    tree.show()

    dfall = tree.arrays(library='pd')

    # shuffle the events
    dfall = dfall.sample(frac=1).reset_index(drop=True)

    ###
    # Examine pandas dataset

    # dump list of features
    dfall.columns

    # examine first few events
    dfall.head()

    # take a look at feature distribution
    dfall.describe()

    label_weights = ( (dfall.loc[dfall[config[root_file]['target']]!=4])[config[root_file]['weights']].sum(), \
                      (dfall.loc[dfall[config[root_file]['target']]==4])[config[root_file]['weights']].sum() )
    if not silent: print('\ntotal label weights {}'.format(label_weights))

    label_nevents = ( dfall.loc[dfall[config[root_file]['target']]!=4].shape[0], \
                      dfall.loc[dfall[config[root_file]['target']]==4].shape[0] )
    if not silent: print ('total class number of events {}'.format(label_nevents))

    ###
    # Data preparation

    if not silent: print ('Full data shape: {}'.format(dfall.shape))

    # keep events with not negative weights
    # it is not correct in principle, but
    # many data science tools break given a negative weight
    fulldata = dfall[dfall[config[root_file]['weights']]>=0]
    if not silent: print ('Data with non-negative weights shape: {}'.format(fulldata.shape))

    # weights and topHOF are not discriminative variables
    # therefore, hide them in in separate vectors
    # do not cut or shuffle after that!
    target = fulldata[config[root_file]['target']]
    del fulldata[config[root_file]['target']]
    weights = fulldata[config[root_file]['weights']]
    del fulldata[config[root_file]['weights']]
    if not silent: print('\nSeparated "target" and "weight" from "fulldata".\n')

    # tf doesn't tolerate targets other than 0/1
    # replace topHOF==4 and !=4 as 0 and 1 respectively
    # simple 'if target[i] == 4 : target[i] = 0' doesn't work on lxplus environment
    targets = []
    sig_vals = []
    bkg_vals = []

    if isinstance(config[root_file]['sig_val'], list) and isinstance(config[root_file]['bkg_val'], list) :
        targets = config[root_file]['sig_val'] + config[root_file]['bkg_val']
        sig_vals = config[root_file]['sig_val']
        bkg_vals = config[root_file]['bkg_val']
    else :
        targets = [-99, 0, 1, 4]
        sig_vals = [-99, 0, 1]
        bkg_vals = [4]

    if (config[root_file]['sig_val'] != None) ^ (config[root_file]['sig_val'] != None) :
        print('WARNING: Config Sig/Bkg targets declaration issue: one is None other is not.')
        print('WARNING: Using the default list [-99, 0, 1, 4]')

    for val in targets:
        if val in bkg_vals: target = target.replace(to_replace = val, value = 0)
        else : target = target.replace(to_replace = val, value = 1)
    # check that it worked
    for i, v in target.items():
        if not silent: print('Index: {}, value: {}'.format(i, v))
        if i>20: break
    if not silent: print('\nReplaced topHOF values with 0 and 1.\n')

    ###
    # Features selection/engineering

    # define a pandas series object with only features
    data = pd.DataFrame(fulldata, columns=config[root_file]['features'])
    if not silent: print('Shape: {}'.format(data.shape))
    data.head()

    # draw features plots
    if root_file=='nominal':
        plt.figure('Discriminative variables')
        ax = data[target==0].hist(weights=weights[target==0], figsize=(15,12), color='b', alpha=0.5, density=True)
        ax = ax.flatten()[:data.shape[1]]
        data[target==1].hist(weights=weights[target==1], figsize=(15,12), color='r', alpha=0.5, density=True, ax=ax)
        plt.savefig(plot_dir + 'discr_vars_plot_test.pdf')
        plt.close()
        if not silent: print('\nCreated discriminative variables plots.\n')


    ###
    # Transform the features

    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    train_size = config['train_size']

    X_train, X_test, y_train, y_test, weights_train, weights_test = \
        train_test_split(data, target, weights, train_size=train_size)

    y_train, y_test, weights_train, weights_test = \
        y_train.reset_index(drop=True),y_test.reset_index(drop=True), \
        weights_train.reset_index(drop=True), weights_test.reset_index(drop=True)

    if not silent: print ('\nXtrain Shape: {}'.format(X_train.shape))
    if not silent: print ('ytrain Shape: {}'.format(y_train.shape))
    if not silent: print ('Training Weights: {}'.format(weights_train.shape, '\n'))
    if not silent: print ('Xtest Shape: {}'.format(X_test.shape))
    if not silent: print ('ytest Shape: {}'.format(y_test.shape))
    if not silent: print ('Test Weights: {}\n'.format(weights_test.shape))

    # extra split: test and validation
    X_test, X_val, y_test, y_val, weights_test, weights_val, = \
        train_test_split(X_test, y_test, weights_test, train_size=1-config['validation_size'], shuffle=False)

    ###
    # Standardize the Data

    # scale to mean of 0 and variance of 1.0: (x - mu)/sigma
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test) # applies the transformation calculated the line above

    ###
    # Adjust the Test and Train sig/bkg weights

#    class_weights_train = (weights_train[y_train==1].sum(), weights_train[y_train==0].sum())
#    if not silent: print ('Class_weights_train: {}'.format(class_weights_train))
#    for i in range(len(class_weights_train)):
#        weights_train[y_train==i] *= max(class_weights_train)/class_weights_train[i] #equalize number of background and signal event
#        weights_test[y_test==i] *= 1/(1-train_size) #increase test weight to compensate for sampling
#
#    if not silent: print ('\nTrain : total weight sig {}'.format(weights_train[y_train == 1].sum()))
#    if not silent: print ('Train : total weight bkg {}'.format(weights_train[y_train == 0].sum()))
#    if not silent: print ('Test : total weight sig {} '.format(weights_test[y_test == 1].sum()))
#    if not silent: print ('Test : total weight bkg {}\n'.format(weights_test[y_test == 0].sum()))
#
#    # quickly take a look at weights
#    if not silent: print(class_weights_train)
#    if not silent: print(weights_train)

    return X_train, X_val, X_test, y_train, y_val, y_test


###
# Prepare training data for DANN

# label classifier: (source) nominal sample b-jets and (target) their labels
X_train, X_val, X_test, y_train, y_val, y_test = get_prepared_data('nominal')
y_train = pd.Series.to_numpy(y_train)
y_val = pd.Series.to_numpy(y_val)
y_test = pd.Series.to_numpy(y_test)

# domain classifier: (source) nominal and domain samples b-jets and (target) their domain labels
#Xdn_train, Xdn_val, Xdn_test, ydn_train, ydn_val, ydn_test = get_prepared_data('nominal_for_domain')
Xd1_train, Xd1_val, Xd1_test, yd1_train, yd1_val, yd1_test = get_prepared_data('domain1')
Xd2_train, Xd2_val, Xd2_test, yd2_train, yd2_val, yd2_test = get_prepared_data('domain2')


# training dataset
nominal_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
nominal_dataset = nominal_dataset.batch(int(batch_size/2))
domain1_dataset = tf.data.Dataset.from_tensor_slices((Xd1_train, yd1_train))
domain1_dataset = domain1_dataset.batch(int(batch_size/2))
training_dataset = tf.data.Dataset.zip((nominal_dataset, domain1_dataset))

# 'images' - coordinates in the phase spase.
def _prepare_data_for_dann_training(nominal_data, domain1_data,
                                    main_head_name='main_preds', domain1_head_name='domain_preds'):

    nominal_images, nominal_labels = nominal_data
    domain1_images, domain1_labels = domain1_data

    num_nominal = tf.shape(nominal_images)[0]
    num_domain1 = tf.shape(domain1_images)[0]

    batch_images = tf.concat((nominal_images, domain1_images), axis=0)
    batch_labels = tf.concat((nominal_labels, domain1_labels), axis=0)

    # not to penalize the model for its prediscions on the domain images,
    # by assigning a weight = 0 to these elements of the batch:
    nominal_weight_per_sample = tf.tile([1.], [num_nominal])
    domain1_weight_per_sample = tf.tile([0.], [num_domain1])
    batch_sample_weights = tf.concat((nominal_weight_per_sample, domain1_weight_per_sample), axis=0)

    # domain classifiscation
    # we prepared ydn_train and yd1_train to be as what we need here
    # but it is simpler to reuse batch_sample_weights that passing extra argument to the function
    domain1_labels = batch_sample_weights
    domain1_sample_weights = tf.tile([1.], [num_nominal + num_domain1])

    batch_domain1 = {main_head_name: batch_labels,
                     domain1_head_name: domain1_labels}
    batch_sample_weights = {main_head_name: batch_sample_weights,
                            domain1_head_name: domain1_sample_weights}

    return batch_images, batch_domain1, batch_sample_weights


import functools

label_preds_head_name = 'label_preds'
domain1_preds_head_name = 'domain1_preds'
prepare_for_dann_training_fn = functools.partial(_prepare_data_for_dann_training,
                                                 main_head_name=label_preds_head_name,
                                                 domain1_head_name=domain1_preds_head_name)

training_dataset = training_dataset.map(prepare_for_dann_training_fn, num_parallel_calls=4)
print(training_dataset)


# testing dataset
testing_dataset = tf.data.Dataset.from_tensor_slices((Xd1_test, yd1_test))
testing_dataset = testing_dataset.batch(batch_size)

def _prepare_data_for_dann_testing(domain1_images, domain1_labels,
                                      main_head_name='main_preds', domain1_head_name='domain_preds'):
    # the batch contains only validation/test images from the target domain. 
    # this time, we want to evaluate the main loss over these images, so we assign a normal loss
    # weight = 1 to each samples.
    num_samples = tf.shape(domain1_images)[0]

    # want to evaluate over
    loss_weights = tf.tile([1], [num_samples])

    # to assure we have labels as zeroes
    domain1_labels = tf.tile([0], [num_samples])

    batch_targets = {main_head_name: domain1_labels,
                     domain1_head_name: domain1_labels}
    batch_sample_weights = {main_head_name: loss_weights,
                            domain1_head_name: loss_weights}

    return domain1_images, batch_targets, batch_sample_weights


prepare_for_dann_testing_fn = functools.partial(_prepare_data_for_dann_testing,
                                                main_head_name=label_preds_head_name,
                                                domain1_head_name=domain1_preds_head_name)

testing_dataset = testing_dataset.map(prepare_for_dann_testing_fn, num_parallel_calls=4)
print(testing_dataset)


###
# Build the model

# build feature extractor layers and the label prediction model
num_classes = 2 # 1 - probability to be of the target (additional b-jet) class
#inputs = tf.keras.layers.Input(shape=(X_train.shape[1],))
#fe_hiddens = []
#for i in range(len(config['model']['hidden_layers'])):
#    layer_name = 'feature_exctractor_{}'.format(i)
#    if i==0:
#        hidden_i = tf.keras.layers.Dense(
#                units      = config['model']['hidden_layers'][i], 
#                activation = config['model']['act_func'][i],
#                name       = layer_name
#                )(inputs)
#    else:
#        hidden_i = tf.keras.layers.Dense(
#                units      = config['model']['hidden_layers'][i],
#                activation = config['model']['act_func'][i],
#                name       = layer_name
#                )(fe_hiddens[i-1])
#    fe_hiddens.append(hidden_i)
#
#label_preds_head_name = 'label_preds'
#label_preds = tf.keras.layers.Dense(
#        units      = num_classes,
#        activation = "sigmoid",
#        name       = label_preds_head_name
#        )(fe_hiddens[-1])

inputs        = tf.keras.layers.Input(shape=(X_train.shape[1],))
hidden1       = tf.keras.layers.Dense(30, activation='relu')(inputs)
hidden2       = tf.keras.layers.Dense(15, activation='relu')(hidden1)
hidden3       = tf.keras.layers.Dense(7, activation='relu')(hidden2)
label_preds   = tf.keras.layers.Dense(num_classes, activation='softmax', name=label_preds_head_name)(hidden3)

label_prediction_model = tf.keras.models.Model(
        inputs  = inputs,
        outputs = label_preds,
        name    = 'classification_model')
label_prediction_model.summary()

label_prediction_model.compile(optimizer=tf.keras.optimizers.Adam(),
                               loss='sparse_categorical_crossentropy',
                               metrics=config['model']['metrics'])

from keras_custom_callbacks import SimpleLogCallback
metrics_to_print_nom = collections.OrderedDict([("source-loss", "loss"),
                                            #("target-loss", "val_loss"),
                                            ("source-acc", "accuracy"),
                                            #("target-acc", "val_acc")
])

callbacks_nom = [
        SimpleLogCallback(metrics_to_print_nom, num_epochs=config['model']['epochs'], log_frequency=1)
]

y_train = np.asarray(y_train).astype('int32').reshape((-1,1))
y_test = np.asarray(y_test).astype('int32').reshape((-1,1))

nom_fit = label_prediction_model.fit(x = X_train,
                                     y = y_train,
                                     epochs = config['model']['epochs'],
                                     validation_data = (X_test, y_test),
                                     callbacks = callbacks_nom)

d1_as_nom_fit = label_prediction_model.fit(x = Xd1_train,
                                           y = yd1_train,
                                           epochs = config['model']['epochs'],
                                           validation_data = (Xd1_test, yd1_test),
                                           callbacks = callbacks_nom)


@tf.custom_gradient
def reverse_gradient(x, hp_lambda):
    """
    Flips the sign of the incoming gradient during backpropagation.
    :param x:           Input tensor
    :param hp_lambda:   Hyper parameter lambda (DANN parameter)
    :return:            Input tensor with reverse gradient (+ function to compute this reversed gradient)
    """

    # Feed-forward operation:
    y = tf.identity(x)

    # Back-propagation/gradient-computing operation:
    def _flip_gradient(dy):
        # Since the decorated function 'reverse_gradient()' actually has 2 inputs
        # (counting 'hp_lambda'), we have to return the gradient for each -- but
        # anyway, the derivative wrt 'hp_lambda' is null:
        return tf.math.negative(dy) * hp_lambda, tf.constant(0.)

    return y, _flip_gradient


# wrap the reverse gradient as a Keras layer
class GradientReversal (tf.keras.layers.Layer):
    """
    Flip the sign of gradient during training
    """

    def __init__(self, hp_lambda, **kwargs):
        super().__init__(**kwargs)
        self.hp_lambda = hp_lambda

    def call(self, inputs, training=None):
        return reverse_gradient(inputs, self.hp_lambda)

    def get_config(self):
        config = super().get_config()
        config['hp_lambda'] = self.hp_lambda
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


# create domain classification model
hp_lambda = tf.Variable(1.0)
num_domains = 1 # 2: 'source' vs. 'target' (maybe not what we need), 1: prob. to be more or less 'source'-like

domain1_preds_head_name = 'domain1_preds'
#domain1_preds = GradientReversal(hp_lambda)(fe_hiddens[-1])
#domain1_preds = tf.keras.layers.Dense(
#        units      = 10,
#        activation = 'relu',
#        name       = 'domain1_dense'
#        )(domain1_preds)
#domain1_preds = tf.keras.layers.Dense(
#        units      = num_domains,
#        activation = "sigmoid",
#        name       = domain1_preds_head_name
#        )(domain1_preds)
#
#domain_classification_model1 = tf.keras.models.Model(
#        inputs  = inputs,
#        outputs = domain1_preds,
#        name    = 'domain_dlassification_model')
##domain_classification_model1.summary()

domain1_preds = GradientReversal(hp_lambda)(hidden3)
domain1_preds = tf.keras.layers.Dense(12, activation='linear')(domain1_preds)
domain1_preds = tf.keras.layers.Dense(5, activation='linear', name="do5")(domain1_preds)
domain1_preds = tf.keras.layers.Activation("elu", name="do6")(domain1_preds)
domain1_preds = tf.keras.layers.Dropout(0.5)(domain1_preds)
domain1_preds = tf.keras.layers.Dense(num_domains, activation='softmax', name=domain_preds_head_name)(x)
domain_classification_model1 = tf.keras.models.Model(inputs=inputs, outputs=domain1_preds)


# build a combined model
combined_model = tf.keras.models.Model(inputs=inputs, outputs=[label_preds, domain1_preds])

combined_model.compile(
                       optimizer=tf.keras.optimizers.Adam(),
                       loss={
                           label_preds_head_name:   'binary_crossentropy',
                           domain1_preds_head_name: 'binary_crossentropy'},
                       loss_weights={
                           label_preds_head_name:   1,
                           domain1_preds_head_name: 1},
                       metrics={ # weighted_metrics ?
                           label_preds_head_name:   config['model']['metrics'],
                           domain1_preds_head_name: config['model']['metrics']}
                       )

combined_model.summary()


# define some metrics
metrics_to_print = collections.OrderedDict([
    ('lc-loss', label_preds_head_name + '_loss'),
    ('d-loss', domain1_preds_head_name + '_loss'),
    ('lc-acc', label_preds_head_name + '_accuracy'),
    ('d-acc', domain1_preds_head_name + '_accuracy'),
    #('target c-acc', 'val_' + label_preds_head_name + '_acc')
])

callbacks = [
        SimpleLogCallback(metrics_to_print, num_epochs=config['model']['epochs'], log_frequency=1)
]


# fit and save the model
starting_time = time.time()
if config['model']['new_or_load'] == 'new' :
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience = 3)
    lr_callback = tf.keras.callbacks.LearningRateScheduler(lr_time_based_decay, verbose = 1)

    #the_fit = combined_model.fit(training_dataset,
    #                             epochs = config['model']['epochs'],
    #                             validation_data = testing_dataset,
    #                             verbose = 0,
    #                             #callbacks = [lr_callback, early_stopping, callbacks])
    #                             callbacks = callbacks)
    model.save(config['model']['name'] + datetime.now().strftime('%d_%m_%Y_%H%M'))

# evaluate the model
loss_n, acc_n = model.evaluate(X_test, y_test.values, weighted_metrics=None)
print('Measured model accuracy on the nominal dataset: {}, loss: {}'.format(acc_n, loss_n))
loss_d1, acc_d1 = model.evaluate(Xd1_test, yd1_test, weighted_metrics=None)
print('Measured model accuracy on the dom1 dataset: {}, loss: {}'.format(acc_d1, loss_d1))


training_time = time.time() - starting_time
print('Training time:i {}'.format(training_time))

exit()
# draw relevant plots
if config['model']['new_or_load'] == 'new' :
    print('Fit history content: {}\n'.format(the_fit.history))

    plt.figure('Training loss')
    plt.plot(the_fit.history['loss'],     color='red',  alpha=0.5, label='training loss')
    plt.plot(the_fit.history['val_loss'], color='blue', alpha=0.5, label='testing loss')
    plt.legend(fontsize=12)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training loss')
    plt.savefig(plot_dir + 'training_loss.pdf')
    plt.close()

    plt.figure('Learning rate')
    plt.plot(the_fit.history['lr'], label='learning rate')
    plt.legend(fontsize=12)
    plt.xlabel('Epoch')
    plt.ylabel('Learning rate')
    plt.savefig(plot_dir + 'learning_rate.pdf')
    plt.close()

    plt.figure('Train and Val Loss and Acc')
    plt.plot(the_fit.history['loss'],         label='train loss')
    plt.plot(the_fit.history['val_loss'],     label='val loss')
    plt.plot(the_fit.history['accuracy'],     label='train acc')
    plt.plot(the_fit.history['val_accuracy'], label='val acc')
    plt.legend(fontsize=12)
    plt.title('Stats')
    plt.xlabel('Epoch')
    plt.ylabel('Loss/Accuracy')
    plt.savefig(plot_dir + 'stats.pdf')
    plt.close()


###
# Use the model to make predictions

y_pred_test = model.predict(X_test).ravel()
y_pred_train = model.predict(X_train).ravel()

# do the ROC curve
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.utils import class_weight

auc_test = roc_auc_score(y_true=y_test, y_score=y_pred_test, sample_weight=None) #, sample_weight=weights_test)
print("\t\tauc_test done")
auc_train = roc_auc_score(y_true=y_train.values, y_score=y_pred_train, sample_weight=None) #,sample_weight=weights_train)
print("\t\tauc_train done")
print('auc test:',auc_test)
print ('auc train:',auc_train)

fpr1,tpr1,_ = roc_curve(y_true=y_train, y_score=y_pred_train, sample_weight=None) #, sample_weight=weights_train)
fpr2,tpr2,_ = roc_curve(y_true=y_test,  y_score=y_pred_test, sample_weight=None) #,  sample_weight=weights_test)
plt.figure('ROC curve')
label_train = 'train (AUC = ' + str(auc_train) + ')'
label_test = 'test (AUC = ' + str(auc_test) + ')'
plt.plot(fpr1, tpr1, color='blue', lw=2, label=label_train, alpha=0.5)
plt.plot(fpr2, tpr2, color='red',  lw=2, label=label_test,  alpha=0.5)
plt.legend(fontsize=12)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.savefig(plot_dir + 'roc.pdf')
plt.close()

###
# Significance function

from math import sqrt
from math import log
def amsasimov(s,b):
    if b<=0 or s<=0:
      return 0
    try:
      return sqrt(2*((s+b)*log(1+float(s)/b)-s))
    except ValueError:
      print(1+float(s)/b)
      print (2*((s+b)*log(1+float(s)/b)-s))

int_pred_test_sig = [weights_test[(y_test ==1) & (y_pred_test > th_cut)].sum() for th_cut in np.linspace(0,1,num=50)]
int_pred_test_bkg = [weights_test[(y_test ==0) & (y_pred_test > th_cut)].sum() for th_cut in np.linspace(0,1,num=50)]
vamsasimov = [amsasimov(sumsig,sumbkg) for (sumsig,sumbkg) in zip(int_pred_test_sig,int_pred_test_bkg)]
Z = max(vamsasimov)
print('Z value: {}'.format(Z))

plt.figure('Significance')
plt.plot(np.linspace(0,1,num=50),vamsasimov, label='Significance (Z = {})'.format(np.round(Z,decimals=2)))

plt.title('NN Significance')
plt.xlabel('Threshold')
plt.ylabel('Significance')
plt.legend()
plt.savefig(plot_dir + 'significance_xgb.pdf')
plt.close()


###
# Plot Sig and Bkg nn scores spectra
from plot_bkg_sig_nn_spectra import compare_train_test

compare_train_test(y_pred_train, y_train, y_pred_test, y_test,
                   xlabel='NN Score', title='NN',
                   weights_train=weights_train.values, weights_test=weights_test.values)
