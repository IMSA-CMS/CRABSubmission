from CRABClient.UserUtilities import config, getUsernameFromCRIC

config = config()

config.General.requestName = "DIGIPM_Hplusplus_M800_13TeV_test4"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab.py"
config.JobType.maxMemoryMB = 4000
#config.JobType.numCores = 8

config.Data.inputDataset = "/GEN_Hpp_NEW_test/ardas-RunIISummer20UL18_SIM-128efeffab8ceb577467d0e58be013b1/USER" 
config.Data.outLFNDirBase = "/store/user/%s/" % (getUsernameFromCRIC())
config.Data.outputDatasetTag = "RunIISummer20UL18_DIGIPremix"
config.Data.inputDBS = "phys03"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.ignoreLocality = True

config.Site.storageSite = "T3_US_FNALLPC"
config.Site.whitelist = ["T2_*","T3_*"]
