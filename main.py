#! /usr/bin/env python
#-*-coding: utf-8 -*-

#from PyQt import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os,sys
import ovalGui

def main(args):
    a=QApplication(args)
    # Création d'un widget qui servira de fenêtre
    fenetre=ovalGui.ovalGui()
    fenetre.resize(1000, 600)
    fenetre.show()
    r=a.exec_()
    return r

if __name__=="__main__":
    main(sys.argv)