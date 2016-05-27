import random as rnd

def arrange():
	get_choice = { 0:"SHEEP",1:"GOLD",2:"SHEEP" }
	seq = []
	list = [0,1,2]
	rnd.shuffle(list)
	for i in list:
		seq.append(get_choice.get(i))
	return seq

def to_show(choice,seq,key):
	list = []
	for i in range(3):
		if ( seq[i] != "GOLD" ):
			list.append(i)
	for i in list:
		if ( choice[i] == ' ' and i != key ):
			choice[i] = "SHEEP"
			break
	return choice

def show_final(choice,seq):
	for i in range(3):
		choice[i] = seq[i]
	return choice

if ( __name__ == "__main__" ):
	seq = arrange()
