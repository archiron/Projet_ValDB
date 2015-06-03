#! /usr/bin/env python
#-*-coding: utf-8 -*-

#from PyQt import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os,sys
import ovalGui

from getEnv import env
from fonctions import liste
		
def main(args):
    a=QApplication(args)
    # Création d'un widget qui servira de fenêtre
    fenetre=ovalGui.ovalGui()
    fenetre.move(100, 500)
    fenetre.show()
    r=a.exec_()
    return r

if __name__=="__main__":
    main(sys.argv)