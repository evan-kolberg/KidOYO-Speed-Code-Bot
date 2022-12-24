import random as r
import time
import keyboard

import challenges

lang = ''
num = ''
procede = ''


def run(input_lang, input_num):
    for i in challenges.data[input_lang][input_num].split('|'):
        for j in i:
            keyboard.write(j)
            if i.isalnum() == False:
                if r.randint(0,20) <= 1:
                    zzz = r.randint(200, 500)/1000
                    time.sleep(zzz)
                else:
                    zzz = r.randint(0, 150)/1000
                    time.sleep(zzz)
            else:
                zzz = r.randint(0, 100)/1000
                time.sleep(zzz) 
        keyboard.send('enter')


def select_a_challenge():
    global lang, num
    choice = input('Enter the challenge you would like to bot (ex. python7, c++9):\n')
    for i in choice:
        if i.isalpha() or i == '+': lang += i
        elif i.isnumeric(): num += i
        else: print('ERROR: INVALID INPUT'); quit()
    try: challenges.data[lang][num]
    except: print('\nSorry, that challenge hasn\'t been added yet'); quit()


if __name__ == '__main__':
    select_a_challenge()

    while True:

        print('\nWhen you press ENTER, you have 3 seconds until the program will simulate keyboard input')
        keyboard.wait('enter')

        time.sleep(3)

        run(lang, num)

        if int(num) != 40:
            print('Cool! Let\'s move on to the next one')
            num = int(num)
            num += 1
            num = str(num)
            continue

        elif int(num) == 40:
            print('Looks like you have comlpete all the exercises in this language')
            select_a_challenge()
        
        else:
            break

# use print colors in the console to make it look pretty