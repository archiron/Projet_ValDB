#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys

class env:
    def __init__(self): #, CMSSWBASE, CMSSWRELEASEBASE, CMSSWVERSION):
        self.CMSSWBASE = os.environ['CMSSW_BASE']
        self.CMSSWBASECMSSWRELEASEBASE = os.environ['CMSSW_RELEASE_BASE']
        self.CMSSWBASECMSSWVERSION = os.environ['CMSSW_VERSION']
        #self.OvalEnvName = os.environ['OVAL_ENVNAME']
        self.EOSCHEMIN = "/afs/cern.ch/cms/Physics/egamma/www/validation/Electrons/"

    def getCMMSWBASE(self):
        return self.CMSSWBASE
		
    def getCMSSWBASECMSSWRELEASEBASE(self):
        return self.CMSSWBASECMSSWRELEASEBASE
		
    def getCMSSWBASECMSSWVERSION(self):
        return self.CMSSWBASECMSSWVERSION
		
    #def getOvalEnvName(self):
    #    return self.OvalEnvName
		
    def getEOSCHEMIN(self):
        return self.EOSCHEMIN
		
    def cmsAll(self):
        cmsAll="<strong>CMSSW_BASE</strong> : " + self.getCMMSWBASE()
        cmsAll+="<br /><strong>CMSSW_RELEASE_BASE</strong> : " + self.getCMSSWBASECMSSWRELEASEBASE()
        cmsAll+="<br /><strong>CMSSW_VERSION</strong> : " + self.getCMSSWBASECMSSWVERSION()
        return cmsAll

    def eosText(self):
        eosText="/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select"
        eosText+=' ls /eos/cms/store/relval/' + self.getCMSSWBASECMSSWVERSION()
        return eosText
				
    def listeElectronsDirs2(self):
        print "***", self.getEOSCHEMIN() # -> OK !
#        dirs = os.listdir('.')
        dirs = os.listdir(self.getEOSCHEMIN())
        # This would print all the files and directories
#        for file in dirs:
#            print file
        return dirs