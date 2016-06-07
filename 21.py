#21 The game
# Harshit's Fork from Rohit
import random
import os
import time
comp_num = 0
total = 0
numbers = ["1","2","3","4","5","6"]

def printtot():
	print("CURRENT TOTAL = %d" % total)

def initialize():
	b = 0
	c = 0
	player = 0
	d = 0
	comp_num = 0

def win(tot,pl):
	if(tot==21 and pl==0):
		print("\n\nGame ends...\nResult:- Computer WINS")
		quit()
	elif(tot==21 and pl==1):
		print("\n\nGame ends...\nResult:- User WINS")
		quit()
		
def switch_player(curr):
	if(curr == 0):
		game(1)
	elif(curr == 1):
		game(0)


#Player0 = Computer
#Player1 = User
def game(player):
	global total
	if(player == 1):
	#User plays
		b = int(raw_input("Enter your number=> "))
		if(total+b > 21):
			print("INVALID NUMBER! Total exceeds 21 already.")
			b = int(raw_input("Re-enter your number=> "))
		if(b>6):
			print("INVALID NUMBER! Can use only 1 to 6.")
			b = int(raw_input("Re-enter your number=> "))			
		total += b
		printtot()
		win(total,player)
		switch_player(player)
	elif(player == 0):
	#Computer plays
		time.sleep(1.5)
		if(total<6):
			comp_num = 6-total
			print("Computer plays %d." % comp_num)
			total += comp_num
			printtot()
			win(total,player)
			switch_player(player)
		elif(total<11):
			comp_num = 11-total
			print("Computer plays %d." % comp_num)
			total += comp_num
			printtot()
			win(total,player)
			switch_player(player)
		elif(total<16):
			comp_num = 16-total
			print("Computer plays %d." % comp_num)
			total += comp_num
			printtot()
			win(total,player)
			switch_player(player)
		elif(total<21):
			comp_num = 21-total
			print("Computer plays %d." % comp_num)
			total += comp_num
			printtot()
			win(total,player)
			switch_player(player)		
		else:
			comp_num = 1
			print("Computer plays %d." % comp_num)
			total += comp_num
			printtot()
			win(total,player)
			switch_player(player)	
			
	else:
		print("The game has encountered an internal error. Force exitting...")
		quit()


#Executing statements start from here
initialize()
print "Let's have an odd-even toss !!!"
time.sleep(1.5)
print("1.Odd")
print("2.Even") 
c = int(raw_input("Enter your choice:- "))
usrnum = int(raw_input("Enter your number for the toss:- "))
compnum = int(random.choice(numbers))
print("Computer chose the number %d for the toss" % compnum)
if((compnum+usrnum)%2==0):
	if(c==1):
        	print("COMPUTER won the toss and begins...")
		game(0)
	else:
		print("PLAYER won the toss and begins...")
		game(1)
else:
	if(c==2):
		print("COMPUTER won the toss and begins...")
		game(0)
	else:
		print("PLAYER won the toss and begins...")
		game(1)
