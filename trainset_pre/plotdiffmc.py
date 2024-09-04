import ROOT
import sys
if len(sys.argv)!= 3:
	print("USAGE: %s<input file><output file>"%(sys.argv[0]))
	sys.exit(1)
histFileName = sys.argv[1]
plotFileName = sys.argv[2]
print("Reading from",histFileName,"then writing to",plotFileName)
colors = [4,616-9,416+1,2,9,5,18]
name = ["Z+jets","others","diboson","tt+H","tt+V","single_top","ttbar"]
limit = [7,7,7,7,7,7,7,7,1000,1000,1000,1000,1000,1000,1000,1000]
var = ["Z","other","diboson","H","V","top","ttbar","data"]
label = ["dR_lep_close","dR_lep_far","dR_lep_el","dR_lep_mu","dR_lep_1pt","dR_lep_2pt","dR_bjet_close",
	"dR_bjet_far","mass_lep_close","mass_lep_far","mass_lep_el","mass_lep_mu","mass_lep_1pt","mass_lep_2pt","mass_bjet_large","mass_bjet_small"]
label_name = ["#DeltaR_{min} (b-jet, lep)","#Delta R_{max} (b-jet, lep)",
"#DeltaR (b-jet, e)","#DeltaR (b-jet, \mu)",
"\DeltaR (b-jet, leading p_{T} lep)","\DeltaR (b-jet, subleading p_{T} lep)",
"\DeltaR_{min}(b-jet, b-jet)","\DeltaR_{max}(b-jet, b-jet)",
"m_{inv} (b-jet, close lep) [GeV]","m_{inv} (b-jet, far lep) [GeV]",
"m_{inv} (b-jet, e) [GeV]","m_{inv} (b-jet, \mu) [GeV]",
"m_{inv} (b-jet, leading p_{T} lep) [GeV]","m_{inv} (b-jet, subleading p_{T} lep) [GeV]",
"m_{inv_large} (b-jet, b-jet) [GeV]","m_{inv_small} (b-jet, b-jet) [GeV]"]
canvas = ROOT.TCanvas("canvas")
canvas.cd()
canvas.Print(plotFileName+"[")
for k in range(len(label)):
	histFile = ROOT.TFile.Open(histFileName,"READ")	
	mc = []	
	for i in range(len(var)-1):
		mc.append(histFile.Get(label[k]+var[i]))
	data = histFile.Get(label[k]+var[7])
	for i in range(len(mc)):
		mc[i].SetDirectory(0)
	data.SetDirectory(0)
	histFile.Close()

	for i in range(len(mc)):
		mc[i].SetStats(0)
	data.SetStats(0)

	combine_mc = mc[0].Clone()
	for i in range(1,len(mc)):
		combine_mc.Add(mc[i])
	ratio = data.Clone()
	ratio.Divide(combine_mc)
	ratio.SetMarkerColor(1)
	ratio.SetMarkerStyle(20)
	ratio.SetMarkerSize(0.5)
	ratio.SetLineWidth(1)
	ratio.SetTitle("")
	ratio.GetXaxis().SetTitle(label_name[k])
	ratio.GetXaxis().SetTitleSize(0.12)
	ratio.GetXaxis().SetLabelSize(0.12)
	ratio.GetYaxis().SetTitleSize(0.11)
	ratio.GetYaxis().SetLabelSize(0.1)
	ratio.GetYaxis().SetTitle("Data / MC")
	ratio.GetYaxis().SetTitleOffset(0.3)
	ratio.GetYaxis().SetRangeUser(0.5,1.5)
	ratio.GetYaxis().SetNdivisions(207)

	total_mc = ROOT.THStack("total_mc","total_mc")
	for i in range(0,len(mc)):
		mc[i].SetFillColor(colors[i])
		mc[i].SetLineColor(colors[i])
		total_mc.Add(mc[i])
	total_mc.SetMinimum(1)

	data.SetMinimum(1)
	data.SetMarkerColor(1)
	data.SetMarkerStyle(20)
	data.SetMarkerSize(0.5)
	data.SetLineWidth(1)

	canvas.Clear()
	pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
	pad1.SetLogy(True)
	pad1.SetBottomMargin(0)
	pad1.Draw()
	pad1.cd()
	total_mc.Draw("h")
	data.Draw("E X0,same")
#	ROOT.gStyle.SetHistMinimumZero(ROOT.kTRUE)
	ROOT.gPad.Update()
	total_mc.SetTitle("")
	total_mc.GetYaxis().SetTitle("Number of events")
	total_mc.GetXaxis().SetLabelSize(0)
	total_mc.GetXaxis().SetTitleSize(0)

	legend = ROOT.TLegend(0.7,0.5,0.85,0.8)
	for i in range(len(mc)):
		legend.AddEntry(mc[i],name[i])
	legend.AddEntry(data,"data")
	legend.SetLineWidth(0)
	legend.Draw("same")

	canvas.cd()
	pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
	pad2.SetBottomMargin(0.25)
	pad2.SetTopMargin(0.05)
	pad2.Draw()
	pad2.cd()
	ratio.Draw("pe")
	
	line = ROOT.TLine(0,1,limit[k],1)
	line.SetLineColor(632)
	line.Draw("same")

	canvas.Print(plotFileName)
canvas.Print(plotFileName+"]")
