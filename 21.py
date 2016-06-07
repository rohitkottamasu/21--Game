#21
import random



def game(a):
	if(a==1):
		b=int(raw_input("Enter a number:"))
		if(b!=1 and b<6):
			print("6")
			game(a)
		elif(b!=6 and 6<b<11):
			print("11")
			game(a)
		elif(b!=11 and 11<b<16):
			print("16")
			game(a)
		elif(b!=16 and 16<b<21):

			print("21")
			d=1
			
		elif(b==1 or b==6 or b==11 or b==16):
			b=b+1
			print(b)
			game(a)
	else:
		print("1")
		a=1
		game(a)

	if(d==1):
		print("computer wins")
	else:
		print("You win")



list1=["1","2","3","4","5","6"]
a=random.choice(list1)
a=int(a)
print("1.odd")
print("2.Even") 
c=int(raw_input("Enter your choice:"))
b=int(raw_input("Enter the number for toss:"))


def win(c):
	if(c==21):
		print("You win")
	elif(c!=21 and c>16):
		print("computer wins")	
		

if((a+b)%2==0):
	if(c==1):
        	print("Computer starts first")
		game(0)
	else:
		print("You start")
		game(1)
if((a+b)%2!=0):
	if(c==2):
		print("Computer starts first")
		game(0)
	else:
		print("You start")
		game(1)







