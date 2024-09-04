from array import array
from numpy import append
import ROOT
import sys
if len(sys.argv)!= 3:
				print("wrong")
				sys.exit(1)
inFileName = sys.argv[1]
outFileName = sys.argv[2]
print("Reading from",inFileName,"writing to",outFileName)

f = open(inFileName,"r")
lines = f.readlines()
f.close()

def weight():
				job_DID = str(ID)
				if job_DID=='410648':
								campaign_xsection_x_genFiltEff = 3.9968
								kFactor = 0.945

				if job_DID=='410649':
								campaign_xsection_x_genFiltEff = 3.9940
								kFactor = 0.946

				if job_DID=='410560': 
								campaign_xsection_x_genFiltEff = 0.24037
								kFactor = 1.0

				if job_DID=='410408':
								campaign_xsection_x_genFiltEff = 0.016046
								kFactor = 1.0

				if job_DID=='346678': 
								campaign_xsection_x_genFiltEff = 0.016719
								kFactor = 1.0

				if job_DID=='346676':
								campaign_xsection_x_genFiltEff = 0.060140
								kFactor = 1.0

				if job_DID=='412043':
								campaign_xsection_x_genFiltEff = 0.010624
								kFactor = 1.1267

				if job_DID=='410155':
								campaign_xsection_x_genFiltEff = 0.54830
								kFactor = 1.10

				if job_DID=='410156':
								campaign_xsection_x_genFiltEff = 0.15499
								kFactor = 1.11

				if job_DID=='410157': 
								campaign_xsection_x_genFiltEff = 0.52771
								kFactor = 1.11

				if job_DID=='410218':
								campaign_xsection_x_genFiltEff = 0.036888
								kFactor = 1.12

				if job_DID=='410220':
								campaign_xsection_x_genFiltEff = 0.036599
								kFactor = 1.12

				if job_DID=='410276':
								campaign_xsection_x_genFiltEff = 0.0184
								kFactor = 1.0
		
				if job_DID=='410277': 
								campaign_xsection_x_genFiltEff = 0.0184
								kFactor = 1.0
				if job_DID=='410219':
								campaign_xsection_x_genFiltEff = 0.036895
								kFactor = 1.12

				if job_DID=='410278':
								campaign_xsection_x_genFiltEff = 0.00197
								kFactor = 1.0

				if job_DID=='410658': 
								campaign_xsection_x_genFiltEff = 36.993
								kFactor = 1.191

				if job_DID=='410659': 
								campaign_xsection_x_genFiltEff = 22.175
								kFactor = 1.183

				if job_DID=='410644':
								campaign_xsection_x_genFiltEff = 2.0268
								kFactor = 1.015

				if job_DID=='410645': 
								campaign_xsection_x_genFiltEff = 1.2676
								kFactor = 1.015

				if job_DID=='346345':
								campaign_xsection_x_genFiltEff = 0.05343
								kFactor = 1.0
		
				if job_DID=='346344': 
								campaign_xsection_x_genFiltEff = 0.22276
								kFactor = 1.0

				if job_DID=='346343':
								campaign_xsection_x_genFiltEff = 0.23082
								kFactor = 1.0

				if job_DID=='364250':
								campaign_xsection_x_genFiltEff = 1.2523
								kFactor = 1.0

				if job_DID=='364253':
								campaign_xsection_x_genFiltEff = 4.5832
								kFactor = 1.0

				if job_DID=='364254':
								campaign_xsection_x_genFiltEff = 12.501
								kFactor = 1.0

				if job_DID=='364288':
								campaign_xsection_x_genFiltEff = 1.4318
								kFactor = 1.0

				if job_DID=='364289': 
								campaign_xsection_x_genFiltEff = 2.9152
								kFactor = 1.0

				if job_DID=='364290':
								campaign_xsection_x_genFiltEff = 0.17046
								kFactor = 1.0

				if job_DID=='364283': 
								campaign_xsection_x_genFiltEff = 0.010471
								kFactor = 1.0

				if job_DID=='364284':
								campaign_xsection_x_genFiltEff = 0.046367
								kFactor = 1.0

				if job_DID=='364285':
								campaign_xsection_x_genFiltEff = 0.1163
								kFactor = 1.0

				if job_DID=='364287':
								campaign_xsection_x_genFiltEff = 0.040779
								kFactor = 1.0

				if job_DID=='345705':
								campaign_xsection_x_genFiltEff = 0.0099486
								kFactor = 1.0

				if job_DID=='345706':
								campaign_xsection_x_genFiltEff = 0.010091
								kFactor = 1.0

				if job_DID=='345723':
								campaign_xsection_x_genFiltEff = 0.0071108
								kFactor = 1.0

				if job_DID=='363356':
								campaign_xsection_x_genFiltEff = 15.563
								kFactor = 0.13961

				if job_DID=='363358':
								campaign_xsection_x_genFiltEff = 3.437
								kFactor = 1.0

				if job_DID=='364128': 
								campaign_xsection_x_genFiltEff = 1627.725872
								kFactor = 0.9751

				if job_DID=='364129':
								campaign_xsection_x_genFiltEff = 223.881432
								kFactor = 0.9751

				if job_DID=='364130':
								campaign_xsection_x_genFiltEff = 127.7329554
								kFactor = 0.9751

				if job_DID=='364131':
								campaign_xsection_x_genFiltEff = 76.0261671
								kFactor = 0.9751

				if job_DID=='364132':
								campaign_xsection_x_genFiltEff = 20.212279
								kFactor = 0.9751

				if job_DID=='364133':
								campaign_xsection_x_genFiltEff = 12.29393
								kFactor = 0.9751

				if job_DID=='364134': 
								campaign_xsection_x_genFiltEff = 24.80341201
								kFactor = 0.9751

				if job_DID=='364135': 
								campaign_xsection_x_genFiltEff = 9.3282378
								kFactor = 0.9751

				if job_DID=='364136':
								campaign_xsection_x_genFiltEff = 5.47909362
								kFactor = 0.9751

				if job_DID=='364137':
								campaign_xsection_x_genFiltEff = 4.791190072
								kFactor = 0.9751

				if job_DID=='364138': 
								campaign_xsection_x_genFiltEff = 2.275625215
								kFactor = 0.9751

				if job_DID=='364139': 
								campaign_xsection_x_genFiltEff = 1.502837652
								kFactor = 0.9751

				if job_DID=='364140':
								campaign_xsection_x_genFiltEff = 1.8096
								kFactor = 0.9751

				if job_DID=='364141':
								campaign_xsection_x_genFiltEff = 0.14834
								kFactor = 0.9751

				if job_DID=='364114':
								campaign_xsection_x_genFiltEff = 1627.176708
								kFactor = 0.9751

				if job_DID=='364115': 
								campaign_xsection_x_genFiltEff = 223.73136
								kFactor = 0.9751

				if job_DID=='364116':
								campaign_xsection_x_genFiltEff = 126.4502953
								kFactor = 0.9751

				if job_DID=='364117':
								campaign_xsection_x_genFiltEff = 76.292515
								kFactor = 0.9751

				if job_DID=='364118':
								campaign_xsection_x_genFiltEff = 20.3360066
								kFactor = 0.9751
		
				if job_DID=='364119':
								campaign_xsection_x_genFiltEff = 12.6227733
								kFactor = 0.9751

				if job_DID=='364120':
								campaign_xsection_x_genFiltEff = 25.03001412
								kFactor = 0.9751

				if job_DID=='364121': 
								campaign_xsection_x_genFiltEff = 9.3719948
								kFactor = 0.9751

				if job_DID=='364122': 
								campaign_xsection_x_genFiltEff = 6.08263138
								kFactor = 0.9751

				if job_DID=='364123': 
								campaign_xsection_x_genFiltEff = 4.869231562
								kFactor = 0.9751

				if job_DID=='364124': 
								campaign_xsection_x_genFiltEff = 2.279979034
								kFactor = 0.9751

				if job_DID=='364125':
								campaign_xsection_x_genFiltEff = 1.494370818
								kFactor = 0.9751

				if job_DID=='364126': 
								campaign_xsection_x_genFiltEff = 1.8081
								kFactor = 0.9751

				if job_DID=='364127':
								campaign_xsection_x_genFiltEff = 0.14857
								kFactor = 0.9751

				if job_DID=='364100': 
								campaign_xsection_x_genFiltEff = 1630.2243
								kFactor = 0.9751

				if job_DID=='364101': 
								campaign_xsection_x_genFiltEff = 223.717472
								kFactor = 0.9751

				if job_DID=='364102':
								campaign_xsection_x_genFiltEff = 127.1799342
								kFactor = 0.9751
		
				if job_DID=='364103': 
								campaign_xsection_x_genFiltEff = 75.0164716
								kFactor = 0.9751

				if job_DID=='364104':
								campaign_xsection_x_genFiltEff = 20.3477432
								kFactor = 0.9751

				if job_DID=='364105':
								campaign_xsection_x_genFiltEff = 12.3885125
								kFactor = 0.9751

				if job_DID=='364106':
								campaign_xsection_x_genFiltEff = 24.28530322
								kFactor = 0.9751

				if job_DID=='364107':
								campaign_xsection_x_genFiltEff = 9.2754186
								kFactor = 0.9751

				if job_DID=='364108':
								campaign_xsection_x_genFiltEff = 6.01361075
								kFactor = 0.9751

				if job_DID=="364109":
								campaign_xsection_x_genFiltEff = 4.77297475
								kFactor = 0.9751

				if job_DID=="364110":
								campaign_xsection_x_genFiltEff = 2.265570784
								kFactor = 0.9751

				if job_DID=="364111":
								campaign_xsection_x_genFiltEff = 1.491320988
								kFactor = 0.9751

				if job_DID=="364112": 
								campaign_xsection_x_genFiltEff = 1.7881
								kFactor = 0.9751

				if job_DID=="364113":
								campaign_xsection_x_genFiltEff = 0.14769
								kFactor = 0.9751

				if job_DID=="411076":
								campaign_xsection_x_genFiltEff = 0.6740
								kFactor = 1.1397

				if job_DID=="411077":
								campaign_xsection_x_genFiltEff = 3.582
								kFactor = 1.1398

				if job_DID=="411078":
								campaign_xsection_x_genFiltEff = 3.034
								kFactor = 1.1397

				if job_DID=="410472":
								campaign_xsection_x_genFiltEff = 76.95
								kFactor = 1.13975636159

				if "mc16a" in name:
								campaign_lumi = 3.21956 + 32.9881
								if job_DID=="410648": sumWeights = 3.99906*pow(10,6)
								if job_DID=="410649": sumWeights = 3.99637*pow(10,6)
								if job_DID=="410560": sumWeights = 43.7437
								if job_DID=="410408": sumWeights = 1611.9
								if job_DID=="346678": sumWeights = 15027.4 
								if job_DID=="346676": sumWeights = 71816.9 
								if job_DID=="412043": sumWeights = 42612.7
								if job_DID=="410155": sumWeights = 4.11068*pow(10,6)
								if job_DID=="410156": sumWeights = 232491
								if job_DID=="410157": sumWeights = 1.58316*pow(10,6)
								if job_DID=="410218": sumWeights = 52012.9
								if job_DID=="410219": sumWeights = 52021.8
								if job_DID=="410220": sumWeights = 34220.9
								if job_DID=="410276": sumWeights = 6385.08
								if job_DID=="410277": sumWeights = 6380.91
								if job_DID=="410278": sumWeights = 579.889
								if job_DID=="410658": sumWeights = 9.16561*pow(10,8)
								if job_DID=="410659": sumWeights = 5.48748*pow(10,8)
								if job_DID=="410644": sumWeights = 4.05637*pow(10,6)
								if job_DID=="410645": sumWeights = 2.53797*pow(10,6)
								if job_DID=="346345": sumWeights = 273019
								if job_DID=="346344": sumWeights = 2.62087*pow(10,6)
								if job_DID=="346343": sumWeights = 1.18883*pow(10,6)
								if job_DID=="364250": sumWeights = 7.51881*pow(10,6)
								if job_DID=="364253": sumWeights = 5.35645*pow(10,6)
								if job_DID=="364254": sumWeights = 5.1148*pow(10,6)
								if job_DID=="364288": sumWeights = 203874
								if job_DID=="364289": sumWeights = 2.24604*pow(10,6)
								if job_DID=="364290": sumWeights = 29840.3
								if job_DID=="364283": sumWeights = 347963
								if job_DID=="364284": sumWeights = 1.7298*pow(10,6)
								if job_DID=="364285": sumWeights = 302610
								if job_DID=="364287": sumWeights = 100818
								if job_DID=="345705": sumWeights = 100065
								if job_DID=="345706": sumWeights = 1.17615*pow(10,6)
								if job_DID=="345723": sumWeights = 100100
								if job_DID=="363356": sumWeights = 6.971*pow(10,6)
								if job_DID=="363358": sumWeights = 254404
								if job_DID=="364128": sumWeights = 5.37604*pow(10,6)
								if job_DID=="364129": sumWeights = 2.86944*pow(10,6)
								if job_DID=="364130": sumWeights = 4.11444*pow(10,6)
								if job_DID=="364131": sumWeights = 2.19096*pow(10,6)
								if job_DID=="364132": sumWeights = 731614
								if job_DID=="364133": sumWeights = 2.09076*pow(10,6)
								if job_DID=="364134": sumWeights = 2.95972*pow(10,6)
								if job_DID=="364135": sumWeights = 2.00116*pow(10,6)
								if job_DID=="364136": sumWeights = 3.47263*pow(10,6)
								if job_DID=="364137": sumWeights = 6.85424*pow(10,6)
								if job_DID=="364138": sumWeights = 918260
								if job_DID=="364139": sumWeights = 1.86088*pow(10,6)
								if job_DID=="364140": sumWeights = 2.97848*pow(10,6)
								if job_DID=="364141": sumWeights = 1.01827*pow(10,6)
								if job_DID=="364114": sumWeights = 5.37483*pow(10,6)
								if job_DID=="364115": sumWeights = 2.87288*pow(10,6)
								if job_DID=="364116": sumWeights = 4.11018*pow(10,6)
								if job_DID=="364117": sumWeights = 2.17538*pow(10,6)
								if job_DID=="364118": sumWeights = 724682
								if job_DID=="364119": sumWeights = 2.08382*pow(10,6)
								if job_DID=="364120": sumWeights = 2.99657*pow(10,6)
								if job_DID=="364121": sumWeights = 2.0014*pow(10,6)
								if job_DID=="364122": sumWeights = 8.62671*pow(10,6)
								if job_DID=="364123": sumWeights = 1.7234*pow(10,6)
								if job_DID=="364124": sumWeights = 918310
								if job_DID=="364125": sumWeights = 3.74627*pow(10,6)
								if job_DID=="364126": sumWeights = 2.96847*pow(10,6)
								if job_DID=="364127": sumWeights = 1.01652*pow(10,6)
								if job_DID=="364100": sumWeights = 5.37248*pow(10,6)
								if job_DID=="364101": sumWeights = 2.87199*pow(10,6)
								if job_DID=="364102": sumWeights = 4.12098*pow(10,6)
								if job_DID=="364103": sumWeights = 2.16649*pow(10,6)
								if job_DID=="364104": sumWeights = 732465
								if job_DID=="364105": sumWeights = 2.08226*pow(10,6)
								if job_DID=="364106": sumWeights = 2.97401*pow(10,6)
								if job_DID=="364107": sumWeights = 1.99109*pow(10,6)
								if job_DID=="364108": sumWeights = 8.64667*pow(10,6)
								if job_DID=="364109": sumWeights = 1.72841*pow(10,6)
								if job_DID=="364110": sumWeights = 918653
								if job_DID=="364111": sumWeights = 3.74946*pow(10,6)
								if job_DID=="364112": sumWeights = 2.98051*pow(10,6)
								if job_DID=="364113": sumWeights = 1.01705*pow(10,6)
								if job_DID=="411076": sumWeights = 3.33006*pow(10, 9)
								if job_DID=="411077": sumWeights = 3.61088*pow(10, 9)
								if job_DID=="411078": sumWeights = 3.61598*pow(10, 9)
								if job_DID=="410472": sumWeights = 5.82869*pow(10, 10)

				if "mc16d" in name:
								campaign_lumi = 44.3074
								if job_DID=="410648": sumWeights = 4.99937*pow(10,6)
								if job_DID=="410649": sumWeights = 4.99173*pow(10,6)
								if job_DID=="410560": sumWeights = 43.7344
								if job_DID=="410408": sumWeights = 1918.38
								if job_DID=="346678": sumWeights = 18884.5 
								if job_DID=="346676": sumWeights = 90501.8 
								if job_DID=="412043": sumWeights = 53248.7 
								if job_DID=="410155": sumWeights = 4.11193*pow(10,6)
								if job_DID=="410156": sumWeights = 232221
								if job_DID=="410157": sumWeights = 1.58544*pow(10,6)
								if job_DID=="410218": sumWeights = 49255.1
								if job_DID=="410219": sumWeights = 49331.1
								if job_DID=="410220": sumWeights = 32785.1
								if job_DID=="410276": sumWeights = 6378.69
								if job_DID=="410277": sumWeights = 6385.65
								if job_DID=="410278": sumWeights = 565.507
								if job_DID=="410658": sumWeights = 1.15403*pow(10,9)
								if job_DID=="410659": sumWeights = 6.86025*pow(10,8)
								if job_DID=="410644": sumWeights = 5.0656*pow(10,6)
								if job_DID=="410645": sumWeights = 3.17182*pow(10,6)
								if job_DID=="346345": sumWeights = 355020
								if job_DID=="346344": sumWeights = 3.41184*pow(10,6)
								if job_DID=="346343": sumWeights = 1.54907*pow(10,6)
								if job_DID=="364250": sumWeights = 1.51851*pow(10,6)
								if job_DID=="364253": sumWeights = 1.10668*pow(10,6)
								if job_DID=="364254": sumWeights = 1.0238*pow(10,6)
								if job_DID=="364288": sumWeights = 247974
								if job_DID=="364289": sumWeights = 2.77882*pow(10,6)
								if job_DID=="364290": sumWeights = 40270.6
								if job_DID=="364283": sumWeights = 427261
								if job_DID=="364284": sumWeights = 2.21104*pow(10,6)
								if job_DID=="364285": sumWeights = 383024
								if job_DID=="364287": sumWeights = 126659
								if job_DID=="345705": sumWeights = 125057
								if job_DID=="345706": sumWeights = 1.00532*pow(10,6)
								if job_DID=="345723": sumWeights = 115179
								if job_DID=="363356": sumWeights = 3.49307*pow(10,6)
								if job_DID=="363358": sumWeights = 1.26717*pow(10,6)
								if job_DID=="364128": sumWeights = 6.72628*pow(10,6)
								if job_DID=="364129": sumWeights = 3.53296*pow(10,6)
								if job_DID=="364130": sumWeights = 5.13739*pow(10,6)
								if job_DID=="364131": sumWeights = 2.7557*pow(10,6)
								if job_DID=="364132": sumWeights = 903050
								if job_DID=="364133": sumWeights = 2.62897*pow(10,6)
								if job_DID=="364134": sumWeights = 3.73485*pow(10,6)
								if job_DID=="364135": sumWeights = 2.50053*pow(10,6)
								if job_DID=="364136": sumWeights = 4.32478*pow(10,6)
								if job_DID=="364137": sumWeights = 8.62032*pow(10,6)
								if job_DID=="364138": sumWeights = 1.13385*pow(10,6)
								if job_DID=="364139": sumWeights = 2.34316*pow(10,6)
								if job_DID=="364140": sumWeights = 3.72324*pow(10,6)
								if job_DID=="364141": sumWeights = 1.2729*pow(10,6)
								if job_DID=="364114": sumWeights = 6.71901*pow(10,6)
								if job_DID=="364115": sumWeights = 3.5837*pow(10,6)
								if job_DID=="364116": sumWeights = 5.1392*pow(10,6)
								if job_DID=="364117": sumWeights = 2.70266*pow(10,6)
								if job_DID=="364118": sumWeights = 907295
								if job_DID=="364119": sumWeights = 2.62872*pow(10,6)
								if job_DID=="364120": sumWeights = 3.74416*pow(10,6)
								if job_DID=="364121": sumWeights = 2.49978*pow(10,6)
								if job_DID=="364122": sumWeights = 1.08892*pow(10,7)
								if job_DID=="364123": sumWeights = 2.15262*pow(10,6)
								if job_DID=="364124": sumWeights = 1.14707*pow(10,6)
								if job_DID=="364125": sumWeights = 4.67242*pow(10,6)
								if job_DID=="364126": sumWeights = 3.67771*pow(10,6)
								if job_DID=="364127": sumWeights = 1.27033*pow(10,6)
								if job_DID=="364100": sumWeights = 6.69374*pow(10,6)
								if job_DID=="364101": sumWeights = 3.57621*pow(10,6)
								if job_DID=="364102": sumWeights = 4.96649*pow(10,6)
								if job_DID=="364103": sumWeights = 2.7176*pow(10,6)
								if job_DID=="364104": sumWeights = 902414
								if job_DID=="364105": sumWeights = 2.60676*pow(10,6)
								if job_DID=="364106": sumWeights = 3.71602*pow(10,6)
								if job_DID=="364107": sumWeights = 2.49178*pow(10,6)
								if job_DID=="364108": sumWeights = 1.08331*pow(10,7)
								if job_DID=="364109": sumWeights = 2.11655*pow(10,6)
								if job_DID=="364110": sumWeights = 1.14598*pow(10,6)
								if job_DID=="364111": sumWeights = 4.6748*pow(10,6)
								if job_DID=="364112": sumWeights = 3.72533*pow(10,6)
								if job_DID=="364113": sumWeights = 1.27407*pow(10,6) 
								if job_DID=="411076": sumWeights = 4.21891*pow(10,9)
								if job_DID=="411077": sumWeights = 4.49595*pow(10,9)
								if job_DID=="411078": sumWeights = 4.49400*pow(10,9)
								if job_DID=="410472": sumWeights = 7.26510*pow(10,10)

				if "mc16e" in name:
								campaign_lumi = 58.4501
								if job_DID=="410648": sumWeights = 6.51714*pow(10,6)
								if job_DID=="410649": sumWeights = 6.61312*pow(10,6)
								if job_DID=="410560": sumWeights = 57.8341
								if job_DID=="410408": sumWeights = 2546.11
								if job_DID=="346678": sumWeights = 25106.3 
								if job_DID=="346676": sumWeights = 120026 
								if job_DID=="412043": sumWeights = 70784.9 
								if job_DID=="410155": sumWeights = 6.60172*pow(10,6)
								if job_DID=="410156": sumWeights = 310260
								if job_DID=="410157": sumWeights = 1.89573*pow(10,6)
								if job_DID=="410218": sumWeights = 79922.4
								if job_DID=="410219": sumWeights = 80098.1
								if job_DID=="410220": sumWeights = 35092
								if job_DID=="410276": sumWeights = 8518.3
								if job_DID=="410277": sumWeights = 8509.1
								if job_DID=="410278": sumWeights = 885.35
								if job_DID=="410658": sumWeights = 1.54136*pow(10,9)
								if job_DID=="410659": sumWeights = 9.19187*pow(10,8)
								if job_DID=="410644": sumWeights = 6.69946*pow(10,6)
								if job_DID=="410645": sumWeights = 4.20759*pow(10,6)
								if job_DID=="346345": sumWeights = 452972
								if job_DID=="346344": sumWeights = 4.33576*pow(10,6)
								if job_DID=="346343": sumWeights = 1.96924*pow(10,6)
								if job_DID=="364250": sumWeights = 1.08084*pow(10,7)
								if job_DID=="364253": sumWeights = 9.2335*pow(10,6)
								if job_DID=="364254": sumWeights = 8.48634*pow(10,6)
								if job_DID=="364288": sumWeights = 330362
								if job_DID=="364289": sumWeights = 4.31831*pow(10,6)
								if job_DID=="364290": sumWeights = 48496.1
								if job_DID=="364283": sumWeights = 6.06443*pow(10,7)
								if job_DID=="364284": sumWeights = 2.8626*pow(10,6)
								if job_DID=="364285": sumWeights = 605580
								if job_DID=="364287": sumWeights = 1.01272*pow(10,6)
								if job_DID=="345705": sumWeights = 500338
								if job_DID=="345706": sumWeights = 994333
								if job_DID=="345723": sumWeights = 170174
								if job_DID=="363356": sumWeights = 5.7981*pow(10,6)
								if job_DID=="363358": sumWeights = 421819
								if job_DID=="364128": sumWeights = 8.93207*pow(10,6)
								if job_DID=="364129": sumWeights = 4.77104*pow(10,6)
								if job_DID=="364130": sumWeights = 6.84357*pow(10,6)
								if job_DID=="364131": sumWeights = 3.65669*pow(10,6)
								if job_DID=="364132": sumWeights = 1.20985*pow(10,6)
								if job_DID=="364133": sumWeights = 3.47688*pow(10,6)
								if job_DID=="364134": sumWeights = 4.9663*pow(10,6)
								if job_DID=="364135": sumWeights = 3.32968*pow(10,6)
								if job_DID=="364136": sumWeights = 5.75619*pow(10,6)
								if job_DID=="364137": sumWeights = 1.1374*pow(10,6)
								if job_DID=="364138": sumWeights = 1.53285*pow(10,6)
								if job_DID=="364139": sumWeights = 3.11996*pow(10,6)
								if job_DID=="364140": sumWeights = 4.92279*pow(10,6)
								if job_DID=="364141": sumWeights = 1.69785*pow(10,6)
								if job_DID=="364114": sumWeights = 8.91779*pow(10,6)
								if job_DID=="364115": sumWeights = 4.7721*pow(10,6)
								if job_DID=="364116": sumWeights = 6.83013*pow(10,6)
								if job_DID=="364117": sumWeights = 3.6381*pow(10,6)
								if job_DID=="364118": sumWeights = 1.20844*pow(10,6)
								if job_DID=="364119": sumWeights = 3.45048*pow(10,6)
								if job_DID=="364120": sumWeights = 5.01136*pow(10,6)
								if job_DID=="364121": sumWeights = 3.32398*pow(10,6)
								if job_DID=="364122": sumWeights = 1.44376*pow(10,7)
								if job_DID=="364123": sumWeights = 2.95158*pow(10,6)
								if job_DID=="364124": sumWeights = 1.59351*pow(10,6)
								if job_DID=="364125": sumWeights = 6.20312*pow(10,6)
								if job_DID=="364126": sumWeights = 4.93026*pow(10,6)
								if job_DID=="364127": sumWeights = 1.69792*pow(10,6)
								if job_DID=="364100": sumWeights = 8.93622*pow(10,6)
								if job_DID=="364101": sumWeights = 4.70476*pow(10,6)
								if job_DID=="364102": sumWeights = 6.78255*pow(10,6)
								if job_DID=="364103": sumWeights = 3.61556*pow(10,6)
								if job_DID=="364104": sumWeights = 1.19295*pow(10,6)
								if job_DID=="364105": sumWeights = 3.47067*pow(10,6)
								if job_DID=="364106": sumWeights = 4.89956*pow(10,6)
								if job_DID=="364107": sumWeights = 3.32423*pow(10,6)
								if job_DID=="364108": sumWeights = 1.43114*pow(10,7)
								if job_DID=="364109": sumWeights = 2.86554*pow(10,6)
								if job_DID=="364110": sumWeights = 1.53185*pow(10,6)
								if job_DID=="364111": sumWeights = 6.20587*pow(10,6)
								if job_DID=="364112": sumWeights = 5.07812*pow(10,6)
								if job_DID=="364113": sumWeights = 1.6227*pow(10,6)
								if job_DID=="411076": sumWeights = 5.47911*pow(10,9)
								if job_DID=="411077": sumWeights = 5.94763*pow(10,9)
								if job_DID=="411078": sumWeights = 5.94190*pow(10,9)
								if job_DID=="410472": sumWeights = 1.01641*pow(10,11)

				weight_lumi = campaign_lumi * pow(10,3) * campaign_xsection_x_genFiltEff * kFactor / sumWeights
				return w_mc * w_pu * w_leptonSF * w_DL1r_77 * w_jvt * weight_lumi

dR_lep_close = ROOT.TH1D("dR_lep_close","dR_lep_close",40,0,7)
dR_lep_close.Sumw2()
dR_lep_close_top = ROOT.TH1D("dR_lep_close_top","dR_lep_close_top",40,0,7)
dR_lep_close_top.Sumw2()
dR_lep_far = ROOT.TH1D("dR_lep_far","dR_lep_far",40,0,7)
dR_lep_far.Sumw2()
dR_lep_far_top = ROOT.TH1D("dR_lep_far_top","dR_lep_far_top",40,0,7)
dR_lep_far_top.Sumw2()

dR_lep_el = ROOT.TH1D("dR_lep_el","dR_lep_el",40,0,7)
dR_lep_el.Sumw2()
dR_lep_el_top = ROOT.TH1D("dR_lep_el_top","dR_lep_el_top",40,0,7)
dR_lep_el_top.Sumw2()
dR_lep_mu = ROOT.TH1D("dR_lep_mu","dR_lep_mu",40,0,7)
dR_lep_mu.Sumw2()
dR_lep_mu_top = ROOT.TH1D("dR_lep_mu_top","dR_lep_mu_top",40,0,7)
dR_lep_mu_top.Sumw2()

dR_lep_1pt = ROOT.TH1D("dR_lep_1pt","dR_lep_1pt",40,0,7)
dR_lep_1pt.Sumw2()
dR_lep_1pt_top = ROOT.TH1D("dR_lep_1pt_top","dR_lep_1pt_top",40,0,7)
dR_lep_1pt_top.Sumw2()
dR_lep_2pt = ROOT.TH1D("dR_lep_2pt","dR_lep_2pt",40,0,7)
dR_lep_2pt.Sumw2()
dR_lep_2pt_top = ROOT.TH1D("dR_lep_2pt_top","dR_lep_2pt_top",40,0,7)
dR_lep_2pt_top.Sumw2()

dR_bjet_close = ROOT.TH1D("dR_bjet_close","dR_bjet_close",40,0,7)
dR_bjet_close.Sumw2()
dR_bjet_close_top = ROOT.TH1D("dR_bjet_close_top","dR_bjet_close_top",40,0,7)
dR_bjet_close_top.Sumw2()
dR_bjet_far = ROOT.TH1D("dR_bjet_far","dR_bjet_far",40,0,7)
dR_bjet_far.Sumw2()
dR_bjet_far_top = ROOT.TH1D("dR_bjet_far_top","dR_bjet_far_top",40,0,7)
dR_bjet_far_top.Sumw2()

mass_lep_close = ROOT.TH1D("mass_lep_close","mass_lep_close",150,0,1000)
mass_lep_close.Sumw2()
mass_lep_close_top = ROOT.TH1D("mass_lep_close_top","mass_lep_close_top",150,0,1000)
mass_lep_close_top.Sumw2()
mass_lep_far = ROOT.TH1D("mass_lep_far","mass_lep_far",150,0,1000)
mass_lep_far.Sumw2()
mass_lep_far_top = ROOT.TH1D("mass_lep_far_top","mass_lep_far_top",150,0,1000)
mass_lep_far_top.Sumw2()

mass_lep_el = ROOT.TH1D("mass_lep_el","mass_lep_el",150,0,1000)
mass_lep_el.Sumw2()
mass_lep_el_top = ROOT.TH1D("mass_lep_el_top","mass_lep_el_top",150,0,1000)
mass_lep_el_top.Sumw2()
mass_lep_mu = ROOT.TH1D("mass_lep_mu","mass_lep_mu",150,0,1000)
mass_lep_mu.Sumw2()
mass_lep_mu_top = ROOT.TH1D("mass_lep_mu_top","mass_lep_mu_top",150,0,1000)
mass_lep_mu_top.Sumw2()

mass_lep_1pt = ROOT.TH1D("mass_lep_1pt","mass_lep_1pt",150,0,1000)
mass_lep_1pt.Sumw2()
mass_lep_1pt_top = ROOT.TH1D("mass_lep_1pt_top","mass_lep_1pt_top",150,0,1000)
mass_lep_1pt_top.Sumw2()
mass_lep_2pt = ROOT.TH1D("mass_lep_2pt","mass_lep_2pt",150,0,1000)
mass_lep_2pt.Sumw2()
mass_lep_2pt_top = ROOT.TH1D("mass_lep_2pt_top","mass_lep_2pt_top",150,0,1000)
mass_lep_2pt_top.Sumw2()

myfile = ROOT.TFile.Open("3j3b.root","RECREATE")
mytree_sig = ROOT.TTree("sig","Signal")
mytree_bkg = ROOT.TTree("bkg","Background")

rlcs = array("f",[0])
rlfs = array('f',[0])
mlcs = array('f',[0])
mlfs = array('f',[0])
rbcs = array('f',[0])
rbfs = array('f',[0])
rles = array('f',[0])
rlms = array('f',[0])
mles = array('f',[0])
mlms = array('f',[0])
rl1s = array('f',[0])
rl2s = array('f',[0])
ml1s = array('f',[0])
ml2s = array('f',[0])
totws = array('f',[0])
topFs = array('l',[0])

mytree_sig.Branch("dR_lep_close",rlcs,"dR_lep_close_sig/F")
mytree_sig.Branch("dR_lep_far",rlfs,"dR_lep_far_sig/F")
mytree_sig.Branch("mass_lep_close",mlcs,"mass_lep_close_sig/F")
mytree_sig.Branch("mass_lep_far",mlfs,"mass_lep_far_sig/F")
mytree_sig.Branch("dR_bjet_close",rbcs,"dR_bjet_close_sig/F")
mytree_sig.Branch("dR_bjet_far",rbfs,"dR_bjet_far_sig/F")
mytree_sig.Branch("dR_lep_el",rles,"dR_lep_el_sig/F")
mytree_sig.Branch("dR_lep_mu",rlms,"dR_lep_mu_sig/F")
mytree_sig.Branch("mass_lep_el",mles,"mass_lep_el_sig/F")
mytree_sig.Branch("mass_lep_mu",mlms,"mass_lep_mu_sig/F")
mytree_sig.Branch("dR_lep_1pt",rl1s,"dR_lep_1pt_sig/F")
mytree_sig.Branch("dR_lep_2pt",rl2s,"dR_lep_2pt_sig/F")
mytree_sig.Branch("mass_lep_1pt",ml1s,"mass_lep_1pt_sig/F")
mytree_sig.Branch("mass_lep_2pt",ml2s,"mass_lep_2pt_sig/F")
mytree_sig.Branch("total_event_weight",totws,"total_event_weight_sig/F")
mytree_sig.Branch("jet_GBHInit_topHadronOriginFlag",topFs,"jet_GBHInit_topHadronOriginFlag_sig/l")

rlcb = array('f',[0])
rlfb = array('f',[0])
mlcb = array('f',[0])
mlfb = array('f',[0])
rbcb = array('f',[0])
rbfb = array('f',[0])
rleb = array('f',[0])
rlmb = array('f',[0])
mleb = array('f',[0])
mlmb = array('f',[0])
rl1b = array('f',[0])
rl2b = array('f',[0])
ml1b = array('f',[0])
ml2b = array('f',[0])
totwb = array('f',[0])
topFb = array('l',[0])

mytree_bkg.Branch("dR_lep_close",rlcb,"dR_lep_close_bkg/F")
mytree_bkg.Branch("dR_lep_far",rlfb,"dR_lep_far_bkg/F")
mytree_bkg.Branch("mass_lep_close",mlcb,"mass_lep_close_bkg/F")
mytree_bkg.Branch("mass_lep_far",mlfb,"mass_lep_far_bkg/F")
mytree_bkg.Branch("dR_bjet_close",rbcb,"dR_bjet_close_bkg/F")
mytree_bkg.Branch("dR_bjet_far",rbfb,"dR_bjet_far_bkg/F")
mytree_bkg.Branch("dR_lep_el",rleb,"dR_lep_el_bkg/F")
mytree_bkg.Branch("dR_lep_mu",rlmb,"dR_lep_mu_bkg/F")
mytree_bkg.Branch("mass_lep_el",mleb,"mass_lep_el_bkg/F")
mytree_bkg.Branch("mass_lep_mu",mlmb,"mass_lep_mu_bkg/F")
mytree_bkg.Branch("dR_lep_1pt",rl1b,"dR_lep_1pt_bkg/F")
mytree_bkg.Branch("dR_lep_2pt",rl2b,"dR_lep_2pt_bkg/F")
mytree_bkg.Branch("mass_lep_1pt",ml1b,"mass_lep_1pt_bkg/F")
mytree_bkg.Branch("mass_lep_2pt",ml2b,"mass_lep_2pt_bkg/F")
mytree_bkg.Branch("total_event_weight",totwb,"total_event_weight_bkg/F")
mytree_bkg.Branch("jet_GBHInit_topHadronOriginFlag",topFb,"jet_GBHInit_topHadronOriginFlag_bkg/l")

for i in range(len(lines)):
	print(i+1,"/",len(lines))
	name = lines[i]
	if "eantipov" in name:continue
	inFile = ROOT.TFile.Open(name.strip(),"READ")
	tree = inFile.Get("nominal")
	if "mc16" in name:
		name_copy = name.split(".")
		ID = int(name_copy[2])
	else:ID=0
	if ID != 410472 and ID not in range(411076,411079): continue
	for j in range(tree.GetEntries()):
		tree.GetEntry(j)
		el_pt = getattr(tree,"el_pt")
		mu_pt = getattr(tree,"mu_pt")
		el_eta = getattr(tree,"el_eta")
		mu_eta = getattr(tree,"mu_eta")
		el_phi = getattr(tree,"el_phi")
		mu_phi = getattr(tree,"mu_phi")
		el_e = getattr(tree,"el_e")
		mu_e = getattr(tree,"mu_e")
		el_charge = getattr(tree,"el_charge")
		mu_charge = getattr(tree,"mu_charge")
		jet_pt = getattr(tree,"jet_pt")
		jet_eta = getattr(tree,"jet_eta")
		jet_phi = getattr(tree,"jet_phi")
		jet_e = getattr(tree,"jet_e")
		btag_77 = getattr(tree,"jet_isbtagged_DL1r_77")
		if "mc16" in name:
			w_mc = getattr(tree,"weight_mc")
			w_pu = getattr(tree,"weight_pileup")
			w_leptonSF = getattr(tree,"weight_leptonSF")
			w_DL1r_77 = getattr(tree,"weight_bTagSF_DL1r_77")
			w_jvt = getattr(tree,"weight_jvt")
			from_top = getattr(tree,"jet_GBHInit_topHadronOriginFlag")
			jet_truthflav = getattr(tree,"jet_truthflav")
		if ID == 410472 or ID in range(411076,411079):
			topHFFF = getattr(tree,"topHeavyFlavorFilterFlag")
			if "410472" in name and topHFFF != 0: continue 
			if "411076" in name and topHFFF != 1: continue 
			if "411077" in name and topHFFF != 2: continue 
			if "411078" in name and topHFFF != 3: continue

		if len(el_pt) != 1 or len(mu_pt)!= 1: continue

		if el_charge[0] == mu_charge[0]: continue

		if el_pt[0]/1000 < 28 or mu_pt[0]/1000 < 28: continue

		if len(jet_pt) < 3: continue

		if jet_pt[-1]/1000 < 25: continue
								
		mass_el = ROOT.Math.PtEtaPhiEVector()
		mass_mu = ROOT.Math.PtEtaPhiEVector()
		mass_el.SetCoordinates(el_pt[0]/1000,el_eta[0],el_phi[0],el_e[0]/1000)
		mass_mu.SetCoordinates(mu_pt[0]/1000,mu_eta[0],mu_phi[0],mu_e[0]/1000)
		if "data" in name:
			mass_bjet = []
			for k in range(len(jet_pt)):
				if btag_77[k] == '\x01' :
					mass_b = ROOT.Math.PtEtaPhiEVector()
					mass_b.SetCoordinates(jet_pt[k]/1000,jet_eta[k],jet_phi[k],jet_e[k]/1000)
					mass_bjet.append(mass_b)
			if len(mass_bjet) < 3: continue
			for k in range(len(mass_bjet)):
				RRR = []
				dRel = ROOT.Math.VectorUtil.DeltaR(mass_el,mass_bjet[k])
				dRmu = ROOT.Math.VectorUtil.DeltaR(mass_mu,mass_bjet[k])
				dRR = [dRel,dRmu]
				sortdRR = sorted(dRR)
				dR_lep_close_data.Fill(sortdRR[0])
				dR_lep_far_data.Fill(sortdRR[1])
				dR_lep_el_data.Fill(dRel)
				dR_lep_mu_data.Fill(dRmu)
				ME = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_el)
				MM = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_mu)
				mass_lep_el_data.Fill(ME)
				mass_lep_mu_data.Fill(MM)
				if el_pt[0] >= mu_pt[0]:
					dR_lep_1pt_data.Fill(dRel)
					dR_lep_2pt_data.Fill(dRmu)
					mass_lep_1pt_data.Fill(ME)
					mass_lep_2pt_data.Fill(MM)
				else:
					dR_lep_2pt_data.Fill(dRel)
					dR_lep_1pt_data.Fill(dRmu)
					mass_lep_2pt_data.Fill(ME)
					mass_lep_1pt_data.Fill(MM)
				if sortdRR[0] == dRR[0]:
					mass_lep_close_data.Fill(ME)
					mass_lep_far_data.Fill(MM)
				else:
					mass_lep_far_data.Fill(ME)
					mass_lep_close_data.Fill(MM)
				for n in range(len(mass_bjet)):
					if k == n:continue
					RRR.append(ROOT.Math.VectorUtil.DeltaR(mass_bjet[k],mass_bjet[n]))
				dR_bjet_close_data.Fill(min(RRR))
				dR_bjet_far_data.Fill(max(RRR))
		if "mc16" in name: 
			mass_bjet = []
			origin = []
			for k in range(len(jet_pt)):
				if jet_truthflav[k] == 5 :
					mass_b = ROOT.Math.PtEtaPhiEVector()
					mass_b.SetCoordinates(jet_pt[k]/1000,jet_eta[k],jet_phi[k],jet_e[k]/1000)
					mass_bjet.append(mass_b)
					origin.append(from_top[k])
			if len(mass_bjet) < 3: continue
			w = weight()
			for k in range(len(mass_bjet)):
				dRel = ROOT.Math.VectorUtil.DeltaR(mass_el,mass_bjet[k])
				dRmu = ROOT.Math.VectorUtil.DeltaR(mass_mu,mass_bjet[k])
				dRR = [dRel,dRmu]
				sortdRR = sorted(dRR)
				ME = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_el)
				MM = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_mu)
				if origin[k] == 4:
					dR_lep_close_top.Fill(sortdRR[0],w)
					dR_lep_far_top.Fill(sortdRR[1],w)
					dR_lep_el_top.Fill(dRel,w)
					dR_lep_mu_top.Fill(dRmu,w)
					mass_lep_el_top.Fill(ME,w)
					mass_lep_mu_top.Fill(MM,w)
					rlcb[0] = sortdRR[0]
					rlfb[0] = sortdRR[1]
					rleb[0] = dRel
					rlmb[0] = dRmu
					mleb[0] = ME
					mlmb[0] = MM
					topFb[0] = origin[k]
					totwb[0] = w
					if el_pt[0] >= mu_pt[0]:	
						dR_lep_1pt_top.Fill(dRel,w)
						dR_lep_2pt_top.Fill(dRmu,w)
						mass_lep_1pt_top.Fill(ME,w)
						mass_lep_2pt_top.Fill(MM,w)
						rl1b[0] = dRel
						rl2b[0] = dRmu
						ml1b[0] = ME
						ml2b[0] = MM
					else:
						dR_lep_2pt_top.Fill(dRel,w)
						dR_lep_1pt_top.Fill(dRmu,w)
						mass_lep_2pt_top.Fill(ME,w)
						mass_lep_1pt_top.Fill(MM,w)
						rl2b[0] = dRel
						rl1b[0] = dRmu
						ml2b[0] = ME
						ml1b[0] = MM
				else:
					dR_lep_close.Fill(sortdRR[0],w)
					dR_lep_far.Fill(sortdRR[1],w)
					dR_lep_el.Fill(dRel,w)
					dR_lep_mu.Fill(dRmu,w)
					mass_lep_el.Fill(ME,w)
					mass_lep_mu.Fill(MM,w)
					rlcs[0] = sortdRR[0]
					rlfs[0] = sortdRR[1]
					rles[0] = dRel
					rlms[0] = dRmu
					mles[0] = ME
					mlms[0] = MM
					totws[0] = w
					topFs[0] = origin[k]
					if el_pt[0] >= mu_pt[0]:	
						dR_lep_1pt.Fill(dRel,w)
						dR_lep_2pt.Fill(dRmu,w)
						mass_lep_1pt.Fill(ME,w)
						mass_lep_2pt.Fill(MM,w)
						rl1s[0] = dRel
						rl2s[0] = dRmu
						ml1s[0] = ME
						ml2s[0] = MM
					else:
						dR_lep_2pt.Fill(dRel,w)
						dR_lep_1pt.Fill(dRmu,w)
						mass_lep_2pt.Fill(ME,w)
						mass_lep_1pt.Fill(MM,w)
						rl2s[0] = dRel
						rl1s[0] = dRmu
						ml2s[0] = ME
						ml1s[0] = MM
				if sortdRR[0] == dRR[0]:
					if origin[k] == 4:
						mass_lep_close_top.Fill(ME,w)
						mass_lep_far_top.Fill(MM,w)
						mlcb[0] = ME
						mlfb[0] = MM
					else:
						mass_lep_close.Fill(ME,w)
						mass_lep_far.Fill(MM,w)
						mlcs[0] = ME
						mlfs[0] = MM
				else:
					if origin[k] == 4:
						mass_lep_far_top.Fill(ME,w)
						mass_lep_close_top.Fill(MM,w)
						mlfb[0] = ME
						mlcb[0] = MM
					else:
						mass_lep_far.Fill(ME,w)
						mass_lep_close.Fill(MM,w)
						mlfs[0] = ME
						mlcs[0] = MM
				RRR = []
				for n in range(len(mass_bjet)):
					if k == n:continue
					RRR.append(ROOT.Math.VectorUtil.DeltaR(mass_bjet[k],mass_bjet[n]))
				if origin[k] == 4:
					dR_bjet_close_top.Fill(min(RRR),w)
					dR_bjet_far_top.Fill(max(RRR),w)
					rbcb[0] = min(RRR)
					rbfb[0] = max(RRR)
				else:								
					dR_bjet_close.Fill(min(RRR),w)
					dR_bjet_far.Fill(max(RRR),w)
					rbcs[0] = min(RRR)
					rbfs[0] = max(RRR)
				mytree_sig.Fill()
				mytree_bkg.Fill()
	dR_lep_el_top.SetDirectory(0)
	dR_lep_mu_top.SetDirectory(0)
	mass_lep_el_top.SetDirectory(0)
	mass_lep_mu_top.SetDirectory(0)
	dR_lep_el.SetDirectory(0)
	dR_lep_mu.SetDirectory(0)
	mass_lep_el.SetDirectory(0)
	mass_lep_mu.SetDirectory(0)
				
	dR_lep_1pt_top.SetDirectory(0)
	dR_lep_2pt_top.SetDirectory(0)
	mass_lep_1pt_top.SetDirectory(0)
	mass_lep_2pt_top.SetDirectory(0)
	dR_lep_1pt.SetDirectory(0)
	dR_lep_2pt.SetDirectory(0)
	mass_lep_1pt.SetDirectory(0)
	mass_lep_2pt.SetDirectory(0)
				
	dR_lep_close_top.SetDirectory(0)
	dR_lep_far_top.SetDirectory(0)
	mass_lep_close_top.SetDirectory(0)
	mass_lep_far_top.SetDirectory(0)
	dR_bjet_close_top.SetDirectory(0)
	dR_bjet_far_top.SetDirectory(0)
				
	dR_lep_close.SetDirectory(0)
	dR_lep_far.SetDirectory(0)
	mass_lep_close.SetDirectory(0)
	mass_lep_far.SetDirectory(0)
	dR_bjet_close.SetDirectory(0)
	dR_bjet_far.SetDirectory(0)
	mytree_sig.SetDirectory(0)
	mytree_bkg.SetDirectory(0)
	inFile.Close()

myfile.cd()

mytree_sig.Write()
mytree_bkg.Write()

myfile.Close()

outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
outHistFile.cd()


dR_lep_close.Write()
dR_lep_far.Write()
mass_lep_close.Write()
mass_lep_far.Write()
dR_bjet_close.Write()
dR_bjet_far.Write()

dR_lep_el.Write()
dR_lep_mu.Write()
mass_lep_el.Write()
mass_lep_mu.Write()
dR_lep_el_top.Write()
dR_lep_mu_top.Write()
mass_lep_el_top.Write()
mass_lep_mu_top.Write()

dR_lep_1pt.Write()
dR_lep_2pt.Write()
mass_lep_1pt.Write()
mass_lep_2pt.Write()
dR_lep_1pt_top.Write()
dR_lep_2pt_top.Write()
mass_lep_1pt_top.Write()
mass_lep_2pt_top.Write()

dR_lep_close_top.Write()
dR_lep_far_top.Write()
mass_lep_close_top.Write()
mass_lep_far_top.Write()
dR_bjet_close_top.Write()
dR_bjet_far_top.Write()

outHistFile.Close()
