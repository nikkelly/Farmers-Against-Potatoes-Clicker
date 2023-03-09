import pyautogui
import cv2
import time

LOCATECOUNT = 0
STARTFIND = 0 
GAME_STARTED = False
POTATO_COUNT = 0

def clickStart():
    global STARTFIND
    global GAME_STARTED

    startButton = pyautogui.locateOnScreen('images/960x540/start.png',confidence=0.8)

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

    goodPotato_1 = pyautogui.locateOnScreen('images/960x540/goodPotato_1.png',confidence=0.55)
    if goodPotato_1 != None:
        pyautogui.moveTo(goodPotato_1)
        pyautogui.click()
        print("Potato Found!")
        POTATO_COUNT += 1


    goodPotato_2 = pyautogui.locateOnScreen('images/960x540/goodPotato_2.png',confidence=0.55)
    if goodPotato_2 != None:
        pyautogui.moveTo(goodPotato_2)
        pyautogui.click()
        print("Potato Found!")
        POTATO_COUNT += 1
    
    timetocount = pyautogui.locateOnScreen('images/960x540/timetocount.png',confidence=0.9)
    if timetocount != None:
        print("Times up!")
        LOCATECOUNT = 1


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("Start Button Missing!")

while True:
    try:
        if GAME_STARTED == True:
            # t_end = time.time() + 63
            locateGoodPotato()
        if GAME_STARTED == False:
            print('Trying to start')
            clickStart()
            LOCATECOUNT = 0
        if LOCATECOUNT == 1 and GAME_STARTED == True:
            print("Game Finished - Potato Count: "+ str(POTATO_COUNT))
            GAME_STARTED = False
            LOCATECOUNT = 0
            print('Sleeping for 5 mintues')
            # time.sleep(60*5) # sleep for 5 minutes
            countdown(60*5)
    except:
        # time.sleep(10)
        print("GameStarted = "+str(GAME_STARTED))
        countdown(10)
