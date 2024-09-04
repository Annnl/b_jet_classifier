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
label = ["number of jets","number of b-jets","Leading PT of jets [GeV]",
"Leading PT of b-jets [GeV]","PT of electron [GeV]","PT of muon [GeV]"]
limit = [7,7,1000,1000,1000,1000]
canvas = ROOT.TCanvas("canvas")
canvas.cd()
canvas.Print(plotFileName+"[")
for k in range(6):
	histFile = ROOT.TFile.Open(histFileName,"READ")	
	mc = []	
	if k == 0:
		mc.append(histFile.Get("numjet_Z"))
		mc.append(histFile.Get("numjet_other"))
		mc.append(histFile.Get("numjet_diboson"))
		mc.append(histFile.Get("numjet_H"))
		mc.append(histFile.Get("numjet_V"))
		mc.append(histFile.Get("numjet_single_top"))	
		mc.append(histFile.Get("numjet_ttbar"))
		data = histFile.Get("numjet_data")
	if k == 1:
		mc.append(histFile.Get("numbjet_Z"))
		mc.append(histFile.Get("numbjet_other"))
		mc.append(histFile.Get("numbjet_diboson"))
		mc.append(histFile.Get("numbjet_H"))
		mc.append(histFile.Get("numbjet_V"))
		mc.append(histFile.Get("numbjet_single_top"))	
		mc.append(histFile.Get("numbjet_ttbar"))
		data = histFile.Get("numbjet_data")
	if k == 2:
		mc.append(histFile.Get("leading_jet_PT_Z"))
		mc.append(histFile.Get("leading_jet_PT_other"))
		mc.append(histFile.Get("leading_jet_PT_diboson"))
		mc.append(histFile.Get("leading_jet_PT_H"))
		mc.append(histFile.Get("leading_jet_PT_V"))
		mc.append(histFile.Get("leading_jet_PT_single_top"))
		mc.append(histFile.Get("leading_jet_PT_ttbar"))
		data = histFile.Get("leading_jet_data")	
	if k == 3:
		mc.append(histFile.Get("leading_bjet_PT_Z"))
		mc.append(histFile.Get("leading_bjet_PT_other"))
		mc.append(histFile.Get("leading_bjet_PT_diboson"))
		mc.append(histFile.Get("leading_bjet_PT_H"))
		mc.append(histFile.Get("leading_bjet_PT_V"))
		mc.append(histFile.Get("leading_bjet_PT_single_top"))
		mc.append(histFile.Get("leading_bjet_PT_ttbar"))
		data = histFile.Get("leading_bjet_data")
	if k == 4:
		mc.append(histFile.Get("elpt_Z"))
		mc.append(histFile.Get("elpt_other"))
		mc.append(histFile.Get("elpt_diboson"))
		mc.append(histFile.Get("elpt_H"))
		mc.append(histFile.Get("elpt_V"))
		mc.append(histFile.Get("elpt_top"))	
		mc.append(histFile.Get("elpt_ttbar"))
		data = histFile.Get("elpt_data")
	if k == 5:
		mc.append(histFile.Get("mupt_Z"))
		mc.append(histFile.Get("mupt_other"))
		mc.append(histFile.Get("mupt_diboson"))
		mc.append(histFile.Get("mupt_H"))
		mc.append(histFile.Get("mupt_V"))
		mc.append(histFile.Get("mupt_top"))	
		mc.append(histFile.Get("mupt_ttbar"))
		data = histFile.Get("mupt_data")
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
	ratio.GetXaxis().SetTitle(label[k])
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

	legend = ROOT.TLegend(0.6,0.5,0.85,0.8)
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
	
	line = ROOT.TLine(2,1,limit[k],1)
	line.SetLineColor(632)
	line.Draw("same")

	canvas.Print(plotFileName)
canvas.Print(plotFileName+"]")
