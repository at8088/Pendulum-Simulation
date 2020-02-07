import tkinter
from math import *
from time import sleep

g=9.81

l1 = 50+75
l2 = l1

teta1 = pi-0.0002
teta2 = 0.0

w1 = 0
w2 = 0

acc1 = 0.0
acc2 = 0.0

origin_x = 345
origin_y = 245
origin_size = 20

first_masse_x = origin_x + l1 * sin(teta1)
first_masse_y = origin_y + l1 * cos(teta1)
first_masse_size = 0.3

second_masse_x = first_masse_x + l2 * sin(teta2)
second_masse_y = first_masse_y + l2 * cos(teta2)
second_masse_size = 0.3

prev_sec_masse_x = second_masse_x
prev_sec_masse_y = second_masse_y

window = tkinter.Tk()
window.title("Pendule Double")
window.resizable(width=False,height=False)
window.geometry("700x600")
c = tkinter.Canvas(window,width=700,height=600,bg='black')
c.pack()
c.create_oval(origin_x-origin_size/2,origin_y-origin_size/2,origin_x+origin_size/2,origin_y+origin_size/2,fill='red')


while True:

        line1=c.create_line(origin_x,origin_y,first_masse_x,first_masse_y,fill='white')

        #first masse
        cir1=c.create_oval(first_masse_x-first_masse_size*100/2,first_masse_y-first_masse_size*100/2,first_masse_x+first_masse_size*100/2,
                        first_masse_y+first_masse_size*100/2,fill='blue')
        #second masse
        cir2=c.create_oval(second_masse_x-second_masse_size*100/2,second_masse_y-second_masse_size*100/2,second_masse_x+second_masse_size*100/2
                        ,second_masse_y+second_masse_size*100/2,fill='blue')


        line2=c.create_line(first_masse_x,first_masse_y,second_masse_x,second_masse_y,fill='white')

        pretty_line = c.create_line(second_masse_x,second_masse_y,prev_sec_masse_x,prev_sec_masse_y,fill='green',width=3)
        prev_sec_masse_x = second_masse_x
        prev_sec_masse_y = second_masse_y

        w1 += acc1
        w2 += acc2

        teta1 += w1
        teta2 += w2

        acc1 = (-g*(2*first_masse_size+second_masse_size)*sin(teta1)-second_masse_size*g*sin(teta1-2*teta2)-2*sin(teta1-teta2)*second_masse_size*((w2*w2) * l2 + w1**2 *l1*cos(teta1-teta2)))/ (l1*(2*first_masse_size+second_masse_size-second_masse_size*cos(2*teta1 - 2*teta2)))

        acc2 = (2*sin(teta1-teta2)*((w1**2) * l1 *(second_masse_size+first_masse_size)+g*(second_masse_size+first_masse_size)*cos(teta1)+ (w2**2 )* l2 *second_masse_size*cos(teta1-teta2)))/(l2*(2*first_masse_size+second_masse_size-second_masse_size*cos(2*teta1-2*teta2)))

        first_masse_x = origin_x + l1 * sin(teta1)
        first_masse_y = origin_y + l1 * cos(teta1)

        second_masse_x = first_masse_x + l2 * sin(teta2)
        second_masse_y = first_masse_y + l2 * cos(teta2)
        c.update()
        sleep(0.01)
        c.delete(line1,line2,cir1,cir2)

window.mainloop()