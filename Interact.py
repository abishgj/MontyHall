import re
import os
import sys
import Draw
import MontyH

def init():
	Draw.display(choice)
	seq_list = MontyH.arrange()
	return seq_list

def eval_input(char):
	trans_list = { 'A':0, 'B':1, 'C':2 }
	if ( re.match(r'[A-C]',char) == None ):
		return -1
	else:
		return trans_list.get(char)

def read_in():
	while True:
                x = raw_input("Which block do you want to select ?(Provide your option as A or B or C)")
                key = eval_input(x)
                if ( key == -1 ):
                        continue
                else:
                        return key
                        break

def disclose(key):
	global choice
	choice = MontyH.show_final(choice,seq)
	Draw.display(choice)
	if ( seq[key] == "GOLD" ):
		print "Woohoooo!! Congrats"
	else:
		print "Thank you for playing"

def game_run():
	global choice
	choice = { 0:" ",1:" ",2:" " }
	global seq
	os.system('clear')
	print "Welcome to The Monty Hall Show!!"
	print "There are three blocks named 'A', 'B' and 'C'\n"
	dum = raw_input("")
	print "There are three objects behind the blocks, but only one of the object is precious!!\n"
	dum = raw_input("")
	print "First you have to choose a block, then I ( Monty Hall) am going to show you one of the block where the non-precious object is present leaving you another chance of whether to switch or stick\n"
	dum = raw_input("")
	print "You have all freedom to either switch or stick to your first choice\n"
	dum = raw_input("")
	print "Shall we start the game then\n"
	dum = raw_input("")
	seq = init()
	key = read_in()
	dum = raw_input("Well.. You have made a choice.. Now you'll see a sheep block among the other two which you did not choose.. Again you will be given a chance of choice between the rest.. Lets see it")
	choice = MontyH.to_show(choice,seq,key)
	Draw.display(choice)
	x = raw_input("Do you want to switch your choice ?( Y for yes and any other key to continue with the same choice )")
	if ( x == 'Y' ):
		key = read_in()
		disclose(key)
	else:
		disclose(key)

if ( __name__ == "__main__" ):
	game_run()
