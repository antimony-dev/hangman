import mysql.connector as sb
import turtle
import random
import sys
window= turtle.Screen().setup(300,400)
t = turtle.Turtle()
print('Welcome To The Classic Game Of Hangman!')
global name
name=input('Enter Your Name : ')
con=sb.connect(host='localhost',username='root',passwd='sbchad',database='hangman')
cur=con.cursor(buffered=True)
global wg
wg=''
global guessed
guessed=''
global wrong
wrong=0
global correct
correct=0
def fruits():
    print('\nHint ! Word Is Name Of A Fruit.\n')
    sample=('''apple banana grape strawberry orange pineapple mango watermelon kiwi lemon pear pomegranate guava papaya cherry peach''')
    return(random.choice(sample.split(' ')))
def flowers():
    print('\nHint ! Word Is Name Of A Flower.\n')
    sample=('''rose lily hibiscus marigold lotus jasmine tulip daffodil sunflower''')
    return(random.choice(sample.split(' ')))
def vegetables():
    print('\nHint ! Word Is Name Of A Vegetable.\n')
    sample=('''cucumber onion carrot cabbage eggplant broccoli cauliflower potato pumpkin radish beetroot capsicum''')
    return(random.choice(sample.split(' ')))
def movies():
    print('\nHint ! Word Is Name Of A Movie.\n')
    sample=('''stree drishyam shershaah kesari sultan dangal krrish pk don bhootnath kick dhoom''')
    return(random.choice(sample.split(' ')))
def instruments():
    print('\nHint ! Word Is Name Of A Musical Instrument.\n')
    sample=('''flute guitar sitar violin piano tabla dholak harmonium veena''')
    return(random.choice(sample.split(' ')))
genre=[fruits,flowers,vegetables,movies,instruments]
word = random.choice(genre)()
for i in range(len(word)):
    print('_', end=' ')

def end():
        sys.exit()

def disprecords():
    cur.execute("select* from player")
    final=cur.fetchall()
    con.commit()
    for i in final:
        print(i)
    end()

def records(r):
    global name
    q1="insert into player (Name,Result) values ('{}','{}')".format(name,r)
    cur.execute(q1)
    con.commit()
    n=input("\nPress <y> to see the previous records\nPress any other key to exit:")
    print("\n")
    if n.lower()=='y':
        disprecords()
    else:
        end()

def won():
    print('\nThe Word Was :',word)
    print('''                  
                                 You won 👍👍👍
                               HANGMAN Survived 😁.
                              Thanks For Playing''')
    records("won")

def lost():
    print('\nThe Word Was :',word)
   
    
    print('''                     
                                  You Lost 👎👎👎
                          HANGMAN Was Hanged To Death 😟.
                               Thanks For Playing''')
    records("lost")

def guess(g):
    global wrong
    global correct
    if (g in word):
        c=word.count(g)
        for _ in range(c):
            global guessed
            guessed+=g
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                    correct+=1
                else:
                    print('_', end=' ')
            guessing(guessed)
            break
    else:
        global wg
        wg+=g
        if (wrong==0):
            t.circle(50)
            t.rt(90)
            wrong += 1
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            guessing(guessed)
        elif(wrong==1):
            t.fd(120)
            t.bk(90)
            wrong += 1
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            guessing(guessed)
        elif(wrong==2):
            t.lt(50)
            t.fd(60)
            t.bk(60)
            t.rt(50)
            wrong += 1
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            guessing(guessed)
        elif(wrong==3):
            t.rt(50)
            t.fd(60)
            t.bk(60)
            t.lt(50)
            t.fd(90)
            wrong+=1
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            guessing(guessed)
        elif(wrong==4):
            t.lt(50)
            t.fd(60)
            t.bk(60)
            t.rt(50)
            wrong += 1
            for char in word:
                if (char in list(guessed)):
                    print(char, end=' ')
                else:
                    print('_', end=' ')
            guessing(guessed)
        else:
            t.rt(50)
            t.fd(60)
            t.bk(60)
            t.lt(50)
            lost()
def guessing(guessed):
    if (len(guessed)==len(set(word))):
        won()
    else:
        g = input('\n\nGuess a Word :')
        g.lower()
        if (g.isalpha() and len(g)==1 and g not in list(guessed) and g not in list(wg)):
            guess(g)
        elif(g in list(guessed)or g in list(wg)):
            print('Letter already guessed')
            guessing(guessed)
        else:
            print('Enter only 1 letter')
            guessing(guessed)
guessing(guessed)
