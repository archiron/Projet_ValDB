#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

import os,sys

from getEnv import env
from fonctions import liste
		
class ovalGui(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('ValDB Gui v0.2')
        self.move(100, 100)

        self.cmsenv = env()
        self.texte = self.cmsenv.cmsAll()
        
		# creation du label
        self.label = QLabel(self.trUtf8(self.texte), self)
        self.label.move(10, 20)
        
        # creation du TextEdit principal
        self.texte1 = QTextEdit()
        self.connect(self.texte1, SIGNAL("textChanged()"), self.on_text_changed)
	
        # creation du TextEdit secondaire
        self.texte2 = QTextEdit()

        # creation du TextEdit liens
        self.texte3 = QTextEdit()

        #Layout intermédiaire : boutons
        self.layoutH_textes = QHBoxLayout()
        self.layoutH_textes.addWidget(self.texte2)
        self.layoutH_textes.addWidget(self.texte3)

        # Création du bouton quitter, ayant pour parent la "fenetre"
        boutonQ=QPushButton(self.trUtf8("Quit ?"),self)
        # Customisation du bouton
        boutonQ.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        boutonQ.setIcon(QIcon("../images/smile.png"))
        boutonQ.setGeometry(400, 110, 90, 30)
        #Connexion du clic du bouton à la fermeture de l'appli
        self.connect(boutonQ, SIGNAL("clicked()"), qApp, SLOT("quit()"))

        # Création du bouton Clear All, ayant pour parent la "fenetre"
        self.bouton1=QPushButton(self.trUtf8("Clear All"),self)
        # Customisation du bouton
        self.bouton1.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        self.bouton1.setIcon(QIcon("../images/smile.png"))
        self.bouton1.setGeometry(250, 110, 90, 30)
        #Connexion du clic du bouton à la cmsenv
        self.connect(self.bouton1, SIGNAL("clicked()"), self.liste1)
        
        # Création du bouton Extract, ayant pour parent la "fenetre"
        self.bouton2=QPushButton(self.trUtf8("Extract"),self)
        # Customisation du bouton
        self.bouton2.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        self.bouton2.setIcon(QIcon("../images/smile.png"))
        self.bouton2.setGeometry(250, 110, 90, 30)
        self.bouton2.setStyleSheet("background-color: None") # default
        #Connexion du clic du bouton à la cmsenv
        self.connect(self.bouton2, SIGNAL("clicked()"), self.liste2)

        #Layout intermédiaire : boutons
        self.layoutH_boutons = QHBoxLayout()
        self.layoutH_boutons.addWidget(self.bouton2)
        self.layoutH_boutons.addStretch(1)
        self.layoutH_boutons.addWidget(self.bouton1)
        self.layoutH_boutons.addWidget(boutonQ)
        
        #Layout principal : création et peuplement
        self.layout_general = QVBoxLayout()
        self.layout_general.addWidget(self.texte1)
        self.layout_general.addWidget(self.label)
        self.layout_general.addLayout(self.layoutH_boutons)
        self.layout_general.addLayout(self.layoutH_textes)
        self.setLayout(self.layout_general)
	
    def liste1(self):
        self.texte1.clear()
        self.texte2.clear()
        self.texte3.clear()
        #

    def liste2(self):
        #
        toto = self.texte1.toPlainText()
        print toto
        self.texte2.append(toto)
        self.texte3.append(toto)
        self.bouton2.setStyleSheet("background-color: None") # default

    def on_text_changed(self):
        print "text changed"
        self.bouton2.setStyleSheet("background-color: red; color: white") 
