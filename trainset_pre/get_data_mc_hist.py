
import ROOT
import sys

if len(sys.argv)!= 4:
	print("Usage:%s <input file><output file>"%(sys.argv[0]))
	sys.exit(1)
inFileNameData = sys.argv[1]
inFileNameMC = sys.argv[2]
outFileName = sys.argv[3]
print("reading from",inFileNameData,"and",inFileNameMC,"then writing to",outFileName)

def produceHist(inFileName):
	inFile = ROOT.TFile.Open(inFileName,"READ")
	
	fNameLower = inFileName.lower()
	isMC = True
	if 'data' in fNameLower: isMC = False
	
	tree = inFile.Get("mini")#("HASCO")
	if isMC:mll = ROOT.TH1D("mc","m_{ll},"+ inFileName,150,50.e3,200.e3)
	else:   mll = ROOT.TH1D("data","m_{ll},"+ inFileName,150,50.e3,200.e3)
	mll.Sumw2()

	for entryNum in range(0,tree.GetEntries()):
		tree.GetEntry(entryNum)
		if entryNum%1000 == 0: print(entryNum, end = "\r")
		if getattr(tree,"lep_n")!= 2:
			continue
		weight = 1.0
		if isMC:
			weight *= getattr(tree,"mcWeight")
			weight *= getattr(tree,"scaleFactor_PILEUP")
			weight *= getattr(tree,"scaleFactor_MUON")
			weight *= getattr(tree,"scaleFactor_TRIGGER")
		lepton0 = ROOT.TLorentzVector()
		lepton1 = ROOT.TLorentzVector()
		pt = getattr(tree,"lep_pt")
		eta = getattr(tree,"lep_eta")
		phi = getattr(tree,"lep_phi")
		nrg = getattr(tree,"lep_E")
		lepton0.SetPtEtaPhiE(pt[0],eta[0],phi[0],nrg[0])
		lepton1.SetPtEtaPhiE(pt[1],eta[1],phi[1],nrg[1])
		dilepton = lepton0+lepton1
		dileptonMass = dilepton.M()
		print(type(dileptonMass))
		mll.Fill(dileptonMass,weight)
	mll.SetDirectory(0)
	inFile.Close()
	return mll

mllData = produceHist(inFileNameData)
mllMC = produceHist(inFileNameMC)

outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
outHistFile.cd()
mllData.Write()
mllMC.Write()
outHistFile.Close()
