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
                    print(zzz)
                    time.sleep(zzz)
                else:
                    zzz = r.randint(0, 150)/1000
                    print(zzz)
                    time.sleep(zzz)
            else:
                zzz = r.randint(0, 100)/1000
                print(zzz)
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

        procede = input('Do you wanna go onto the next one? (yes or no):  ')

        if procede == 'yes' and num != 40:
            num += 1
            continue

        elif procede == 'yes' and num == 40:
            select_a_challenge()
        
        else:
            break

# use print colors in the console to make it look pretty