#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

import os, sys, re

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
#        self.label.move(10, 20)
        
		# creation du compteur principal
        self.compteur_p = QLabel(self.trUtf8("0"), self)
        
		# creation du compteur secondaire
        self.compteur_s = QLabel(self.trUtf8("0"), self)       
		# creation du compteur liens
        self.compteur_l = QLabel(self.trUtf8("0"), self)
        #Layout intermédiaire : boutons
        self.layoutH_compteurs = QHBoxLayout()
        self.layoutH_compteurs.addWidget(self.compteur_s)
        self.layoutH_compteurs.addStretch(1)
        self.layoutH_compteurs.addWidget(self.compteur_l)
        
        # creation du TextEdit principal
        self.texte1 = QTextEdit()
        self.connect(self.texte1, SIGNAL("textChanged()"), self.on_text_changed)
	
        # creation du TextEdit secondaire
        self.texte_s = QTextEdit()
        # creation du TextEdit liens
        self.texte_l = QTextEdit()

        #Layout intermédiaire : boutons
        self.layoutH_textes = QHBoxLayout()
        self.layoutH_textes.addWidget(self.texte_s)
        self.layoutH_textes.addWidget(self.texte_l)

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
        self.connect(self.bouton1, SIGNAL("clicked()"), self.clearAll)
        
        # Création du bouton Extract, ayant pour parent la "fenetre"
        self.bouton2=QPushButton(self.trUtf8("Extract"),self)
        # Customisation du bouton
        self.bouton2.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        self.bouton2.setIcon(QIcon("../images/smile.png"))
        self.bouton2.setGeometry(250, 110, 90, 30)
        self.bouton2.setStyleSheet("background-color: None") # default
        #Connexion du clic du bouton à la cmsenv
        self.connect(self.bouton2, SIGNAL("clicked()"), self.extract)

        #Layout intermédiaire : boutons
        self.layoutH_boutons = QHBoxLayout()
        self.layoutH_boutons.addWidget(self.bouton2)
        self.layoutH_boutons.addStretch(1)
        self.layoutH_boutons.addWidget(self.bouton1)
        self.layoutH_boutons.addWidget(boutonQ)
        
        #Layout principal : création et peuplement
        self.layout_general = QVBoxLayout()
        self.layout_general.addWidget(self.texte1)
        self.layout_general.addWidget(self.compteur_p)
        self.layout_general.addWidget(self.label)
        self.layout_general.addLayout(self.layoutH_boutons)
        self.layout_general.addLayout(self.layoutH_textes)
        self.layout_general.addLayout(self.layoutH_compteurs)
        self.setLayout(self.layout_general)
	
    def clearAll(self):
        self.texte1.clear()
        self.texte_s.clear()
        self.texte_l.clear()
        t_s = str(len(self.texte_s.toPlainText()))
        t_l = str(len(self.texte_l.toPlainText()))
        self.compteur_s.setText(self.trUtf8(t_s))
        self.compteur_l.setText(self.trUtf8(t_l))
        self.bouton2.setStyleSheet("background-color: None") # default
        self.compteur_s.setStyleSheet("background-color: None")
        self.compteur_l.setStyleSheet("background-color: None")

    def extract(self):
        self.texte_s.clear()
        self.texte_l.clear()
        texte_p = self.texte1.toPlainText()
        print texte_p
        self.texte_s.append(texte_p)
        self.texte_l.append(texte_p)
        self.bouton2.setStyleSheet("background-color: None") # default
        inter = texte_p.split(' ')
        i = 0
        list_s = ''
        list_l = ''

        tmp = re.findall(r'(https?://\S+)', str(texte_p))
        list_s = texte_p
        i = 0
        for item in tmp:
            print item
            list_s.replace(item, '[' + str(i) + ']')
            list_l += '[' + str(i) + '] ' + item + '\r\r'
            i += 1
        
        self.texte_s.setText(self.trUtf8(list_s))
        self.texte_l.setText(self.trUtf8(list_l))
        t_s = str(len(self.texte_s.toPlainText()))
        t_l = str(len(self.texte_l.toPlainText()))
        self.compteur_s.setText(self.trUtf8(t_s))
        self.compteur_l.setText(self.trUtf8(t_l))
        len_s = len(self.texte_s.toPlainText())
        len_l = len(self.texte_l.toPlainText())
        if len_s > 20:
            self.compteur_s.setStyleSheet("background-color: red; color: white")
        else:
            self.compteur_s.setStyleSheet("background-color: None")
        if len_l > 20:
            self.compteur_l.setStyleSheet("background-color: red; color: white")
        else:
            self.compteur_l.setStyleSheet("background-color: None")

    def on_text_changed(self):
#        print "text changed"
        self.bouton2.setStyleSheet("background-color: red; color: white") 
        symbols = str(len(self.texte1.toPlainText()))
        self.compteur_p.setText(self.trUtf8(symbols))
        
