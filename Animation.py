import sys
from Tkinter import *
from PIL import ImageTk, Image


 
centers=[]
window= Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
C = Canvas(window, bg="gray",cursor="fleur", height=h, width=w)

def callback(event):
	global centers
	print "clicked at", event.x, event.y
	boids(event.x,event.y)
	print len(centers)


def boids(x,y):
	global C
	r=5
	centers.append((x,y))
	for center in centers:
		C.create_oval(center[0]-r,center[1]-r,center[0]+r,center[1]+r ,fill="black",outline="green")


window.title("Welcome to LikeGeeks app")
window.geometry("%dx%d+0+0" % (w,h))

window.title("STARLING MURMURATION")

coord = 10, 50, 240, 210 ,0,0

C.pack()
C.bind("<Button-1>", callback)


window.configure(background='white')

window.mainloop()
