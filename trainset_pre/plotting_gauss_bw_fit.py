#This is a tutorial code that instructs you how to plot data in CERN Style
import ROOT
import sys
if len(sys.argv)!= 3:
	print("USAGE:%s<input file><output file>"%(sys.argv[0]))
	sys.exit(1)
histFileName = sys.argv[1]
plotFileName = sys.argv[2]
print("Reading from <",histFileName,"> and writing to <",plotFileName,">")
histFile = ROOT.TFile.Open(histFileName,"READ")
dataHist = histFile.Get("data")
if not dataHist:
	print("Failed to get data histogram")
	sys.exit(1)
dataHist.SetDirectory(0)
histFile.Close()

canvas = ROOT.TCanvas("canvas")
canvas.cd()
canvas.SetLogy(True)
canvas.Print(plotFileName+"[")
# plot1 raw
dataHist.SetStats(0)
dataHist.SetLineColor(ROOT.kBlack)
dataHist.SetLineWidth(2)
dataHist.GetYaxis().SetTitle("Number of events")
dataHist.GetXaxis().SetTitle("m_{ll}[MeV]")
dataHist.Draw("pe")
canvas.Print(plotFileName)
# plot2 gauss fit
gaussFit = ROOT.TF1("gaussfit","gaus",80.e3,100.e3)
dataHist.Fit(gaussFit,"E")
latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

chi2 = gaussFit.GetChisquare()
ndof = gaussFit.GetNDF()
mean = gaussFit.GetParameter(1)/1000
width = gaussFit.GetParameter(0)/1000

dataHist.Draw("pe")
legend = ROOT.TLegend(0.7,0.5,0.85,0.65)
legend.AddEntry(dataHist,"Data")
legend.AddEntry(gaussFit,"Gaussian Fit")
legend.SetLineWidth(0)
legend.Draw("same")
latex.DrawText(0.6,0.8,"Mean = %.1f GeV"%(mean))
latex.DrawText(0.6,0.75,"Width = %.1f GeV"%(width))
latex.DrawText(0.6,0.7,"chi2/ndof = %.1f/%d = %.1f"%(chi2,ndof,chi2/ndof))
canvas.Print(plotFileName)

#plot 3 Breit-Wigner
#def
bw_A = "2*sqrt(2)*[0]*[1]*sqrt([0]**2*([0]**2+[1]**2))" 
bw_B = "3.1415926*sqrt([0]**2+sqrt([0]**2*([0]**2+[1]**2)))"
bw_C = "(x**2-[0]**2)**2 + [0]**2*[1]**2"
bw = "[2]*((%s)/(%s))/(%s)"%(bw_A,bw_B,bw_C)
bwFit = ROOT.TF1("bwfit",bw,50.e3,200.e3)
bwFit.SetParameter(0,100.e3)
bwFit.SetParameter(1,1.e3)

dataHist.Fit(bwFit,"E")
dataHist.Draw("pe")
chi2 = bwFit.GetChisquare()
ndof = bwFit.GetNDF()
mean = bwFit.GetParameter(0)/1000
width = bwFit.GetParameter(1)/1000

ratio = dataHist.Clone()
ratio.Divide(bwFit)
ratio.SetLineColor(ROOT.kRed)
ratio.SetTitle("")
ratio.GetXaxis().SetLabelSize(0.12)
ratio.GetXaxis().SetTitleSize(0.12)
ratio.GetYaxis().SetLabelSize(0.1)
ratio.GetYaxis().SetTitleSize(0.15)
ratio.GetYaxis().SetTitle("Data/Fit")
ratio.GetYaxis().SetTitleOffset(0.3)
ratio.GetYaxis().SetRangeUser(0.5,1.5)
ratio.GetYaxis().SetNdivisions(207)

canvas.Clear()
dataHist.SetTitle("")
dataHist.GetXaxis().SetLabelSize(0)
dataHist.GetXaxis().SetTitleSize(0)
dataHist.GetYaxis().SetTitleSize(0.05)
pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
pad1.SetLogy(True)
pad1.SetBottomMargin(0)
pad1.Draw()
pad1.cd()
dataHist.Draw("pe,same")

legend = ROOT.TLegend(0.65,0.45,0.85,0.6)
legend.AddEntry(dataHist,"Data")
legend.AddEntry(bwFit,"Breit-Wigner Fit")
legend.SetLineWidth(0)
legend.Draw("same")


latex.DrawText(0.65,0.75,"Mean = %.1f GeV"%(mean))
latex.DrawText(0.65,0.7,"Width = %.1f GeV"%(width))
latex.DrawText(0.65,0.65,"chi2/ndof = %.1f/%d = %.1f"%(chi2,ndof,chi2/ndof))

latex.SetTextSize(0.06)
latex.DrawText(0.65,0.85,"Mini 2022")
latex.SetTextSize(0.04)
latex.DrawText(0.65,0.8,"Di-Muon events")

canvas.cd()
pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.25)
pad2.Draw()
pad2.cd()
ratio.Draw("pe")

line = ROOT.TLine(50.e3,1,200.e3,1)
line.SetLineColor(ROOT.kBlack)
line.SetLineWidth(2)
line.Draw("same")
canvas.Print(plotFileName)

canvas.Print(plotFileName+"]")
