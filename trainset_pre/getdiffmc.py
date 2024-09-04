from numpy import array
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
def channel(ID):               
	if ID == 410472 or ID in range(411076,411079):ch_num = 6
	if ID == 410648 or ID == 410649 or ID == 410644 or ID == 410645 or ID == 410658 or ID == 410659:ch_num = 5
	if ID in range(410155, 410158) or ID in range(410218, 410221) or ID in range(410276, 410279):ch_num = 4
	if ID == 346345:ch_num = 3
	if ID == 364250 or ID == 364253 or ID == 364254 or ID == 345705 or ID == 345706 or ID == 345723 or ID == 363356 or ID == 363358 or ID in range(364283, 364291) and ID != 364286:ch_num = 2
	if ID == 410560 or ID == 410408 or ID == 346678 or ID == 346676 or ID == 412043:ch_num = 1
	if ID in range(364100,364142):ch_num = 0
	return ch_num
var = ["Z","other","diboson","H","V","top","ttbar","data"]
dR_lep_close = []
dR_lep_far = []
dR_lep_el = []
dR_lep_mu = []
dR_lep_1pt = []
dR_lep_2pt = []
dR_bjet_close = []
dR_bjet_far = []
mass_lep_close = []
mass_lep_far = []
mass_lep_el = []
mass_lep_mu = []
mass_lep_1pt = []
mass_bjet_large = []
mass_bjet_small = []
mass_lep_2pt = []
for i in range(len(var)):
	dR_lep_close.append(ROOT.TH1D("dR_lep_close"+var[i],"dR_lep_close"+var[i],40,0,7))
	dR_lep_close[i].Sumw2()
	dR_lep_far.append(ROOT.TH1D("dR_lep_far"+var[i],"dR_lep_far"+var[i],40,0,7))
	dR_lep_far[i].Sumw2()

	dR_lep_el.append(ROOT.TH1D("dR_lep_el"+var[i],"dR_lep_el"+var[i],40,0,7))
	dR_lep_el[i].Sumw2()
	dR_lep_mu.append(ROOT.TH1D("dR_lep_mu"+var[i],"dR_lep_mu"+var[i],40,0,7))
	dR_lep_mu[i].Sumw2()

	dR_lep_1pt.append(ROOT.TH1D("dR_lep_1pt"+var[i],"dR_lep_1pt"+var[i],40,0,7))
	dR_lep_1pt[i].Sumw2()
	dR_lep_2pt.append(ROOT.TH1D("dR_lep_2pt"+var[i],"dR_lep_2pt"+var[i],40,0,7))
	dR_lep_2pt[i].Sumw2()

	dR_bjet_close.append(ROOT.TH1D("dR_bjet_close"+var[i],"dR_bjet_close"+var[i],40,0,7))
	dR_bjet_close[i].Sumw2()
	dR_bjet_far.append(ROOT.TH1D("dR_bjet_far"+var[i],"dR_bjet_far"+var[i],40,0,7))
	dR_bjet_far[i].Sumw2()

	mass_lep_close.append(ROOT.TH1D("mass_lep_close"+var[i],"mass_lep_close"+var[i],150,0,1000))
	mass_lep_close[i].Sumw2()
	mass_lep_far.append(ROOT.TH1D("mass_lep_far"+var[i],"mass_lep_far"+var[i],150,0,1000))
	mass_lep_far[i].Sumw2()

	mass_lep_el.append(ROOT.TH1D("mass_lep_el"+var[i],"mass_lep_el"+var[i],150,0,1000))
	mass_lep_el[i].Sumw2()
	mass_lep_mu.append(ROOT.TH1D("mass_lep_mu"+var[i],"mass_lep_mu"+var[i],150,0,1000))
	mass_lep_mu[i].Sumw2()

	mass_lep_1pt.append(ROOT.TH1D("mass_lep_1pt"+var[i],"mass_lep_1pt"+var[i],150,0,1000))
	mass_lep_1pt[i].Sumw2()
	mass_lep_2pt.append(ROOT.TH1D("mass_lep_2pt"+var[i],"mass_lep_2pt"+var[i],150,0,1000))
	mass_lep_2pt[i].Sumw2()
	
	mass_bjet_large.append(ROOT.TH1D("mass_bjet_large"+var[i],"mass_bjet_large"+var[i],150,0,1000))
	mass_bjet_large[i].Sumw2()
	mass_bjet_small.append(ROOT.TH1D("mass_bjet_small"+var[i],"mass_bjet_small"+var[i],150,0,1000))
	mass_bjet_small[i].Sumw2()

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
				MMM = []
				dRel = ROOT.Math.VectorUtil.DeltaR(mass_el,mass_bjet[k])
				dRmu = ROOT.Math.VectorUtil.DeltaR(mass_mu,mass_bjet[k])
				dRR = [dRel,dRmu]
				sortdRR = sorted(dRR)
				dR_lep_close[7].Fill(sortdRR[0])
				dR_lep_far[7].Fill(sortdRR[1])
				dR_lep_el[7].Fill(dRel)
				dR_lep_mu[7].Fill(dRmu)
				ME = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_el)
				MM = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_mu)
				mass_lep_el[7].Fill(ME)
				mass_lep_mu[7].Fill(MM)
				if el_pt[0] >= mu_pt[0]:
					dR_lep_1pt[7].Fill(dRel)
					dR_lep_2pt[7].Fill(dRmu)
					mass_lep_1pt[7].Fill(ME)
					mass_lep_2pt[7].Fill(MM)
				else:
					dR_lep_2pt[7].Fill(dRel)
					dR_lep_1pt[7].Fill(dRmu)
					mass_lep_2pt[7].Fill(ME)
					mass_lep_1pt[7].Fill(MM)
				if sortdRR[0] == dRR[0]:
					mass_lep_close[7].Fill(ME)
					mass_lep_far[7].Fill(MM)
				else:
					mass_lep_far[7].Fill(ME)
					mass_lep_close[7].Fill(MM)
				for n in range(len(mass_bjet)):
					if k == n:continue
					RRR.append(ROOT.Math.VectorUtil.DeltaR(mass_bjet[k],mass_bjet[n]))
					MMM.append(ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_bjet[n]))
				dR_bjet_close[7].Fill(min(RRR))
				dR_bjet_far[7].Fill(max(RRR))
				mass_bjet_small[7].Fill(min(MMM))
				mass_bjet_large[7].Fill(max(MMM))
		if "mc16" in name: 
			w = weight()
			ch = channel(ID)
			mass_bjet = []
			for k in range(len(jet_pt)):
				if jet_truthflav[k] == 5 :
					mass_b = ROOT.Math.PtEtaPhiEVector()
					mass_b.SetCoordinates(jet_pt[k]/1000,jet_eta[k],jet_phi[k],jet_e[k]/1000)
					mass_bjet.append(mass_b)
			if len(mass_bjet) < 3: continue
			for k in range(len(mass_bjet)):
				dRel = ROOT.Math.VectorUtil.DeltaR(mass_el,mass_bjet[k])
				dRmu = ROOT.Math.VectorUtil.DeltaR(mass_mu,mass_bjet[k])
				dRR = [dRel,dRmu]
				sortdRR = sorted(dRR)
				ME = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_el)
				MM = ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_mu)
				dR_lep_close[ch].Fill(sortdRR[0],w)
				dR_lep_far[ch].Fill(sortdRR[1],w)
				dR_lep_el[ch].Fill(dRel,w)
				dR_lep_mu[ch].Fill(dRmu,w)
				mass_lep_el[ch].Fill(ME,w)
				mass_lep_mu[ch].Fill(MM,w)
				if el_pt[0] >= mu_pt[0]:	
					dR_lep_1pt[ch].Fill(dRel,w)
					dR_lep_2pt[ch].Fill(dRmu,w)
					mass_lep_1pt[ch].Fill(ME,w)
					mass_lep_2pt[ch].Fill(MM,w)
				else:
					dR_lep_2pt[ch].Fill(dRel,w)
					dR_lep_1pt[ch].Fill(dRmu,w)
					mass_lep_2pt[ch].Fill(ME,w)
					mass_lep_1pt[ch].Fill(MM,w)
				if sortdRR[0] == dRR[0]:
					mass_lep_close[ch].Fill(ME,w)
					mass_lep_far[ch].Fill(MM,w)
				else:
					mass_lep_far[ch].Fill(ME,w)
					mass_lep_close[ch].Fill(MM,w)
				RRR = []
				MMM = []
				for n in range(len(mass_bjet)):
					if k == n:continue
					RRR.append(ROOT.Math.VectorUtil.DeltaR(mass_bjet[k],mass_bjet[n]))
					MMM.append(ROOT.Math.VectorUtil.InvariantMass(mass_bjet[k],mass_bjet[n]))
				dR_bjet_close[ch].Fill(min(RRR),w)
				dR_bjet_far[ch].Fill(max(RRR),w)
				mass_bjet_small[ch].Fill(min(MMM),w)
				mass_bjet_large[ch].Fill(max(MMM),w)
	inFile.Close()
for z in range(len(var)):
				
	dR_lep_el[z].SetDirectory(0)
	dR_lep_mu[z].SetDirectory(0)
	mass_lep_el[z].SetDirectory(0)
	mass_lep_mu[z].SetDirectory(0)
				
	dR_lep_1pt[z].SetDirectory(0)
	dR_lep_2pt[z].SetDirectory(0)
	mass_lep_1pt[z].SetDirectory(0)
	mass_lep_2pt[z].SetDirectory(0)
				
				
	dR_lep_close[z].SetDirectory(0)
	dR_lep_far[z].SetDirectory(0)
	mass_lep_close[z].SetDirectory(0)
	mass_lep_far[z].SetDirectory(0)
	dR_bjet_close[z].SetDirectory(0)
	dR_bjet_far[z].SetDirectory(0)
	mass_bjet_large[z].SetDirectory(0)
	mass_bjet_small[z].SetDirectory(0)

outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
outHistFile.cd()
for i in range(len(var)):

	dR_lep_close[i].Write()
	dR_lep_far[i].Write()
	mass_lep_close[i].Write()
	mass_lep_far[i].Write()
	dR_bjet_close[i].Write()
	dR_bjet_far[i].Write()

	dR_lep_el[i].Write()
	dR_lep_mu[i].Write()
	mass_lep_el[i].Write()
	mass_lep_mu[i].Write()

	dR_lep_1pt[i].Write()
	dR_lep_2pt[i].Write()
	mass_lep_1pt[i].Write()
	mass_lep_2pt[i].Write()
	mass_bjet_large[i].Write()
	mass_bjet_small[i].Write()

outHistFile.Close()
