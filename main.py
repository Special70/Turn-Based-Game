import random
import threading
import time
import msvcrt
import os

# External .py Files
import system_lib as syslib
import locale_EN as lang
import func_lib as func

# ------------------------------------- Intro Msg
lang.mainMenu_startMsg_0()
#time.sleep(1)
os.system('cls')
syslib.disableKeyListener = False
   

def mainThread():
    while syslib.programStatus:
        # Main Menu
        match(syslib.currentMenu):
            case 1:
                lang.mainMenu_startMsg_1()
                func.mainMenuSystem()
                os.system('cls')
            case 2:
                # Main Game Menu
                lang.gameSelector()
                func.gameSelectorMenu()
                os.system('cls')
        
        
            
            
    # For debugging purposes
    print("[!] mainThread thread finished [!]")

def keyListener(): # This function is only good at making inputs work. NOT at setting up keybinds or some sort. If you're gonna add some custom things that records keypresses, don't use syslib.currentKey .
    while syslib.programStatus:
        if msvcrt.kbhit() and syslib.disableKeyListener == False:
            syslib.currentKey = str(msvcrt.getch()).split("'")[1].upper()
            print(syslib.currentKey)
            #time.sleep(0.1) # Just to make sure it's not deleting SUPER FAST. Comment or increase when problems arise
            syslib.currentKey = ""
            
                
    

thread1 = threading.Thread(target=mainThread)
thread2 = threading.Thread(target=keyListener)

thread1.start()
thread2.start()

thread1.join()