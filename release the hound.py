import pyautogui
import random as r
import time

#
# CURRENT BEST WPM: 76
#

backslash = ""

chosen = input('Enter the challenge you would like to bot (ex. python7):  ')
filtered = ''

# after each entry comes a comma
data = {
    'python1': """print "Hello World"|print 7|print 5 + 4|print "5 + 4"|print "5" + "4"|print 5 * 2|print 24 / 6|print 10 - 3|print 2 * 4 - 3|print 2 * (4 - 3)|print "ROAR! " * 5|print "Add a leading # to make one line be comment"|print "Comments are just for you, they will be ignored when the code runs"|""",
    'python2': """a = 1|b = 2|print a|print a + b|c = 1.5|print a + b + c|print 1 < 2|print 3 == 3|print 4 == 3|print 3 > 4|print 1 < 2 and 3 < 4|print 3 < 3 or 3 == 3|print 3 <= 3|print not 1 < 2|s1 = "Hello"|print s1|s2 = "15"|print s2 * 2|print int(s2) * 2|s3 = "3.14"|print s3 * 2|print float(s3) * 2|""",
    'python3': """s = "hello world"|print "hello" + "  ,  " + "python" + "  !"|print len(s)|print s.capitalize()|print s.count("h")|print s.count("o")|print s.count("world")|print s.endswith("orld")|print s.endswith("ello")|print s.startswith("he")|print s.upper()|print s.lower()|print s.title()|print s.split()|print s.find("he")|print s.find("world")|print s.find("py")|""",
    'python4': """name = raw_input("Enter your name")|print "Hello", name|age = raw_input("Enter your age")|print "You are", age, "years old"|color = raw_input("Enter your favorite color")|print "Your favorite color is", color|number = raw_input("What is your favorite number?")|print "Your favorite number is", number|multiplied = int(number) * 2|print "Your favorite number doubled is", multiplied|""",
    'python5': """weather = "sunny"|if weather == "sunny":|print "We will go on a picnic!"|print "Hooray!"|import time|time.sleep(0.5)|age = int(raw_input("Enter your age:"))|if age >= 13:|print "You can watch this movie"|else:|print "Sorry, you can't watch this movie"|time.sleep(0.5)|score = float(raw_input("how would you rate this movie? (1~5):"))|if score >= 4.5:|print "You like it very much"|elif score >= 3.5:|print "You like it"|elif score >= 2.5:|print "You think it is an average movie"|else:|print "You don't like it :("|""",
    'python6': """shopping_list = ["milk", "apple juice", "beacon", "tomato"]|print shopping_list, "has", len(shopping_list), "items"|shopping_list.append("grape")|shopping_list.append("orange")|print shopping_list|print shopping_list[0]|print shopping_list[2]|shopping_list.extend(["eggs", "bagel"])|print shopping_list|shopping_list.remove("milk")|print shopping_list|shopping_list.remove("beacon")|print shopping_list|shopping_list.sort()|print "After sorted:"|print shopping_list|mylist = [1, 2, "apple", 3.14, "circle"]|print mylist|""",
    'python7': """numbers = [12, 3, 25, 36]|print numbers[0]|print numbers[1]|print numbers[2]|print numbers[3]|print "* for-loop demo:"|for index in range(len(numbers)):|print numbers[index]|for num in numbers:|print num|for i in range(10):|print "Hello Python"|print "* while-loop demo:"|i = 0|while i < len(numbers):|print numbers[i]|i = i + 1|counter = 0|while counter < 10:|print "Hello Python"|counter = counter + 1|print "* break demo:"|for i in range(10):|if i == 6:|break|print i|print "* continue demo:"|for i in range(10):|if i == 6:|continue|print i|""",
    'python8': """number = raw_input("Enter a number")|decimal = int(number)|binary = ""|while decimal > 0:|remainder = decimal % 2|binary = str(remainder) + binary|decimal = decimal / 2|print number, "in binary is", binary|""",
    'python9': """number = raw_input("Enter a number")|decimal = int(number)|hexadecimal = ""|while decimal > 0:|remainder = decimal % 16|if remainder < 10:|hexadecimal = str(remainder) + hexadecimal|elif remainder == 10:|hexadecimal = "A" + hexadecimal|elif remainder == 11:|hexadecimal = "B" + hexadecimal|elif remainder == 12:|hexadecimal = "C" + hexadecimal|elif remainder == 13:|hexadecimal = "D" + hexadecimal|elif remainder == 14:|hexadecimal = "E" + hexadecimal|else:|hexadecimal = "F" + hexadecimal|decimal = decimal / 16|print number, "in hexadecimal is", hexadecimal|""",
    'python10': """import time|print "Timezone:", time.tzname|for i in range(5):|print time.asctime()|time.sleep(1)|print "-" * 20|import random|numbers = [1, 2, 3, 4, 5]|print random.choice(numbers)|newNumber = random.randint(10, 20)|numbers.append(newNumber)|print numbers|random.shuffle(numbers)|print numbers|""",
    'python11': """import random|import time|x = random.randint(1, 50)|chances = 10|numGuesses = 0|guess = 0|while numGuesses < chances:|guess = raw_input("Guess a number between 1 and 100")|guess = int(guess)|if guess > 100 or guess < 1:|print guess, "is out of range"|numGuesses += 1|elif guess > x:|print guess, "is too high"|numGuesses += 1|elif guess < x:|print guess, "is too low"|numGuesses += 1|else:|print "Correct!"|break|time.sleep(0.5)|if guess != x:|print "The correct number was", x|""",
    'python12': """import time|choice = ""|total = 0.0|while choice != "done":|choice = raw_input("burger, pizza or cookies."|+ " type 'done' when you are done")|choice = choice.lower()|if choice == "burger":|total = total + 4.50|elif choice == "pizza":|total = total + 2.0|elif choice == "cookies":|total = total + 2.50|elif choice == "done":|break|else:|print "We don't have", choice|time.sleep(0.5)|continue|print "Your choice:", choice|time.sleep(0.5)|print "Your total is $" + str(total)|""",
    'python13': """import time|for multiplier in range(1, 5):|for i in range(1, 10):|print i, "x", multiplier, "=", i * multiplier|print "-" * 10|time.sleep(1)|numStars = int(raw_input("How many stars do you want in one line?"))|numLines = int(raw_input("How many lines do you want?"))|for i in range(numLines):|for j in range(numStars):|print "*",|print ""|print "-" * 10|time.sleep(1)|numBlocks = int(raw_input("How many star blocks do you want?"))|for k in range(numBlocks):|print "[block %s]:" % k|for i in range(numLines):|for j in range(numStars):|print "*",|print ""|""",
    'python14': """from random import randint|myList = []|for counter in range(10):|myList.append(randint(1, 100))|print "Before sorting:"|print myList|iterCount = 1|for i in range(len(myList)):|smallest = i|for j in range(i, len(myList)):|if myList[j] < myList[smallest]:|smallest = j|if smallest != i:|temp = myList[i]|myList[i] = myList[smallest]|myList[smallest] = temp|print "Iteration", iterCount, ":", myList|iterCount = iterCount + 1|print "After sorting:"|print myList|""",
    'python15': """from random import randint|myList = []|for counter in range(10):|myList.append(randint(1, 100))|print "Before sorting:"|print myList|iterCount = 1|for index in range(1, len(myList)):|currValue = myList[index]|position = index|while position > 0 and myList[position - 1] > currValue:|myList[position] = myList[position - 1]|position = position - 1|myList[position] = currValue|print "Iteration", iterCount, ":", myList|iterCount += 1|print "After sorting:"|print myList|""",
    'python16': """myDict = {|"hello": "an expression of greeting",|"world": "everything that exists anywhere"|}|print "Query - hello:", myDict["hello"]|menu = {|"milk": 3.72,|"bacon": 4.98,|"burger": 3.5|}|print "Price of bacon is", menu["bacon"]|if menu.has_key("milk"):|print "We have milk"|else:|print "Sorry, we don't have milk"|if "milk" in menu:|print "We have milk"|print menu.keys()|print "* Menu:"|for (key, value) in menu.items():|print key, ":", value|menu["milk"] = 3.82|menu["sausage"] = 4.94|print menu|menu.pop("burger")|print menu|""",
    'python17': """calories = {|"apple": 95,|"banana": 105,|"pineapple": 402,|"orange": 45,|"mango": 201,|}|import time|answer = ""|totalCalories = 0|while answer != "done":|answer = raw_input("What do you want?\\n %s \\nInput 'done' to finish" %|calories.keys())|answer = answer.lower()|if answer in calories:|print "You choose", answer|totalCalories += calories[answer]|elif answer == "done":|continue|else:|print "Sorry, we don't have", answer|time.sleep(0.2)|print "Total calories:", totalCalories|""",
    'python18': """def printInfo():|print "John"|print "Address: 10 xyz lane"|print "Favorite color: blue"|print "Favorite coding language: Python"|print|printInfo()|printInfo()|def printInfo(name, addr, color, lang):|print name|print "Address:", addr|print "Favorite color:", color|print "Favorite coding language:", lang|print|printInfo("Bob", "11 abc Lane", "green", "Java")|printInfo("Alice", "236 meadow dr", "pink", "Scratch")|def add(a, b):|return a + b|c = add(1, 2)|print "sum is:", c|print|def checkPlease(price, taxRate, tipsRate):|tax = price * taxRate|tips = price * tipsRate|total = price + tax + tips|return total|print "Your total is:", checkPlease(13.5, 0.05, 0.15)|""",
    'python19': """speed = 10|def speedUp1():|print "I am going to change the speed"|speed = 20|speedUp1()|print "After calling speedUp1, current speed is:", speed|print|def speedUp2():|global speed|print "I declare speed is the global one"|print "I am going to really change the speed"|speed = 20|speedUp2()|print "After calling speedUp2, current speed is:", speed|""",

}


# Lowest sleep possible on Windows is 1 millisecond
# (10, 90) / 1000 -> 63 / 1000 -> 0.063

def run(given):
    for i in data[given]:
        if i == '|':
            pyautogui.press('enter')
        elif i.isalpha():
            time.sleep(0.001)  # waiting 0.001 seconds is the lowest on Win
            pyautogui.typewrite(i)
        elif i.isnumeric():
            time.sleep(r.randint(10, 90) / 1000)
            pyautogui.typewrite(i)
        elif i == '':
            time.sleep(r.randint(1, 5) / 1000)
            pyautogui.typewrite('')
        else:
            time.sleep(r.randint(20, 200) / 1000)
            pyautogui.typewrite(i)


for i in chosen:
    if i.isalpha():
        filtered += i
    elif i.isnumeric():
        filtered += i
    else:
        print('ERROR: INVALID INPUT')
        quit()
if data.get(filtered) is not None:
    pass
else:
    print('Such challenge does not exist or has not been added in this program')
    quit()

input('Press Enter to Start - You will have 3 seconds to get in position:\n')
time.sleep(3)

if __name__ == '__main__':
    run(filtered)

# Area to get raw challenge data
# Make sure all lines are line up against the left wall
# No extra spaces before line
# Fix broken print statements if needed
# CTRL + \ -> DEL -> END
# Makes a | at the end of the first line and deletes the space between the next, repeat
# If faced with a backslash n, make it \\n
