import tkinter
from math import *
from time import sleep

g=1

l1 = 100
l2 = l1

teta1 = pi/2.5
teta2 = pi/6

w1 = 0
w2 = 0

acc1 = 0.0
acc2 = 0.0

origin_x = 345
origin_y = 245
origin_size = 20

first_masse_x = origin_x + l1 * sin(teta1) 
first_masse_y = origin_y + l1 * cos(teta1)
m1 = 0.3

second_masse_x = first_masse_x + l2 * sin(teta2)
second_masse_y = first_masse_y + l2 * cos(teta2)
m2 = 0.3

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
        cir1=c.create_oval(first_masse_x-m1*100/2,first_masse_y-m1*100/2,first_masse_x+m1*100/2,
                        first_masse_y+m1*100/2,fill='blue')
        #second masse
        cir2=c.create_oval(second_masse_x-m2*100/2,second_masse_y-m2*100/2,second_masse_x+m2*100/2
                        ,second_masse_y+m2*100/2,fill='blue')


        line2=c.create_line(first_masse_x,first_masse_y,second_masse_x,second_masse_y,fill='white')

        pretty_line = c.create_line(second_masse_x,second_masse_y,prev_sec_masse_x,prev_sec_masse_y,fill='green',width=3)
        prev_sec_masse_x = second_masse_x
        prev_sec_masse_y = second_masse_y

        num1= (-g) * (2*m1*3+m2*3)*sin(teta1)
        num2=(-m2*3)*g*sin(teta1-2*teta2)
        num3= (-2)*sin(teta1-teta2)*m2*3*(w2*w2*l2+w1*w1*l1*cos(teta1-teta2))
        den= l1*(2*m1*3+m2*3-m2*3*cos(2*teta1-2*teta2))
        acc1 = (num1+num2+num3)/den

        num1=2*sin(teta1-teta2)
        num2=w1*w1*l1*(m1+m2)*3
        num3=g*3*(m1+m2)*cos(teta1)
        num4=w2*w2*l2*m2*3*cos(teta1-teta2)
        den=den*l2/l1
        acc2 = (num1*(num2+num3+num4))/den

        w1 += acc1
        w2 += acc2

        teta1 += w1
        teta2 += w2

        first_masse_x = origin_x + l1 * sin(teta1)
        first_masse_y = origin_y + l1 * cos(teta1)

        second_masse_x = first_masse_x + l2 * sin(teta2)
        second_masse_y = first_masse_y + l2 * cos(teta2)
        c.update()
        sleep(0.02)
        c.delete(line1,line2,cir1,cir2)

window.mainloop()