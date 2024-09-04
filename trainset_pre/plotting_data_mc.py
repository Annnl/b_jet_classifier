import ROOT
import sys
if len(sys.argv)!= 3:
	print("USAGE: %s<input file><output file>"%(sys.argv[0]))
	sys.exit(1)
histFileName = sys.argv[1]
plotFileName = sys.argv[2]
print("Reading from",histFileName,"then writing to",plotFileName)

histFile = ROOT.TFile.Open(histFileName,"READ")
dataHist = histFile.Get("mass_lep_close_top")
mcHist   = histFile.Get("mass_lep_close")
if not dataHist:
	print("Failed to get data histogram")
	sys.exit(1)
if not mcHist:
	print("Failed to get mc histogram")
	sys.exit(1)
dataHist.SetDirectory(0)
mcHist.SetDirectory(0)
histFile.Close()

canvas = ROOT.TCanvas("canvas")
canvas.cd()
canvas.Print(plotFileName+"[")

mcHist.SetStats(0)
dataHist.SetStats(0)

mcHist.SetLineColor(ROOT.kRed)
mcHist.SetLineWidth(2)
dataHist.SetLineColor(ROOT.kBlack)
dataHist.SetLineWidth(2)

mcHist.GetYaxis().SetTitle("Number of events")
dataHist.GetYaxis().SetTitle("Number of events")
mcHist.GetXaxis().SetTitle("m_{ll}[MeV]")
dataHist.GetXaxis().SetTitle("m_{ll}[MeV]")
canvas.SetLogy(True)
mcHist.Scale(dataHist.Integral()/mcHist.Integral())

ratio = dataHist.Clone()
ratio.Divide(mcHist)
ratio.SetLineColor(ROOT.kRed)

mcHist.Draw("h")
dataHist.Draw("pe,same")
canvas.Print(plotFileName)

mcHist.Draw("h")
canvas.Print(plotFileName)
dataHist.Draw("pe")
canvas.Print(plotFileName)
#Plot 4
canvas.Clear()
mcHist.SetTitle("m_{ll} two pads plot")
mcHist.GetXaxis().SetLabelSize(0)
mcHist.GetXaxis().SetTitleSize(0)
mcHist.GetYaxis().SetTitleSize(0.05)
ratio.SetTitle("")
ratio.GetXaxis().SetLabelSize(0.12)
ratio.GetXaxis().SetTitleSize(0.12)
ratio.GetYaxis().SetLabelSize(0.1)
ratio.GetYaxis().SetTitleSize(0.15)
ratio.GetYaxis().SetTitle("Data/MC")
ratio.GetYaxis().SetTitleOffset(0.3)
pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
pad1.SetLogy(True)
pad1.SetBottomMargin(0)
pad1.Draw()
pad1.cd()
mcHist.Draw("h")
dataHist.Draw("pe,same")

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.AddEntry(mcHist,"MC")
legend.AddEntry(dataHist,"Data")
legend.SetLineWidth(0)
legend.Draw("same")

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.06)
latex.DrawText(0.7,0.83,"Mini 2022")
latex.SetTextSize(0.04)
latex.DrawText(0.7,0.77,"Di-muon events")

canvas.cd()
pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.25)
pad2.Draw()
pad2.cd()

ratio.GetYaxis().SetRangeUser(0.5,1.5)
ratio.GetYaxis().SetNdivisions(207)
ratio.Draw("pe")

line = ROOT.TLine(50.e3,1,200.e3,1)
line.SetLineColor(ROOT.kBlack)
line.SetLineWidth(2)
line.Draw("same")

canvas.Print(plotFileName)

canvas.Print(plotFileName+"]")

