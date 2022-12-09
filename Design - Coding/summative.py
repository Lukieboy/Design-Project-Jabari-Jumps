# imports
import time
import sys
import os
import random
import sys,tty
import curses

#intializing python cursor
stdscr=curses.initscr()
curses.endwin()
# A class with ANCII characters so that I can use color in the game
class colors:
  off='\033[0m' 
  class fg:
          black = '\033[30m'
          red = '\033[31m'
          green = '\033[32m'
          orange = '\033[33m'
          blue = '\033[34m'
          purple = '\033[35m'
          cyan = '\033[36m'
          lightgrey = '\033[37m'
          darkgrey = '\033[90m'
          lightred = '\033[91m'
          lightgreen = '\033[92m'
          yellow = '\033[93m'
          lightblue = '\033[94m'
          pink = '\033[95m'
          lightcyan = '\033[96m'
  class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'

##############################################
##############################################
#################VARIABLES####################
##############################################
##############################################
##non-dependent-some variables are in function
##because they are dependant on other variables
##which are referenced later on

#multi-line string for introduction
intro = """
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░████
█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░████
█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░████████████
█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████
█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░████
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░████████████
█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░████
█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████
█░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░████░░░░░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░░░█
█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░░░░░░░░░████████░░░░░░█████░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""

#multi line string for when you "jump" in the adventure game
jump= """
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦
░░░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀█ █ 
░▄░▒█ ▒█░▒█ ▒█▒█▒█ ▒█▄▄█ ▀ 
▒█▄▄█ ░▀▄▄▀ ▒█░░▒█ ▒█░░░ ▄
💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦"""

#array with a list of response to correct answers
correctAnswers = ["""
  ░█████╗░███╗░░░███╗░█████╗░███████╗██╗███╗░░██╗░██████╗░  ░░░░░██╗░█████╗░██████╗░██╗
  ██╔══██╗████╗░████║██╔══██╗╚════██║██║████╗░██║██╔════╝░  ░░░░░██║██╔══██╗██╔══██╗██║
  ███████║██╔████╔██║███████║░░███╔═╝██║██╔██╗██║██║░░██╗░  ░░░░░██║██║░░██║██████╦╝██║
  ██╔══██║██║╚██╔╝██║██╔══██║██╔══╝░░██║██║╚████║██║░░╚██╗  ██╗░░██║██║░░██║██╔══██╗╚═╝
  ██║░░██║██║░╚═╝░██║██║░░██║███████╗██║██║░╚███║╚██████╔╝  ╚█████╔╝╚█████╔╝██████╦╝██╗
  ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚════╝░░╚════╝░╚═════╝░╚═╝""",
  """
  ███████╗██╗░░██╗░█████╗░███████╗██╗░░░░░██╗░░░░░███████╗███╗░░██╗████████╗██╗
  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██║░░░░░██║░░░░░██╔════╝████╗░██║╚══██╔══╝██║
  █████╗░░░╚███╔╝░██║░░╚═╝█████╗░░██║░░░░░██║░░░░░█████╗░░██╔██╗██║░░░██║░░░██║
  ██╔══╝░░░██╔██╗░██║░░██╗██╔══╝░░██║░░░░░██║░░░░░██╔══╝░░██║╚████║░░░██║░░░╚═╝
  ███████╗██╔╝╚██╗╚█████╔╝███████╗███████╗███████╗███████╗██║░╚███║░░░██║░░░██╗
  ╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚══════╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝""",
  """
  ░██████╗░░█████╗░░█████╗░██████╗░  ░░░░░██╗░█████╗░██████╗░██╗
  ██╔════╝░██╔══██╗██╔══██╗██╔══██╗  ░░░░░██║██╔══██╗██╔══██╗██║
  ██║░░██╗░██║░░██║██║░░██║██║░░██║  ░░░░░██║██║░░██║██████╦╝██║
  ██║░░╚██╗██║░░██║██║░░██║██║░░██║  ██╗░░██║██║░░██║██╔══██╗╚═╝
  ╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝  ╚█████╔╝╚█████╔╝██████╦╝██╗
  ░╚═════╝░░╚════╝░░╚════╝░╚═════╝░  ░╚════╝░░╚════╝░╚═════╝░╚═╝""",
  """
  ███╗░░██╗██╗░█████╗░███████╗██╗
  ████╗░██║██║██╔══██╗██╔════╝██║
  ██╔██╗██║██║██║░░╚═╝█████╗░░██║
  ██║╚████║██║██║░░██╗██╔══╝░░╚═╝
  ██║░╚███║██║╚█████╔╝███████╗██╗
  ╚═╝░░╚══╝╚═╝░╚════╝░╚══════╝╚═╝"""
  ]

#array with a list of response to incorrect answers
wrongAnswer=["""
  ████████╗██████╗░██╗░░░██╗  ░█████╗░░██████╗░░█████╗░██╗███╗░░██╗
  ╚══██╔══╝██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔════╝░██╔══██╗██║████╗░██║
  ░░░██║░░░██████╔╝░╚████╔╝░  ███████║██║░░██╗░███████║██║██╔██╗██║
  ░░░██║░░░██╔══██╗░░╚██╔╝░░  ██╔══██║██║░░╚██╗██╔══██║██║██║╚████║
  ░░░██║░░░██║░░██║░░░██║░░░  ██║░░██║╚██████╔╝██║░░██║██║██║░╚███║
  ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝"""]

#array of all the questions for the quiz game
questions= [
    {
      "Question": "Who does Jabari go to the pool with? \n Press 1 for: His dad \n Press 2 for: His mom \n Press 3 for: His friend \n",
      "Answer":"1"
    },
    {
      "Question": "How does Jabari feel about jumping off the diving board? \n Press 1 for: sad  \n Press 2 for: bored \n Press 3 for: nervous \n",
      "Answer":"3"
    },
    {
      "Question": "What does Jabari do when he gets to the diving board? \n Press 1 for: Climb up the ladder first \n Press 2 for: Let the other kids go first \n",
      "Answer":"2"
    },
    {
      "Question": "What does Jabari's dad do? \n Press 1 for: He is rude to Jabari \n Press 2 for: He comforts Jabari \n Press 3 for: He takes Jabari home \n",
      "Answer":"2"
    },
    {
      "Question": "What did Jabari forget to do before jumping? \n Press 1 for: Stretch \n Press 2 for: rest \n Press 3 for: He didn't forget anything \n",
      "Answer":"1"
    },
    {
      "Question": "Do you think Jabari is lucky to be able to go to the pool? \n Press 1 for: Yes \n Press 2 for: No \n",
      "Answer":"1"
    },
    {
      "Question": "Is there clean water and pools everywhere in the world? \n Press 1 for: Yes \n Press 2 for: No \n",
      "Answer":"2"
    },
    {
      "Question": "Should everyone be able to drink clean water and go to the pool? \n Press 1 for Yes \n Press 2 for: No \n",
      "Answer":"1"
    },
    {
      "Question": "Do you think we should try and make sure everyone has clean water and pools? \n Press 1 for Yes \n Press 2 for: No \n",
      "Answer":"1"
    }
  ]


##############################################
##############################################
#################FUNCTIONS####################
##############################################
##############################################

#################Print Question Function###############
##This is the function that prints a question. to make it more interesting,##
##it will print with a "typing" effect and a random color!##
def printQuestion(str):
  #index of the end of the line so the question will be a random color,
  #but the options are white(note - for one line prints it doesn't matter)
  indexOfEndLine=str.find("\n")
  #random number between 0-5 to choose a random color
  randnum=random.randint(0,5)
  #pick a random color
  if randnum==0:
    print(colors.fg.green, " ")
  elif randnum==1:
    print(colors.fg.lightcyan, " ")
  elif randnum==2:
    print(colors.fg.purple, " ")
  elif randnum==3:
    print(colors.fg.blue, " ")
  elif randnum==4:
    print(colors.fg.green, " ")
  else:
    print(colors.fg.pink, " ")

  #print the question in a random color
  for x in range(0, indexOfEndLine):
    #each time print a character
    time.sleep(0.03)
    print(str[x], end="")
    sys.stdout.flush()
  print(colors.off, " ")

  #print the options in normal color
  for x in range(indexOfEndLine, len(str)):
    #each time print a character
    time.sleep(0.01)
    print(str[x], end="")
    sys.stdout.flush()
  print(colors.off, "\n")

#################Introduction function###############
##Shows the introduction to the game
def introduction():
  #clear the screen
  os.system("clear")
  #flash red, blue, green
  for x in range(8):
    #flash red
    print(colors.fg.red, intro)
    time.sleep(0.3)
    os.system("clear")
    #flash blue
    print(colors.fg.blue, intro)
    time.sleep(0.3)
    os.system("clear")
    #flash green
    print(colors.fg.green,intro)
    time.sleep(0.3)
    os.system("clear")

  print(colors.off, "")
introduction()

#################Personal Question Function###############
##Asks the user a few questions about themselves.
def askPersonalQuestions():

  ###ask the user what their name is###
  printQuestion("What is your name?(Type your name then press enter)\n")
  curses.flushinp() # this is used to clear the input in case the user types something during time.sleep
  global name
  name=input()#takes the input
  print("hi " + name)
  time.sleep(2)#waits for a sec
  os.system("clear")#clears screen

  ###ask the user their hobby is###
  printQuestion("What do you like to do?(Type your answer then press enter)\n")
  curses.flushinp()
  global hobby
  hobby=input()
  print("cool")
  time.sleep(2)
  os.system("clear")

  ###ask the user who supports them###
  printQuestion("Who supports you?(Type your answer then press enter)\n")
  curses.flushinp()
  global support
  support=input()
  support=support.replace("my", "")
  time.sleep(2)
  os.system("clear")

  print("Alright, let's start! \n") 
askPersonalQuestions()


#################Finish function###############
##exectcuted when the game is finished###(flashing thanks for playing)
def finish():
  #multi line variable of what to show at end of game
  end="""

█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░░░░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███
█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░░░░░░░░░▄▀░░████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███████████░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░░░█░░░░░░░░░░▄▀░░████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█
█████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█
█████░░░░░░█████░░░░░░██░░░░░░█░░░░░░██░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░█████░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█
█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░█████░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░███████░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░░░░░█░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███████░░▄▀░░█████████░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░█
█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███████░░▄▀░░█████████░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████████
█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░█
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░███████░░░░░░███████░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 

Great Job """+name+"🙂!"
  #While loop to print the end string in flashing colors
  while True:
    #print red, wait a sec
    print(colors.fg.red, end)
    time.sleep(0.3)
    os.system("clear")
    #print blue, wait a sec
    print(colors.fg.blue, end)
    time.sleep(0.3)
    os.system("clear")
    #print green, wait a sec
    print(colors.fg.green,end)
    time.sleep(0.3)
    os.system("clear")

#################Flash Red function###############
##Flashes the str red
def flashRed(str):
  #flash it 3 times
  for x in range(3):
    #print the string, wait a sec, clear(flash effect)
    print(colors.fg.red, str)
    time.sleep(0.2)
    os.system("clear")
    time.sleep(0.2)

#################Flash Green function###############
##Flashes the str green
def flashGreen(str):
  #flash it 3 times
  for x in range(3):
    #print the string, wait a sec, clear(flash effect)
    print(colors.fg.green, str)
    time.sleep(0.2)
    os.system("clear")
    time.sleep(0.2)


##############################################
#############Adventure Function###############
##############################################
## - very important function. 
## - adventure game
def adventure():
  #############Options dictionary###############
  ##Dictionary with all the data for the game


  #Start:
  ###**##//**##**##//**##**##//**##**##//**##**##//**
  ##**##//**##**##//**##**##//**##**##//**##**##//**
  options = {
    ##option 1
    "1": "You go to the pool. You see the other kids climb the long ladder. They spread their arms and bend their knees. Then they jump and fall down, down, down landing with a splash!\n Press 1 to: Get in line for the diving board\n Press 2 to: Rest for a bit first", 
    #A dictionary with what you can do after option 1:
    "options1":{
      "1": "You go to the diving board. \n Press 1 to: Start climbing up the ladder \n Press 2 to: Let the other kids go first",
      "options1": {
        #Start Climbing
        "1": "You start climbing first. You get to the top and walk to the end of the board. It is very tall. You get to the end of the board \n Press 1 to: Jump of the diving board\n Press 2 to: Go down and stretch",
        "options1": {
          
          "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
          "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun"},
          
          "2": "You go down and stretch.\n Press 1 to:jump\n Press 2 to: Go home instead",
          "options2":{
            
            "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun"},

            "2": "You go home and " + hobby + " instead!"
          }
        },

        #Let the other kids go first
        "2": "You let the other kids go first.\n Press 1 to: Start climbing the ladder\n Press 2 to: Go home instead",
        "options2": {
          #Start Climbing
          "1": "You start climbing first. You get to the top.\n Press 1 to: Jump off the diving board\n Press 2 to: Go down and stretch first",
          "options1": {
            
            "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: go and jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
            
            "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: Go home instead",
            "options2":{
              
              "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
        
              "2": "You go home and "+ hobby + " instead!"
            }
          },
          "2":"You go home and "+ hobby + " instead!"
  }
      },

      "2":"You rest for a bit.\n Press 1 to: Go to the diving board\n Press 2 to: Go home instead",
      "options2": {
        "1": "You go to the diving board.\n Press 1 to: Start climbing the ladder\n Press 2 to: Let the other kids go first",
        "options1": {
        #Start Climbing
        "1": "You start climbing first. You get to the top.\n Press 1 to: jump\n Press 2 to: go down and stretch",
        "options1": {
          
          "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
          "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
          
          "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: go home",
          "options2":{
            
            "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},

            "2": "You go home and "+ hobby + " instead!"
          }
        },

        #Let the other kids go first
        "2": "You let the other kids go first.\n Press 1 to: Start climbing the ladder\n Press 2 to: Go home instead",
        "options2": {
          #Start Climbing
          "1": "You start climbing. You get to the top.\n Press 1 to: to jump\n Press 2 to: go down and stretch",
          "options1": {
            
            "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to:jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
            
            "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: go home",
            "options2":{
              
              "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"}, 
        
              "2": "You go home and "+ hobby + " instead!"
            }
          },
          "2":"You go home and "+ hobby + " instead!"
  }
      },

        "2":"You go home and "+ hobby + " instead!"
      }
    },

    #option 2
    "2": "You decide to go home. Then the next day you wake up feeling much better.\n Press 1 to: go the pool\n Press 2 to: stay home",
    #A dictionary with everything you can do from option 2
    "options2":{
      "1": "You go to the pool. You see the other kids climb the long ladder. They spread their arms and bend their knees. Then they jump and fall down, down, down landing with a splash!\n Press 1 to: Get in line for the diving board\n Press 2 to: Rest for a bit first",
      "options1":{
        "1": "You go to the diving board. \n Press 1 to: Start climbing up the ladder \n Press 2 to: Let the other kids go first",
        "options1": {
          #Start Climbing
          "1": "You start climbing first. You get to the top and walk to the end of the board. It is very tall. You get to the end of the board \n Press 1 to: Jump of the diving board\n Press 2 to: Go down and stretch",
          "options1": {
            
            "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun"},
            
            "2": "You go down and stretch.\n Press 1 to:jump\n Press 2 to: Go home instead",
            "options2":{
              
              "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun"},

              "2": "You go home and " + hobby + " instead!"
            }
          },

          #Let the other kids go first
          "2": "You let the other kids go first.\n Press 1 to: Start climbing the ladder\n Press 2 to: Go home instead",
          "options2": {
            #Start Climbing
            "1": "You start climbing first. You get to the top.\n Press 1 to: Jump off the diving board\n Press 2 to: Go down and stretch first",
            "options1": {
              
              "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: go and jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
              
              "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: Go home instead",
              "options2":{
                
                "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to: jump again",
                "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
          
                "2": "You go home and "+ hobby + " instead!"
              }
            },
            "2":"You go home and "+ hobby + " instead!"
    }
        },

        "2":"You rest for a bit.\n Press 1 to: Go to the diving board\n Press 2 to: Go home instead",
        "options2": {
          "1": "You go to the diving board.\n Press 1 to: Start climbing the ladder\n Press 2 to: Let the other kids go first",
          "options1": {
          #Start Climbing
          "1": "You start climbing first. You get to the top.\n Press 1 to: jump\n Press 2 to: go down and stretch",
          "options1": {
            
            "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
            "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
            
            "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: go home",
            "options2":{
              
              "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},

              "2": "You go home and "+ hobby + " instead!"
            }
          },

          #Let the other kids go first
          "2": "You let the other kids go first.\n Press 1 to: Start climbing the ladder\n Press 2 to: Go home instead",
          "options2": {
            #Start Climbing
            "1": "You start climbing. You get to the top.\n Press 1 to: to jump\n Press 2 to: go down and stretch",
            "options1": {
              
              "1": "You " +jump +"!\n Press 1 to: tell your "+ support +" everything\n Press 2 to:jump again",
              "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"},
              
              "2": "You go down and stretch.\n Press 1 to: jump\n Press 2 to: go home",
              "options2":{
                
                "1": "You " +jump +"!\n Press 1 to: Do you want to tell your "+ support +" everything\n Press 2 to: jump again",
                "options1":{"1":"You tell your "+ support +" everything! Your"+support+"is so proud of you!", "2":"You " +jump +" again! That was so much fun!"}, 
          
                "2": "You go home and "+ hobby + " instead!"
              }
            },
            "2":"You go home and "+ hobby + " instead!"
    }
        },

          "2":"You go home and "+ hobby + " instead!"
        }
      },

      "2":"You go home and " + hobby + " instead.",
    }

  }

  #End:
  ###**##//**##**##//**##**##//**##**##//**##**##//**
  ##**##//**##**##//**##**##//**##**##//**##**##//**

  

  #the variable lst will be updated when the user makes a choice
  lst=options
  
  ##############################################
  ##While loop. loops through the options dictionary
  ##user can make choices, until end of adventure game
  
  while True:
    ##Print the first question if it is the first time:
    if lst==options:
      printQuestion("You have been practicing swimming a lot, and you want to practice jumping. \n Press 1 to: Go to the pool \n Press 2 to: stay at home\n \n(Press E to exit)\n")
    
    #Flush the input and get the user's input
    curses.flushinp()
    choice=input()

    #If the answer is invalid
    if choice != "1" and choice !="2" and choice !="e" and choice != "E":

      #invalid message
      print(colors.fg.red, "Sorry, that is invalid...try again")
      print(colors.off, "")
      time.sleep(2)
      os.system("clear")

      #re-print the question so the user can try again
      if lst!=options:
        print(lst)
        print("(Press E to exit) \n")
      continue



    # If the user presses E, exits the game
    if choice=="e" or choice=="E":
      break



    # If you get to the end of the game:
    if not ("options"+str(choice)) in lst:
      #print the final answer
      print(lst[choice])
      #print the end!
      print(colors.fg.green, "\nThe End! Great job "+name+"!", colors.off, "")
      time.sleep(3)
      os.system("clear")
      #end game
      break
    ##
    #After each iteration, Print the next question and update the list

    #clear iteration
    print("\n")
    os.system("clear")
    #print next question
    printQuestion(lst[choice]+" ")
    printQuestion("(Press E to exit) \n")
    lst=lst["options"+str(choice)] # update list

  #Once the game is finished, take the user back to the menu!
  menu()


##############################################
################Quiz Function#################
##############################################
## - very important function. 
## - quiz about the book
def quiz():
  score=0 #set the score to zero

  #audio files
  correct=["correct1.mp3", "correct2.mp3", "correct3.mp3"]
  wrong=["wrong1.mp3", "wrong2.mp3"]

  # This loops through the list of questions
  for x in range(0, len(questions)-1):

    start=time.time()#set start time
    firstTry=True #intially it is the user's first try

    #Loops through the same question until the user gets it correct
    while True:
      #prints the quesiton
      printQuestion(questions[x]["Question"])
      printQuestion("(Press E to exit) \n")
      print(colors.fg.green, "Your current score is: "+str(score)+"! \n You get 3 points if you are correct on the first try, and 1 point if you are correct after the first try")
      print(colors.off, "")

      #clears the input
      curses.flushinp()
      userAns=input()
      os.system("clear")

      # checks if user wants to exit the game
      if userAns=="e" or userAns=="E":
        menu()

      # Checks if the user gets the correct answer
      if userAns==questions[x]["Answer"]:

        end=time.time() #stop the timer
        #flash correct
        flashGreen(correctAnswers[random.randint(0,3)])
        #sound correct sound
        os.system('afplay '+ correct[random.randint(0,2)])
        #tell user amount of time taken
        print(colors.fg.green,"You took "+str(round(end-start)) + " seconds to answer question!", colors.off, "")
        time.sleep(2)
        os.system("clear")
        
        #calculates the score
        if firstTry==True:
          score=score+3
        else:
          score=score+1

        # Extra text for question 6
        if x==6: 
          printQuestion("\n Many places do not have clean water. There aren't enough resources to clean the water. \n")
        break

      #Checks if the user gets the wrong answer(including invalid)
      else:
        #flashes incorrect
        flashRed(wrongAnswer[random.randint(0,0)])
        #plays wrong sound
        os.system('afplay '+ wrong[random.randint(0,1)])
        #no longer first time
        firstTry=False

      #clears the screen
      os.system("clear")
      
  #Prints final score
  print(colors.fg.green, "Your final score is "+str(score)+"! Great Job! The highest score is 27")
  print(colors.off,"")
  #returns to menu
  menu()

##############################################
################Menu Function#################
##############################################
##-menu with choice to go to quiz/adventure/finish
def menu():
  #clear input
  curses.flushinp()
  print(colors.fg.green, "Press A: play an adventure:\n Press Q: play a quiz\n Press F: Finished \n \n", colors.off, "")
  start=input()# get input

  #Choose an option...until valid
  while True:

    #Adventure option#
    if start=="A" or start=="a":
      os.system("clear")
      adventure() #call adventure function
      break

    #Quiz option
    elif start=="Q" or start=="q":
      os.system("clear")
      quiz() #call quiz function
      break

    #Finish option
    elif start=="f" or start=="F":
      #double check the user wants to finish
      curses.flushinp()
      checkIfFinish=input("Press y if you want to finish, Type anything else to go back to menu: \n")
      if checkIfFinish != "y" and checkIfFinish != "Y":
        #if the user actually doesn't want to finish
        menu()
      # if the user wants to finish
      finish()
      break

    #Invalid Option
    else:
      os.system("clear")
      curses.flushinp()
      #if answer is invalid
      start=input("❗ Sorry, that was invalid. \n Press a: play an adventure: \n Press q: play a quiz\n Press F: Finished\n \n")

##These are the functions that are called for the game to start
menu()
