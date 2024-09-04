import ROOT
import sys
from numpy import sqrt
if len(sys.argv)!= 3:
	print("USAGE: %s<input file><output file>"%(sys.argv[0]))
	sys.exit(1)
histFileName = sys.argv[1]
plotFileName = sys.argv[2]
print("Reading from",histFileName,"then writing to",plotFileName)
colors = [1,632,416]
name = ["from top","not from top"]
label = ["#DeltaR_{min} (b-jet, lep)","#Delta R_{max} (b-jet, lep)",
"#DeltaR (b-jet, e)","#DeltaR (b-jet, \mu)",
"\DeltaR (b-jet, leading p_{T} lep)","\DeltaR (b-jet, subleading p_{T} lep)",
"\DeltaR_{min}(b-jet, b-jet)","\DeltaR_{max}(b-jet, b-jet)",
"m_{inv} (b-jet, close lep) [GeV]","m_{inv} (b-jet, far lep) [GeV]",
"m_{inv} (b-jet, e) [GeV]","m_{inv} (b-jet, \mu) [GeV]",
"m_{inv} (b-jet, leading p_{T} lep) [GeV]","m_{inv} (b-jet, subleading p_{T} lep) [GeV]",
"m_{inv_large} (b-jet, b-jet) [GeV]","m_{inv_small} (b-jet, b-jet) [GeV]",
"p_{T} (b-jet) [GeV]","E (b-jet) [GeV]","Eta (b-jet)","Phi (b-jet)","#DeltaR_{min} (b-jet, unb-jet)","#Delta R_{max} (b-jet, unb-jet)"]
limit = [7,7,7,7,7,7,7,7,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,7,7,7,7]
Names = ["dR_lep_close","dR_lep_far","dR_lep_el","dR_lep_mu","dR_lep_1pt","dR_lep_2pt","dR_bjet_close","dR_bjet_far","mass_lep_close","mass_lep_far",
	"mass_lep_el","mass_lep_mu","mass_lep_1pt","mass_lep_2pt","mass_bjet_large","mass_bjet_small","pt","Energy","eta","phi",
	"dR_unb_close","dR_unb_far"]
canvas = ROOT.TCanvas("canvas")
canvas.cd()
canvas.Print(plotFileName+"[")

for k in range(22):
	histFile = ROOT.TFile.Open(histFileName,"READ")	
	mc = []	
	mc.append(histFile.Get(Names[k]))
	mc.append(histFile.Get(Names[k]+"_top"))
	for i in range(len(mc)):
		mc[i].SetDirectory(0)
	histFile.Close()

	mcc=[]
	for i in range(len(mc)):
		mcc.append(mc[i].Clone())	
		mcc[i].SetStats(0)
		mcc[i].SetLineWidth(2)
		mcc[i].SetLineColor(colors[i+1])
		mcc[i].Scale(1.0/mc[i].Integral())
	ratio = []
	for j in range(3):
		ratio.append(ROOT.TH1D("ratio"+str(k)+str(j),"ratio"+str(k)+str(j),40,0,limit[k]))
		ratio[j].SetStats(0)	
		ratio[j].SetLineColor(colors[j])
	#	ratio[j].SetMarkerStyle(20)
	#	ratio[j].SetMarkerSize(0.5)
		ratio[j].SetLineWidth(1)
	for i in range(41):
		sig1 = mcc[1].Integral(i,41)
		sig0 = mcc[1].Integral(0,41)
		bkg0 = mcc[0].Integral(0,41)
		bkg1 = mcc[0].Integral(0,i-1)
		if bkg0 == 0 or sig0 == 0:continue
		ratio[0].SetBinContent(i,(sig1+bkg1)/(sig0+bkg0))
		ratio[1].SetBinContent(i,bkg1/bkg0)
		ratio[2].SetBinContent(i,sig1/sig0)
	m=0
	ratio[m].SetTitle("")
	ratio[m].GetXaxis().SetTitle(label[k])
	ratio[m].GetXaxis().SetTitleSize(0.12)
	ratio[m].GetXaxis().SetLabelSize(0.12)
	ratio[m].GetYaxis().SetTitleSize(0.11)
	ratio[m].GetYaxis().SetLabelSize(0.1)
	ratio[m].GetYaxis().SetTitle("Efficiency")
	ratio[m].GetYaxis().SetTitleOffset(0.3)
	ratio[m].GetYaxis().SetNdivisions(207)
	ratio[m].GetYaxis().SetRangeUser(0.3,0.7)
	mcc[0].SetMinimum(1)

	mcc[0].SetTitle("")
	mcc[0].GetYaxis().SetTitle("Probability density of b-jets")
	mcc[0].GetXaxis().SetLabelSize(0)
	mcc[0].GetXaxis().SetTitleSize(0)

	canvas.Clear()
	pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
	pad1.SetLogy(True)
	pad1.SetBottomMargin(0)
	pad1.Draw()
	pad1.cd()
	mcc[0].Draw("h")
	mcc[1].Draw("h,same")
#	ROOT.gPad.Update()

	legend = ROOT.TLegend(0.7,0.75,0.85,0.85)
	for i in range(len(mc)):
		legend.AddEntry(mcc[i],name[i])
	legend.SetLineWidth(0)
	legend.Draw("same")

	canvas.cd()
	pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
	pad2.SetBottomMargin(0.25)
	pad2.SetTopMargin(0.05)
	pad2.Draw()
	pad2.cd()
	ratio[m].Draw("h")
	#ratio[m-1].Draw("h,same")
	#ratio[m-2].Draw("h,same")
	

	canvas.Print(plotFileName)
canvas.Print(plotFileName+"]")
