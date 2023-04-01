import pyautogui
import time

class FarmersAgainstPotatoes:
    def __init__(self):
        self.locate_count = 0
        self.start_find = 0
        self.game_started = False
        self.potato_count = 0

    def click_start(self):
        """Click the start button to initiate the game."""
        start_button = pyautogui.locateOnScreen('images/960x540/start.png', confidence=0.8)

        if start_button is not None:
            print('Starting Game')
            pyautogui.moveTo(start_button)
            pyautogui.click()
            print("Waiting for game to start")
            time.sleep(3)
            self.game_started = True
        else:
            self.start_find += 1

    def locate_good_potato(self):
        """Locate and click good potatoes."""
        good_potato_1 = pyautogui.locateOnScreen('images/960x540/goodPotato_1.png', confidence=0.55)
        if good_potato_1 is not None:
            pyautogui.moveTo(good_potato_1)
            pyautogui.click()
            print("Potato Found!")
            self.potato_count += 1

        good_potato_2 = pyautogui.locateOnScreen('images/960x540/goodPotato_2.png', confidence=0.55)
        if good_potato_2 is not None:
            pyautogui.moveTo(good_potato_2)
            pyautogui.click()
            print("Potato Found!")
            self.potato_count += 1

        time_to_count = pyautogui.locateOnScreen('images/960x540/timetocount.png', confidence=0.9)
        if time_to_count is not None:
            print("Times up!")
            self.locate_count = 1

    def countdown(self, time_sec):
        """Perform a countdown and display the remaining time."""
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            time_format = f'{mins:02d}:{secs:02d}'
            print(time_format, end='\r')
            time.sleep(1)
            time_sec -= 1

        print("Start Button Missing!")

    def play_game(self):
        while True:
            try:
                if self.game_started:
                    self.locate_good_potato()
                else:
                    print('Trying to start')
                    self.click_start()
                    self.locate_count = 0
                if self.locate_count == 1 and self.game_started:
                    print(f"Game Finished - Potato Count: {self.potato_count}")
                    self.game_started = False
                    self.locate_count = 0
                    print('Sleeping for 5 minutes')
                    self.countdown(60 * 5)
            except:
                print(f"GameStarted = {self.game_started}")
                self.countdown(10)

def main():
    game = FarmersAgainstPotatoes()
    game.play_game()

if __name__ == '__main__':
    main()
