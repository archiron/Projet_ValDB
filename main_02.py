#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os,sys

from getEnv import env
from fonctions import liste
		
cmsenv = env()
texte = "<strong>CMSSW_BASE</strong> : " + cmsenv.getCMMSWBASE() + "<br /><strong>CMSSW_RELEASE_BASE</strong> : " + cmsenv.getCMSSWBASECMSSWRELEASEBASE() + "<br /><strong>CMSSW_VERSION</strong> : " + cmsenv.getCMSSWBASECMSSWVERSION()

def main(args):
    a=QApplication(args)
    # Création d'un widget qui servira de fenêtre
    fenetre=QWidget()
    fenetre.setFixedSize(500, 150)
    fenetre.setWindowTitle('OvalGui v0.1')
	
    # creation du label
    label=QLabel(a.trUtf8(texte), fenetre)
    label.move(10, 20)
	
    # Création du bouton quitter, ayant pour parent la "fenetre"
    boutonQ=QPushButton(a.trUtf8("Quitter ?"),fenetre)
    # Customisation du bouton
    boutonQ.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
    #boutonQ.setCursor(QtCore.Qt.ForbiddenCursor)
    boutonQ.setIcon(QIcon("../images/smile.png"))
    boutonQ.setGeometry(400, 110, 90, 30)

    #Connexion du clic du bouton à la fermeture de l'appli
    fenetre.connect(boutonQ, SIGNAL("clicked()"), qApp, SLOT("quit()"))

    # Création du bouton cmsenv, ayant pour parent la "fenetre"
    bouton2=QPushButton(a.trUtf8("cmsenv ?"),fenetre)
    # Customisation du bouton
    bouton2.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
    #bouton2.setCursor(QtCore.Qt.ForbiddenCursor)
    bouton2.setIcon(QIcon("../images/smile.png"))
    bouton2.setGeometry(250, 110, 90, 30)

    #Connexion du clic du bouton à la fermeture de l'appli
    fenetre.connect(bouton2, SIGNAL("clicked()"), fenetre, SLOT("fonctions.liste()")) #SLOT("print os.system('ls')"))
    #print liste()
	
    fenetre.move(100, 500)
    fenetre.show()
    r=a.exec_()
    return r

if __name__=="__main__":
    main(sys.argv)