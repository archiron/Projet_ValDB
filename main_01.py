#!/usr/bin/python
#-*-coding: utf-8 -*-

import sys
import os

try:
    from PyQt4 import QtGui, QtCore 
except Exception,e:
    raise ImportError("pbm avec Qt4 "+str(e))
from PyQt4.QtGui import *

def main(args):
    a=QApplication(args)
    bouton=QPushButton(a.trUtf8("Salut les Zéros, la forme ?"),None)
    bouton.show()

    r=a.exec_()
    return r
if __name__=="__main_01__":
    main(sys.argv)
