data = {
    'python': {
        '1': """print "Hello World"|print 7|print 5 + 4|print "5 + 4"|print "5" + "4"|print 5 * 2|print 24 / 6|print 10 - 3|print 2 * 4 - 3|print 2 * (4 - 3)|print "ROAR! " * 5|print "Add a leading # to make one line be comment"|print "Comments are just for you, they will be ignored when the code runs"|""",
        '2': """a = 1|b = 2|print a|print a + b|c = 1.5|print a + b + c|print 1 < 2|print 3 == 3|print 4 == 3|print 3 > 4|print 1 < 2 and 3 < 4|print 3 < 3 or 3 == 3|print 3 <= 3|print not 1 < 2|s1 = "Hello"|print s1|s2 = "15"|print s2 * 2|print int(s2) * 2|s3 = "3.14"|print s3 * 2|print float(s3) * 2|""",
        '3': """s = "hello world"|print "hello" + "  ,  " + "" + "  !"|print len(s)|print s.capitalize()|print s.count("h")|print s.count("o")|print s.count("world")|print s.endswith("orld")|print s.endswith("ello")|print s.startswith("he")|print s.upper()|print s.lower()|print s.title()|print s.split()|print s.find("he")|print s.find("world")|print s.find("py")|""",
        '4': """name = raw_input("Enter your name")|print "Hello", name|age = raw_input("Enter your age")|print "You are", age, "years old"|color = raw_input("Enter your favorite color")|print "Your favorite color is", color|number = raw_input("What is your favorite number?")|print "Your favorite number is", number|multiplied = int(number) * 2|print "Your favorite number doubled is", multiplied|""",
        '5': """weather = "sunny"|if weather == "sunny":|print "We will go on a picnic!"|print "Hooray!"|import time|time.sleep(0.5)|age = int(raw_input("Enter your age:"))|if age >= 13:|print "You can watch this movie"|else:|print "Sorry, you can't watch this movie"|time.sleep(0.5)|score = float(raw_input("how would you rate this movie? (1~5):"))|if score >= 4.5:|print "You like it very much"|elif score >= 3.5:|print "You like it"|elif score >= 2.5:|print "You think it is an average movie"|else:|print "You don't like it :("|""",
        '6': """shopping_list = ["milk", "apple juice", "beacon", "tomato"]|print shopping_list, "has", len(shopping_list), "items"|shopping_list.append("grape")|shopping_list.append("orange")|print shopping_list|print shopping_list[0]|print shopping_list[2]|shopping_list.extend(["eggs", "bagel"])|print shopping_list|shopping_list.remove("milk")|print shopping_list|shopping_list.remove("beacon")|print shopping_list|shopping_list.sort()|print "After sorted:"|print shopping_list|mylist = [1, 2, "apple", 3.14, "circle"]|print mylist|""",
        '7': """numbers = [12, 3, 25, 36]|print numbers[0]|print numbers[1]|print numbers[2]|print numbers[3]|print "* for-loop demo:"|for index in range(len(numbers)):|print numbers[index]|for num in numbers:|print num|for i in range(10):|print "Hello "|print "* while-loop demo:"|i = 0|while i < len(numbers):|print numbers[i]|i = i + 1|counter = 0|while counter < 10:|print "Hello "|counter = counter + 1|print "* break demo:"|for i in range(10):|if i == 6:|break|print i|print "* continue demo:"|for i in range(10):|if i == 6:|continue|print i|""",
        '8': """number = raw_input("Enter a number")|decimal = int(number)|binary = ""|while decimal > 0:|remainder = decimal % 2|binary = str(remainder) + binary|decimal = decimal / 2|print number, "in binary is", binary|""",
        '9': """number = raw_input("Enter a number")|decimal = int(number)|hexadecimal = ""|while decimal > 0:|remainder = decimal % 16|if remainder < 10:|hexadecimal = str(remainder) + hexadecimal|elif remainder == 10:|hexadecimal = "A" + hexadecimal|elif remainder == 11:|hexadecimal = "B" + hexadecimal|elif remainder == 12:|hexadecimal = "C" + hexadecimal|elif remainder == 13:|hexadecimal = "D" + hexadecimal|elif remainder == 14:|hexadecimal = "E" + hexadecimal|else:|hexadecimal = "F" + hexadecimal|decimal = decimal / 16|print number, "in hexadecimal is", hexadecimal|""",
        '10': """import time|print "Timezone:", time.tzname|for i in range(5):|print time.asctime()|time.sleep(1)|print "-" * 20|import random|numbers = [1, 2, 3, 4, 5]|print random.choice(numbers)|newNumber = random.randint(10, 20)|numbers.append(newNumber)|print numbers|random.shuffle(numbers)|print numbers|""",
        '11': """import random|import time|x = random.randint(1, 50)|chances = 10|numGuesses = 0|guess = 0|while numGuesses < chances:|guess = raw_input("Guess a number between 1 and 100")|guess = int(guess)|if guess > 100 or guess < 1:|print guess, "is out of range"|numGuesses += 1|elif guess > x:|print guess, "is too high"|numGuesses += 1|elif guess < x:|print guess, "is too low"|numGuesses += 1|else:|print "Correct!"|break|time.sleep(0.5)|if guess != x:|print "The correct number was", x|""",
        '12': """import time|choice = ""|total = 0.0|while choice != "done":|choice = raw_input("burger, pizza or cookies."|+ " type 'done' when you are done")|choice = choice.lower()|if choice == "burger":|total = total + 4.50|elif choice == "pizza":|total = total + 2.0|elif choice == "cookies":|total = total + 2.50|elif choice == "done":|break|else:|print "We don't have", choice|time.sleep(0.5)|continue|print "Your choice:", choice|time.sleep(0.5)|print "Your total is $" + str(total)|""",
        '13': """import time|for multiplier in range(1, 5):|for i in range(1, 10):|print i, "x", multiplier, "=", i * multiplier|print "-" * 10|time.sleep(1)|numStars = int(raw_input("How many stars do you want in one line?"))|numLines = int(raw_input("How many lines do you want?"))|for i in range(numLines):|for j in range(numStars):|print "*",|print ""|print "-" * 10|time.sleep(1)|numBlocks = int(raw_input("How many star blocks do you want?"))|for k in range(numBlocks):|print "[block %s]:" % k|for i in range(numLines):|for j in range(numStars):|print "*",|print ""|""",
        '14': """from random import randint|myList = []|for counter in range(10):|myList.append(randint(1, 100))|print "Before sorting:"|print myList|iterCount = 1|for i in range(len(myList)):|smallest = i|for j in range(i, len(myList)):|if myList[j] < myList[smallest]:|smallest = j|if smallest != i:|temp = myList[i]|myList[i] = myList[smallest]|myList[smallest] = temp|print "Iteration", iterCount, ":", myList|iterCount = iterCount + 1|print "After sorting:"|print myList|""",
        '15': """from random import randint|myList = []|for counter in range(10):|myList.append(randint(1, 100))|print "Before sorting:"|print myList|iterCount = 1|for index in range(1, len(myList)):|currValue = myList[index]|position = index|while position > 0 and myList[position - 1] > currValue:|myList[position] = myList[position - 1]|position = position - 1|myList[position] = currValue|print "Iteration", iterCount, ":", myList|iterCount += 1|print "After sorting:"|print myList|""",
        '16': """myDict = {|"hello": "an expression of greeting",|"world": "everything that exists anywhere"|}|print "Query - hello:", myDict["hello"]|menu = {|"milk": 3.72,|"bacon": 4.98,|"burger": 3.5|}|print "Price of bacon is", menu["bacon"]|if menu.has_key("milk"):|print "We have milk"|else:|print "Sorry, we don't have milk"|if "milk" in menu:|print "We have milk"|print menu.keys()|print "* Menu:"|for (key, value) in menu.items():|print key, ":", value|menu["milk"] = 3.82|menu["sausage"] = 4.94|print menu|menu.pop("burger")|print menu|""",
        '17': """calories = {|"apple": 95,|"banana": 105,|"pineapple": 402,|"orange": 45,|"mango": 201,|}|import time|answer = ""|totalCalories = 0|while answer != "done":|answer = raw_input("What do you want?\\n %s \\nInput 'done' to finish" %|calories.keys())|answer = answer.lower()|if answer in calories:|print "You choose", answer|totalCalories += calories[answer]|elif answer == "done":|continue|else:|print "Sorry, we don't have", answer|time.sleep(0.2)|print "Total calories:", totalCalories|""",
        '18': """def printInfo():|print "John"|print "Address: 10 xyz lane"|print "Favorite color: blue"|print "Favorite coding language: "|print|printInfo()|printInfo()|def printInfo(name, addr, color, lang):|print name|print "Address:", addr|print "Favorite color:", color|print "Favorite coding language:", lang|print|printInfo("Bob", "11 abc Lane", "green", "Java")|printInfo("Alice", "236 meadow dr", "pink", "Scratch")|def add(a, b):|return a + b|c = add(1, 2)|print "sum is:", c|print|def checkPlease(price, taxRate, tipsRate):|tax = price * taxRate|tips = price * tipsRate|total = price + tax + tips|return total|print "Your total is:", checkPlease(13.5, 0.05, 0.15)|""",
        '19': """speed = 10|def speedUp1():|print "I am going to change the speed"|speed = 20|speedUp1()|print "After calling speedUp1, current speed is:", speed|print|def speedUp2():|global speed|print "I declare speed is the global one"|print "I am going to really change the speed"|speed = 20|speedUp2()|print "After calling speedUp2, current speed is:", speed|""",
        '20': """def fibonacci(num):|if num == 0:|return 0|if num == 1:|return 1|return fibonacci(num-2) + fibonacci(num-1)|for i in range(10):|print fibonacci(i),|print|def power(base, exp):|if exp == 0:|return 1|return base * power(base, exp-1)|print "2^5 is:", power(2, 5)|print "3^2 is:", power(3, 2)|print "4^5 is:", power(4, 5)|""",
        '21': """import math|class Circle:|def __init__(self, radius):|self.radius = radius|def circumference(self):|return 2 * math.pi * self.radius|def area(self):|return math.pi * self.radius * self.radius|c1 = Circle(1.2)|print "Circle c1"|print "- radius:", c1.radius|print "- circumference:", c1.circumference()|print "- area:", c1.area()|c2 = Circle(2.5)|print "Circle c2"|print "- radius:", c2.radius|print "- circumference:", c2.circumference()|print "- area:", c2.area()|""",
        '22': """class Person:|def __init__(self, name, birthyear):|self.name = name|self.birthyear = birthyear|def printInfo(self):|print "Name:", self.name|print "Year of birth:", self.birthyear|class Student(Person):|def __init__(self, name, birthyear, school):|Person.__init__(self, name, birthyear)|self.school = school|def printInfo(self):|Person.printInfo(self)|print "School:", self.school|class CollegeStudent(Student):|def __init__(self, name, birthyear, school, major):|Student.__init__(self, name, birthyear, school)|self.major = major|def printInfo(self):|Student.printInfo(self)|print "Major:", self.major|student1 = Student("Alice", 2000, "Meadow High School")|student1.printInfo()|print "-" * 10|student2 = CollegeStudent("Bob", 1996, "MIT", "Computer Science")|student2.printInfo()|""",
        '23': """from turtle import Turtle|t = Turtle()|t.setposition(-200, 200)|t.forward(100)|t.right(90)|t.forward(80)|t.circle(40)|t.color("red")|t.circle(40, 180)|t.shape("turtle")|t.stamp()|t.forward(100)|t.setposition(0, 0)|t.goto(50, 50)|t.goto(100, 0)|t.goto(0, 0)|t.goto(0, -100)|t.goto(100, -100)|t.goto(100, 0)|t.setposition(40, -100)|t.goto(40, -50)|t.goto(60, -50)|t.goto(60, -100)|t.color("green")|t.setposition(50, -90)|""",
        '24': """from turtle import Turtle|from random import randint|t = Turtle()|for counter in range(4):|t.forward(40)|t.right(90)|t.setposition(-100, -100)|for counter in range(50):|t.color(0, randint(0, 255), randint(0, 255))|t.forward(100)|t.right(115)|t.setposition(80, 120)|for counter in range(50):|t.color(randint(0, 255), randint(0, 255), randint(0, 255))|t.forward(90)|t.right(82)|""",
        '25': """from turtle import Turtle|t = Turtle()|def hexagon(size):|for i in range(6):|t.forward(size)|t.right(60)|t.setposition(-150, 150)|hexagon(40)|t.setposition(150, 150)|hexagon(20)|t.setposition(-150, -150)|hexagon(50)|t.setposition(0, 0)|for i in range(6):|hexagon(30)|t.forward(30)|t.left(60)|""",
        '26': """from turtle import Turtle|t = Turtle()|t.begin_fill()|for counter in range(4):|t.forward(80)|t.right(90)|t.end_fill()|t.setposition(-150, 150)|t.color("orange")|t.begin_fill()|for counter in range(6):|t.forward(80)|t.right(60)|t.end_fill()|t.setposition(-150, -100)|t.color("blue")|t.begin_fill()|for i in range(12):|t.forward(40)|t.right(30)|t.end_fill()|t.setposition(150, 100)|t.color("#339960")|t.begin_fill()|t.circle(40)|t.end_fill()|""",
        '27': """from turtle import Turtle|t = Turtle()|t.width(1)|t.speed(10)|for j in range(3):|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|t.penup()|t.back(60)|t.left(90)|t.forward(20)|t.right(90)|t.pendown()|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|t.color("blue")|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|t.color("black")|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|t.penup()|t.back(60)|t.left(90)|t.forward(20)|t.right(90)|t.pendown()|for j in range(3):|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|""",
        '28': """from turtle import Turtle|t = Turtle()|t.width(1)|t.speed(10)|def square(color):|t.color(color)|t.begin_fill()|for i in range(4):|t.forward(20)|t.right(90)|t.end_fill()|t.forward(20)|def nextRow(numSquares):|t.up()|t.back(numSquares * 20)|t.left(90)|t.forward(20)|t.right(90)|t.down()|for j in range(3):|square("black")|nextRow(3)|square("black")|square("blue")|square("black")|nextRow(3)|for j in range(3):|square("black")|""",
        '29': """from turtle import Turtle|t = Turtle()|t.width(1)|t.speed(10)|side = 20|width = 3|def row(colors, numbers):|for i in range(len(colors)):|t.color(colors[i])|for j in range(numbers[i]):|t.begin_fill()|for k in range(4):|t.forward(side)|t.right(90)|t.end_fill()|t.forward(side)|t.up()|t.back(width * side)|t.left(90)|t.forward(side)|t.right(90)|t.down()|colors = ["black"]|numbers = [3]|row(colors, numbers)|colors = ["black", "blue", "black"]|numbers = [1, 1, 1]|row(colors, numbers)|colors = ["black"]|numbers = [3]|row(colors, numbers)|""",
        '30': """from turtle import Turtle|t = Turtle()|t.width(1)|t.speed(10)|side = 20|width = 9|height = 9|white, black, red, darkred = 'white', 'black', 'red', 'darkred'|t.setposition(-(width * (side/2)), height * (side/2))|def row(pixels):|for (color, count) in pixels:|t.color(color)|for j in range(count):|t.begin_fill()|for k in range(4):|t.forward(side)|t.right(90)|t.end_fill()|t.forward(side)|t.penup()|t.back(width * side)|t.right(90)|t.forward(side)|t.left(90)|t.pendown()|row([(white, 2), (black, 2), (white, 1), (black, 2), (white, 2)])|row([(white, 1), (black, 1), (red, 2), (black, 1),|(red, 2), (black, 1), (white, 1)])|row([(black, 1), (red, 1), (white, 1), (red, 5), (black, 1)])|row([(black, 1), (red, 7), (black, 1)])|row([(black, 1), (darkred, 1), (red, 5), (darkred, 1), (black, 1)])|row([(white, 1), (black, 1), (darkred, 1),|(red, 3), (darkred, 1), (black, 1), (white, 1)])|row([(white, 2), (black, 1), (darkred, 1),|(red, 1), (darkred, 1), (black, 1), (white, 2)])|row([(white, 3), (black, 1), (darkred, 1), (black, 1), (white, 3)])|row([(white, 4), (black, 1), (white, 4)])|""",
        '31': """from processing import *|def setup():|size(400, 400)|def draw():|background(0, 0, 0)|stroke(255)|line(0, 0, 50, 200)|fill(255, 0, 0)|ellipse(180, 80, 150, 100)|noStroke()|fill(0, 0, 255)|ellipse(180, 200, 150, 100)|fill(255, 160, 0)|rect(50, 300, 100, 70)|fill(0, 200, 0)|triangle(300, 200, 280, 380, 350, 350)|run()|""",
        '32': """from processing import *|import math|width = 520|height = 360|radius = 16|theta = 0|dx = 0|steps = width / radius + 1|def setup():|global dx|size(width, height)|dx = float(TWO_PI / width) * radius|colorMode(HSB)|def draw():|global theta|background(0, 0, 0)|theta += 0.05|x = theta|hue = 0|for i in range(steps):|y = height / 2 + math.sin(x) * 70|x += dx|fill(hue, 255, 240)|ellipse(i * radius, y, radius, radius)|hue += 5|run()|""",
        '33': """from processing import *|from random import randint|rotating_sun = 0|rotating_earth = 0|rotating_moon = 0|center_x = 250|center_y = 250|star_count = 150|stars = []|def setup():|size(540, 500)|for i in range(star_count):|x = randint(10, 530)|y = randint(10, 490)|width = randint(2, 8)|height = randint(2, 8)|color = randint(10, 100)|stars.append({|"x": x,|"y": y,|"width": width,|"height": height,|"color": color|})|def draw():|global rotating_sun, rotating_earth, rotating_moon|background(0, 0, 0)|for star in stars:|fill(star["color"])|ellipse(star["x"], star["y"], star["width"], star["height"])|noFill()|stroke(60, 60, 60)|arc(center_x, center_y, 140, 140, 0, 2*PI)|rotating_sun += -0.0001|rotating_earth += -0.005|rotating_moon += -0.06|noStroke()|translate(center_x, center_y)|rotate(rotating_sun)|fill(250, 0, 0)|ellipse(0, 0, 30, 30)|rotate(rotating_earth)|fill(100, 200, 250)|ellipse(70, 0, 13, 13)|translate(70, 0)|rotate(rotating_moon)|fill(250, 250, 0)|ellipse(10, 0, 4, 4)|run()|""",
        '34': """from processing import *|font = None|def setup():|global font|size(500, 400)|font = createFont("Comic Sans MS", 30)|def draw():|background(0)|textFont(font)|fill(0, 240, 255)|textSize(40)|text("My Clock", 140, 120)|time = "%02d/%02d/%02d %02d:%02d:%02d" % \|(month(), day(), year(), hour(), minute(), second())|textSize(35)|fill(0, 255, 0)|text(time, 80, 220)|run()|""",
        '35': """from processing import *|from math import sin|from random import randint|ballx = 30|bally = 30|rectx = 30|recty = 350|radius = 30|delay = 16|r = 100|g = 100|b = 100|def setup():|size(540, 400)|def draw():|global ballx, bally, rectx, recty, radius|background(r, g, b)|strokeWeight(10)|stroke(255)|fill(0, 121, 200)|ballx += float(mouse.x - ballx) / delay|bally += float(mouse.y - bally) / delay|radius = radius + sin(environment.frameCount / 4)|ellipse(ballx, bally, radius, radius)|strokeWeight(2)|fill(240, 150, 0)|rect(rectx, recty, 150, 30)|def mousePressed():|global r, g, b|r = randint(0, 150)|g = randint(0, 150)|b = randint(0, 150)|def keyPressed():|global rectx, recty|if keyboard.keyCode == UP:|recty -= 10|elif keyboard.keyCode == DOWN:|recty += 10|elif keyboard.keyCode == LEFT:|rectx -= 10|elif keyboard.keyCode == RIGHT:|rectx += 10|run()|""",
        '36': """from processing import *|angle = 0|numLines = 20|width = 400|height = 400|def setup():|size(width, height)|colorMode(HSB)|def draw():|global angle|hue = 0|background(25)|strokeWeight(3)|translate(200, 200)|for i in range(numLines):|hue += i|stroke(hue, 255, 200)|rotate(PI / 30)|line(mouse.x-width/2, mouse.y-height/2, 0, -60)|angle += 0.0001|rotate(angle)|run()|""",
        '37': """from processing import *|from random import choice|bunny = None|turtle = None|bunny_x = 10|turtle_x = 10|def setup():|global bunny, turtle|size(500, 400)|bunny = loadImage("https://speedcode.oyohub.com/img/bunny.png")|turtle = loadImage("https://speedcode.oyohub.com/img/turtle.png")|def draw():|background(255)|fill(20)|text("Use A and D key to move the turtle", 10, 20)|text("Use Left and Right arrow key to move the bunny", 230, 20)|image(turtle, turtle_x, 100, 60, 40)|image(bunny, bunny_x, 200, 60, 80)|noStroke()|fill(0, 200, 100)|rect(10, 140, 500, 10)|fill(240, 200, 0)|rect(10, 280, 500, 10)|textSize(30)|fill(0, 200, 100)|if turtle_x > 440:|text("Turtle won!", 170, 70)|exitp()|if bunny_x > 440:|text("Bunny won!", 170, 70)|exitp()|def keyPressed():|global turtle_x, bunny_x|if keyboard.key == "a":|turtle_x -= 10|elif keyboard.key == "d":|turtle_x += 10|if keyboard.keyCode == LEFT:|bunny_x -= 30|elif keyboard.keyCode == RIGHT:|if choice([0, 1, 2]) == 0:|bunny_x -= 30|else:|bunny_x += 30|run()|""",
        '38': """from processing import *|counter = 0|currFrame = 0|x = 300|y = 10|speedY = 0|frames = []|def setup():|global p1, p2, p3, frames|size(540, 400)|background(0, 102, 0)|stepLeft = loadImage("https://speedcode.oyohub.com/img/frame1.png")|stand = loadImage("https://speedcode.oyohub.com/img/frame2.png")|stepRight = loadImage("https://speedcode.oyohub.com/img/frame3.png")|frames = [stepLeft, stand, stepRight, stand]|def draw():|global counter, currFrame, y|background(0, 102, 0)|fill(255)|text("Use up and down arrow key to move the character", 10, 20)|noStroke()|rect(290, 0, 40, 400)|if counter == 10:|currFrame = (currFrame + 1) % 4|counter = 0|counter += 1|if speedY:|y += speedY|image(frames[currFrame], x, y, 20, 30)|else:|stand = frames[1]|image(stand, x, y, 20, 30)|def keyPressed():|global speedY|if keyboard.keyCode == UP:|speedY = -1|if keyboard.keyCode == DOWN:|speedY = 1|def keyReleased():|global speedY|if keyboard.keyCode in [UP, DOWN]:|speedY = 0|run()|""",
        '39': """from processing import *|import random|cat = None|catSoundList = [|"meow meow ~",|"where is my fish cake",|"pur pur pur ...",|]|class Cat:|def __init__(self, x, y, imgURL, soundList):|self.x = x|self.y = y|self.currSound = ""|self.img = loadImage(imgURL)|self.soundList = soundList|def moveLeft(self):|self.x -= 10|def moveRight(self):|self.x += 10|def startSpeaking(self):|if not self.currSound:|self.currSound = random.choice(self.soundList)|def endSpeaking(self):|self.currSound = ""|def draw(self):|image(self.img, self.x, self.y)|def speak(self):|if self.currSound:|fill(10)|textSize(20)|text(self.currSound, self.x, self.y - 10)|def setup():|global cat|size(540, 400)|background(255)|cat = Cat(200, 250,|"https://speedcode.oyohub.com/img/cat.png",|catSoundList)|def draw():|background(255)|fill(0)|text("Press space to speak", 200, 20)|cat.draw()|cat.speak()|def keyPressed():|if keyboard.keyCode == 32:|cat.startSpeaking()|def keyReleased():|if keyboard.keyCode == 32:|cat.endSpeaking()|run()|""",
        '40': """from processing import *|width = 540|height = 450|ball = {|"x": 50,|"y": 50,|"radius": 10,|"vel_x": 20,|"vel_y": 20|}|r = 0|g = 100|b = 200|rinc = 2|ginc = 3|binc = 1|def setup():|size(width, height)|background(0, 0, 0)|def draw():|fill(r, g, b)|ellipse(ball["x"], ball["y"], 2*ball["radius"], 2*ball["radius"])|moveBall()|changeBallColor()|def moveBall():|ball["x"] += ball["vel_x"]|ball["y"] += ball["vel_y"]|if ball["x"] + ball["radius"] >= width or \|ball["x"] - ball["radius"] <= 0:|ball["vel_x"] = -ball["vel_x"]|if ball["y"] + ball["radius"] >= height or \|ball["y"] - ball["radius"] <= 0:|ball["vel_y"] = -ball["vel_y"]|def changeBallColor():|global r, g, b, rinc, ginc, binc|r += rinc|g += ginc|b += binc|if r >= 255 or r <= 0:|rinc = -rinc|if g >= 255 or g <= 0:|ginc = -ginc|if b >= 255 or b <= 0:|binc = -binc|run()|"""
    },

    'html': {
        '1': """<!DOCTYPE html>|<html>|<head>|<title>Boilerplate</title>|</head>|<body>|Hello world! A HTML tag is like a container. An opening tag starts with a|pointy bracket followed by a tag name and a closing tag starts with a pointy bracket and a forward slash followed by the tag name.|</body>|</html>|""",
    },
}