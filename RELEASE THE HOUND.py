import pyautogui
import random as r
import time
import keyboard

import challenges

# CURRENT BEST WPM: 80 on Python27 - Rank 1 on the leaderboard

"""
To Run File:
Step 1: Click run
Step 2: Type in the challenge name with number (ex. python7, html9)
Step 3: Refresh chrome tab
Step 4: Once your chrome tab is refreshed, click on the typing box (or anywhere on the site)
to get ready for the hound to type away
Step 5: Press enter on your keyboard as soon as the T-Countdown gets to 3 (T-0:03)
Step 6: Enjoy climbing to the top of the leaderboards and blowing though badges!
"""


# Lowest sleep possible on Windows is 1 millisecond
# (10, 90) / 1000 -> 63 / 1000 -> 0.063
def run(input_lang, input_num):
    for i in challenges.data[input_lang][input_num]:
        if i == '|':
            pyautogui.press('enter')
        elif i == '':
            time.sleep(r.randint(0, 5) / 1000)
            pyautogui.typewrite('')
        elif i.isalpha():
            time.sleep(r.randint(1, 15) / 1000)
            pyautogui.typewrite(i)
        elif i.isnumeric():
            time.sleep(r.randint(1, 120) / 1000)
            pyautogui.typewrite(i)
        else:
            time.sleep(r.randint(1, 250) / 1000)
            pyautogui.typewrite(i)


chosen = input('Enter the challenge you would like to bot (ex. python7, c++9):\n')

lang = ''
num = ''

for i in chosen:
    if i.isalpha() or i == '+':
        lang += i
    elif i.isnumeric():
        num += i
    else:
        print('ERROR: INVALID INPUT')
        quit()

try:
    challenges.data[lang][num]
except:
    print('\nSorry, that challenge hasn\'t been added yet')
    quit()


print('\nGo get ready in the Speed Code Lobby. Once you are ready, click on the challenge\n'
      'and press enter when T-0:03. Enjoy!')
keyboard.wait('enter')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('\nR E L E A S E    T H E    H O U N D')

if __name__ == '__main__':
    run(lang, num)

