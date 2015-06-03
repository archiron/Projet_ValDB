#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys

from getEnv import env

def liste(self):
    os.system('ls -alt')

def cmd_eos(self):
    name = "RelValTTbar_13"
    os.system(self.cmsenv.eosText() + '/' + name + '/GEN-SIM-RECO')

