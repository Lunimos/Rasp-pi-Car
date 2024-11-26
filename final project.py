#elliot ross-hamond
#ec1861152

import RPi.GPIO as GPIO
import time
import curses



screen = curses.initscr()
curses.noecho()
screen.keypad(True)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
#gpio setup keys so power going to right gpio





try:
  while True:
    char = screen.getch()
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)
    
    if char == ord ('q'):
      break


    elif char == curses.KEY_UP:
      print ("Forward")
      GPIO.output(7,True)
      GPIO.output(13,True)
      #makes the buggy go forward

    elif char == curses.KEY_RIGHT:
      print ("Right")
      GPIO.output(7,True)
        #makes the buggy go right

    elif char == curses.KEY_DOWN:
      print("Backwards")
      GPIO.output(11,True)
      GPIO.output(15,True)
    #used to make buggy go backwards

    elif char == curses.KEY_LEFT:
      print ("Left")
      GPIO.output(13,True)
        #used to make buggy go left

    
        
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo(); curses.endwin()

