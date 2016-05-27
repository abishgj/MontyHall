import os

def display(choice):
	os.system('clear')
	print "\t"+(" ------- \t")*2+" ------- "
	for i in range(2):
		print "\t"+("|\t|\t")*2+"|\t|"
	for i in range(3):
		print "\t",
		if ( choice.get(i) == ' ' ):
			print "|\t|",
		else:
			str = "| "+choice.get(i)+" |" if ( len(choice.get(i)) == 5 ) else "| "+choice.get(i)+"  |"
			print str,
	print ""	
	for i in range(2):
		print "\t"+("|\t|\t")*2+"|\t|"
	print "\t"+(" ------- \t")*2+" ------- "
	print "\t Block_A \t Block_B \t Block_C"
	print "\n\n"

if ( __name__ == "__main__" ):
	choice = { 0:" ",1:" ",2:" " }
	display(choice)
