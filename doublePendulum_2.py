#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:59:37 2021

@author: yz3259
"""

import tkinter as tk
import numpy as np
import time
from scipy.integrate import odeint


w = 1800
h = 1200

r1 = 80
r2 = 80

m1 = 10
m2 = 5

xf, yf = (w//2, 600//3.2)

A1, A2 = (95.0,-30.0)

v1 = 0
v2 = 0

a1 = 0
a2 = 0

g = 10.0

flag = False

def create_circle(x, y, r, canvasName,col = "black"): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=col,outline=col)

# def dA_dt(A):
#     ang1, ang2,v1,v2,a1,a2 = A

#     num1 = -g*(2*m1+m2)*np.sin(ang1)
#     num2 = -m2*g*np.sin(ang1-2*ang2)
#     num3 = -2*np.sin(ang1-ang2)*m2
#     num4 = v2**2*r2+v1**2*r1*np.cos(ang1-ang2)
#     den = r1*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
#     a1 = (num1+num2+num3*num4)/den

#     num1 = 2*np.sin(ang1-ang2)
#     num2 = v1**2*r1*(m1+m2)
#     num3 = g*(m1+m2)*np.cos(ang1)
#     num4 = v2**2*r2*m2*np.cos(ang1-ang2)
#     den = r2*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
#     a2 = num1*(num2+num3+num4)/den
#     print(a1)
#     print(a2)


#     return np.array([ang1,ang2, v1,v2,a1,a2])


def funt(y):
    ang1 = y[0]
    ang2 = y[1]
    v1 = y[2]
    v2 = y[3]


    num1 = -g*(2*m1+m2)*np.sin(ang1)
    num2 = -m2*g*np.sin(ang1-2*ang2)
    num3 = -2*np.sin(ang1-ang2)*m2
    num4 = v2**2*r2+v1**2*r1*np.cos(ang1-ang2)
    den = r1*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
    a1 = (num1+num2+num3*num4)/den

    num1 = 2*np.sin(ang1-ang2)
    num2 = v1**2*r1*(m1+m2)
    num3 = g*(m1+m2)*np.cos(ang1)
    num4 = v2**2*r2*m2*np.cos(ang1-ang2)
    den = r2*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
    a2 = num1*(num2+num3+num4)/den

    dydt = np.zeros(4)

    dydt[0] = v1
    dydt[1] = v2
    dydt[2] = a1
    dydt[3] = a2

    return dydt

def rk4(A,h):
  # print(x0.shape)
  #print(A.shape)
  k1 = funt(A)
  k2 = funt(A+h*k1/2)
  k3 = funt(A+h*k2/2)
  k4 = funt(A+h*k3)

  y1 = A + h*(k1+2*k2+2*k3+k4)/6

  #x0,A = t1,y1

  return  y1

# def rk4(x,y,h):
#     k1 = funt(x,y)
#     x1 = x+ k1[0]*h/2
#     y1 = y + k1[1]*h/2
#     k2 = funt(x1,y1)
#     x2 = x1+ k2[0]*h/2
#     y2 = y1 + k2[1]*h/2
#     k3 = funt(x2, y2)
#     x3 = x2+ k3[0]*h
#     y3 = y2 + k3[1]*h
#     k4 = funt(x3,y3)
#     return [x+h*(k1[0]+k2[0]*2+k3[0]*2+k4[0])/6,y+h*(k1[1]+k2[1]*2+k3[1]*2+k4[1])/6]

root = tk.Tk()
root.title("Double Pendulum")
root.geometry("1200x1200")

choice = tk.Frame(root,width = 1000//3, height = 1000//3, bd = 0,bg = "ivory")
choice.grid(row=0,column = 0,padx = 5, pady =5)


graph = tk.Frame(root,width = 1000//3, height = 1200//3, bd = 0)
graph.grid(row=0,column = 1,padx=5,pady = 5)

#graph2 = tk.Frame(root,width = 1000, height = 1000,bd=0)
#graph2.grid(row=1,column=0,padx = 25, pady = 10)

labe1 = tk.Label(graph, text = "Double Pendulum Movement",font = ('arial', 14, 'bold')).grid(row=0,column=0)
my_canvas = tk.Canvas(graph,width =w, height =h+10, bg = "ivory")
my_canvas.grid(row=1,column=0,padx = 5,pady=5)

labe2 = tk.Label(graph, text = "Pendulum 1: ",font = ('arial', 14, 'bold')).grid(row=2,column=0)
labe3 = tk.Label(graph,text = "angle",font = ('arial', 14, 'bold'),fg = 'gray').grid(row=3,column=0)
labe3 = tk.Label(graph,text = "angular velocity",font = ('arial', 14, 'bold'),fg = 'coral').grid(row=4,column=0)

track_canvas = tk.Canvas(graph,width =w, height = h//2-20, bg = "ivory")
track_canvas.grid(row=5,column=0,padx=5,pady=5)

#labe2 = tk.Label(graph2, text = "Pendulum 2- angle and angular velocity",font = ('arial', 14, 'bold')).grid(row=4,column=0)
#track_canvas2 = tk.Canvas(graph2,width =w, height = h//2-20, bg = "ivory")
#track_canvas2.grid(row=0,column=0,padx=20,pady=10)

#flag = False
def slide():
    global line1,line2,circle1,circle2
    #my_label = tk.Label(choice,text=angle1.get())
    #my_label.grid(row=6,column=1)
    A1 = angle1.get()
    A2 = angle2.get()

    m1 = mass1.get()
    m2 = mass2.get()

    r1 = rod1.get()
    r2 = rod2.get()

    v1 = 0
    v2 = 0

    a1 = 0
    a2 = 0

    g = 10.0
    ang1 = np.pi*A1/180
    ang2 = np.pi*A2/180
    t = 0
    A = np.array([ang1,ang2,v1,v2])
    track_canvas.delete("all")
    my_canvas.delete("all")
    flag = True
    while flag:
        # num1 = -g*(2*m1+m2)*np.sin(ang1)
        # num2 = -m2*g*np.sin(ang1-2*ang2)
        # num3 = -2*np.sin(ang1-ang2)*m2
        # num4 = v2**2*r2+v1**2*r1*np.cos(ang1-ang2)
        # den = r1*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
        # a1 = (num1+num2+num3*num4)/den

        # num1 = 2*np.sin(ang1-ang2)
        # num2 = v1**2*r1*(m1+m2)
        # num3 = g*(m1+m2)*np.cos(ang1)
        # num4 = v2**2*r2*m2*np.cos(ang1-ang2)
        # den = r2*(2*m1+m2-m2*np.cos(2*ang1-2*ang2))
        # a2 = num1*(num2+num3+num4)/den




       # print(V)
        x1 = r1*np.sin(A[0])+ xf
        y1 = r1*np.cos(A[0]) + yf

        x2 = x1+r2*np.sin(A[1])
        y2 = y1+r2*np.cos(A[1])
        # Create line

    #    my_canvas.delete("all")
        my_canvas.delete(line1,line2,circle1,circle2)
        line1 = my_canvas.create_line(xf,yf,x1,y1,fill = "black",width=4)
        circle1 = create_circle(x1,y1,m1,my_canvas,col = "black")

        # second pendulum
        line2 = my_canvas.create_line(x1,y1,x2,y2,fill = "black",width = 4)
        circle2 = create_circle(x2,y2,m2,my_canvas,col = "black")

        create_circle(x2,y2,1,my_canvas,col="skyblue")

       # v1 += a1
       # v2 += a2

       # ang1 += v1
       # ang2 += v2

       # v1 *=0.999
       # v2 *=0.999


        #my_canvas.delete(line1,line2,circle1,circle2)
        create_circle(t,180.0*(A[0])/np.pi+ h//4-10,1,track_canvas,col="gray")
        create_circle(t,180.0*A[2]/np.pi+h//4-10,1,track_canvas,col="coral")
       # create_circle(t,180.0*(ang1)/np.pi+ h//4-10,2,track_canvas2,col="gray")
       # create_circle(t,180.0*v1/np.pi+h//4-10,2,track_canvas2,col="coral")

        #print(v1)

        step = 0.1
        t += step
        #print(t)

        A = rk4(A,step)



        #A[2] = A[2]*0.9991
        #A[3] = A[3]*0.9991

        root.update()

     #   time.sleep(0.01)
    return
 #   flag = True




length_label = tk.Label(choice, text="Angle 1",font = ('arial', 14, 'bold')).grid(row=0, column=0, pady=5, padx = 5)
angle1 = tk.Scale(choice,from_=-360, to =360,font = ('arial', 14, 'bold'),tickinterval= 180,orient = tk.HORIZONTAL,width = 20,length = 200)
angle1.set(A1)
angle1.grid(row=0,column=1,columnspan=10,padx = 5,pady=5)

length_label = tk.Label(choice, text="Angle 2",font = ('arial', 14, 'bold')).grid(row=1, column=0, pady=5, padx = 5)
angle2 = tk.Scale(choice, from_=-360, to =360,font = ('arial', 14, 'bold'),tickinterval= 180,orient = tk.HORIZONTAL,width = 20,length = 200)
angle2.set(A2)
angle2.grid(row=1,column=1,columnspan=10,padx = 5,pady=5)


mass_label = tk.Label(choice, text="Mass 1",font = ('arial', 14, 'bold')).grid(row=2, column=0, pady=5, padx = 5)
mass1 = tk.Scale(choice, from_=0, to =200,font = ('arial', 14, 'bold'),tickinterval= 50,orient = tk.HORIZONTAL,width = 20,length = 200)
mass1.set(m1)
mass1.grid(row=2,column=1,columnspan=100,padx = 5,pady=5)

mass_label = tk.Label(choice, text="Mass 2",font = ('arial', 14, 'bold')).grid(row=3, column=0, pady=5, padx = 5)
mass2 = tk.Scale(choice, from_=0, to =100,font = ('arial', 14, 'bold'),tickinterval= 50,orient = tk.HORIZONTAL,width = 20,length = 200)
mass2.set(m2)
mass2.grid(row=3,column=1,columnspan=10,padx = 5,pady=5)

string_label = tk.Label(choice, text="Rod 1 Length",font = ('arial', 14, 'bold')).grid(row=4, column=0, pady=5, padx = 5)
rod1 = tk.Scale(choice, from_=0, to =200,font = ('arial', 14, 'bold'),tickinterval= 200,orient = tk.HORIZONTAL,width = 20,length = 200)
rod1.set(r1)
rod1.grid(row=4,column=1,columnspan=10,padx = 5,pady=5)

string_label = tk.Label(choice, text="Rod 2 Length",font = ('arial', 14, 'bold')).grid(row=5, column=0, pady=5, padx = 5)
rod2 = tk.Scale(choice, from_=0, to =200,font = ('arial', 14, 'bold'),tickinterval= 200,orient = tk.HORIZONTAL,width = 20,length = 200)
rod2.set(r2)
rod2.grid(row=5,column=1,columnspan=10,padx = 5,pady=5)

my_btn = tk.Button(choice,text="Start", command = slide,padx=10,pady=20,font = ('arial', 14, 'bold'))
my_btn.grid(row=6,column=0, columnspan= 2,padx=5,pady=5)

#btn_clear = tk.Button(choice, text = "Clear track", command=lambda:slide("clear"),padx=10,pady=20,font = ('arial', 14, 'bold'))
#btn_clear.grid(row=6,column = 3)





ang1 = np.pi*A1/180
ang2 = np.pi*A2/180


x1 = r1*np.sin(ang1)+ xf
y1 = r1*np.cos(ang1) + yf

x2 = x1+r2*np.sin(ang2)
y2 = y1+r2*np.cos(ang2)
# # Create line
# # create_line(x1,y1,x2,y2,fill="color")
# #first pendulum
line1 = my_canvas.create_line(xf,yf,x1,y1,fill = "black",width=4)
circle1 = create_circle(x1,y1,m1,my_canvas)

# # second pendulum
line2 = my_canvas.create_line(x1,y1,x2,y2,fill = "black",width=4)
circle2 = create_circle(x2,y2,m2,my_canvas)




root.mainloop()
