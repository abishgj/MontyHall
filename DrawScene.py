import Tkinter as tk

def rect():
	global top
	frame = tk.Frame(top,width=550,height=350)
	frame.pack()
	can = tk.Canvas(frame,bg="white",height=300,width=500)
	rect1 = can.create_rectangle(50,50,150,250,fill="black")
	var = "A"
	lab1 = tk.Label(can,textvariable=var,anchor="center")
	rect2 = can.create_rectangle(200,50,300,250,fill="black")
        rect3 = can.create_rectangle(350,50,450,250,fill="black")
	#print rect1,rect2,rect3
        can.pack()
	return frame

def draw():
	global top
	top = tk.Tk()
	top.title("Monty Hall Game")
	top.resizable(0,0)
	frame = tk.Frame(top,width=550,height=350)
	frme = rect()
	type(frme)
	top.mainloop()

if ( __name__ == "__main__" ):
	draw()
