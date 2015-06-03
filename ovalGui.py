#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

import os,sys

from getEnv import env
from fonctions import liste, cmd_eos #, listeElectronsDirs
		
class ovalGui(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # self.setFixedSize(500, 150)
        self.setWindowTitle('CorrectionGui v0.1')
        self.move(100, 500)

        self.cmsenv = env()
        #listeElectronsDirs(self)
        self.texte = self.cmsenv.cmsAll()
        
        for file in self.cmsenv.listeElectronsDirs2():
            print file
            self.texte += "<br /><strong>BLOP</strong> : " + file # 
		
		# creation du label
        self.label=QLabel(self.trUtf8(self.texte), self)
        self.label.move(10, 20)
	
        # Création du bouton quitter, ayant pour parent la "fenetre"
        boutonQ=QPushButton(self.trUtf8("Quitter ?"),self)
        # Customisation du bouton
        boutonQ.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        #boutonQ.setCursor(QtCore.Qt.ForbiddenCursor)
        boutonQ.setIcon(QIcon("../images/smile.png"))
        boutonQ.setGeometry(400, 110, 90, 30)

        #Connexion du clic du bouton à la fermeture de l'appli
        self.connect(boutonQ, SIGNAL("clicked()"), qApp, SLOT("quit()"))

        # Création du bouton cmsenv, ayant pour parent la "fenetre"
        self.bouton2=QPushButton(self.trUtf8("cmsenv ?"),self)
        # Customisation du bouton
        self.bouton2.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        #self.bouton2.setCursor(QtCore.Qt.ForbiddenCursor)
        self.bouton2.setIcon(QIcon("../images/smile.png"))
        self.bouton2.setGeometry(250, 110, 90, 30)

        #Connexion du clic du bouton à la cmsenv
        self.connect(self.bouton2, SIGNAL("clicked()"), self.liste2)
        #print liste(self)
	
    def liste2(self):
        #instruction = "alias cmsenv='eval `/afs/cern.ch/cms/common/scramv1 runtime -sh`'"
        #os.system(instruction)
        #exec(instruction)
        #liste(self)
        cmd_eos(self)
        #cmd_chemin(self)
