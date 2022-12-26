
#TODO Add red potato tracking to ignore
#TODO Why does it exit after a few instead of sleeping?

import pyautogui
import time

LOCATECOUNT = 0
STARTFIND = 0 
GAME_STARTED = False
POTATO_COUNT = 0

def clickWhack():
    whackButton = pyautogui.locateOnScreen('images/960x540/whackAPotato.png')
    if whackButton != None:
        print('Move to Whack-A-Potato')
        pyautogui.moveTo(whackButton)        
        pyautogui.click()
        print(' Clicked Whack-A-Potato')
        time.sleep(2)

def clickStart():
    global STARTFIND
    global GAME_STARTED

    startButton = pyautogui.locateOnScreen('images/960x540/start.png',confidence=0.9)

    if STARTFIND > 3:
        raise ValueError("Can't see start button")

    if startButton != None:
        print('Starting Game')
        pyautogui.moveTo(startButton)
        pyautogui.click()
        print("Waiting for game to start")
        time.sleep(3)
        GAME_STARTED = True

    else:
        STARTFIND += 1
        clickWhack()

def locateGoodPotato():
    global LOCATECOUNT
    global POTATO_COUNT

    goodPotato_1 = pyautogui.locateOnScreen('images/960x540/goodPotato_1.png',confidence=0.7)
    if goodPotato_1 != None:
        pyautogui.moveTo(goodPotato_1)
        pyautogui.click()
        print("Potato Found!")
        POTATO_COUNT += 1

    if (goodPotato_1 == None):
        LOCATECOUNT += 1
    else: 
        LOCATECOUNT = 0

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

# clickStart() # start game

# t_end = time.time() + 70
# while time.time() < t_end: # run for 60 seconds
#     if GAME_STARTED == False:
#         clickStart() # start game

#     locateGoodPotato()
#     if LOCATECOUNT > 0:
#         print("     ")
#     if LOCATECOUNT == 10 and time.time() > t_end:
#         print("Game Finished - Potato Count: " + str(POTATO_COUNT))
#         print("Can't find potato - sleeping for 5 minutes")
#         time.sleep(60*5) # sleep for 5 minutes 

#         # reset variables
#         t_end = time.time() + 60
#         LOCATECOUNT = 0
#         STARTFIND = 0 
#         GAME_STARTED = False
#         POTATO_COUNT = 0

while True:
    try:
        if GAME_STARTED == True:
            t_end = time.time() + 63
            locateGoodPotato()
        else:
            clickStart()
        if LOCATECOUNT == 10:
            print("Game Finished - Potato Count: "+ str(POTATO_COUNT))
            GAME_STARTED = False
            LOCATECOUNT = 0
            print('Sleeping for 5 mintues')
            # time.sleep(60*5) # sleep for 5 minutes
            countdown(60*5)
    except:
        # time.sleep(10)
        countdown(10)
