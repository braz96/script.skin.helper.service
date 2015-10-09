#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import time
import _strptime
from resources.lib.Utils import *
from resources.lib.BackgroundsUpdater import BackgroundsUpdater
from resources.lib.ListItemMonitor import ListItemMonitor
from resources.lib.KodiMonitor import Kodi_Monitor

class Main:
    
    def __init__(self):
        
        KodiMonitor = Kodi_Monitor()
        listItemMonitor = ListItemMonitor()
        backgroundsUpdater = BackgroundsUpdater()
        lastSkin = None
                   
        #start the extra threads
        listItemMonitor.start()
        backgroundsUpdater.start()
        
        while not KodiMonitor.abortRequested():
            
            #set skin info
            if lastSkin != xbmc.getSkinDir():
                setSkinVersion()
            
            KodiMonitor.waitForAbort(5000)
        else:
            # Abort was requested while waiting. We should exit
            xbmc.log('SKIN HELPER SERVICE --> shutdown requested !')
            #stop the extra threads
            backgroundsUpdater.stop()
            listItemMonitor.stop()                             

xbmc.log('skin helper service version %s started' % ADDON_VERSION)
Main()
xbmc.log('skin helper service version %s stopped' % ADDON_VERSION)

