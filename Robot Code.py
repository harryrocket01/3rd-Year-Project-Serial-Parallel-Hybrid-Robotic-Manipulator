#import board
#import busio
#import adafruit_pca9685
#from adafruit_servokit import ServoKit


#-------------------------IMPORTS---------------------------------------

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import math
import time
import datetime as dt
import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
#import matplotlib.dates as mdates
#import matplotlib.animation as animation
#from matplotlib import style
#from matplotlib.figure import Figure

global TimeLimit
TimeLimit = 100

#i2c = busio.I2C(board.SCL, board.SDA)
#hat = adafruit_pca9685.PCA9685(i2c)
#kit = ServoKit(channels = 16)
#delay = 2

#kit.servo[1].angle=0
Servo1 = 1
Servo2 = 2
Servo3 = 3
Servo4 = 4


#-----------------------CONSTANTS AND GLOBALS---------------------------



#-------------------------TKINTER STYLISATIONS-------------------------
TitleFont = ("Arial",20)
SubFont1 = ("Arial",10)
SubFont2 = ("Arial",5)



class Servo_Info:

    def __init__(self,Number):
        self.ServoNumber = Number
        self.Angle = 0
        self.Offset = 0
        self.Pin =0
        self.Board = 0

    def GetPin(self):
        return self.Pin
    def SetPin(self,value):
        self.Pin = value
    
    def GetOffset(self):
        return self.Offset
    def SetOffset(self,value):
        self.Offset = value

    def GetAngle(self):
        return self.Angle
    def SetAngle(self,value):
        self.Angle = value

    def GetBoard(self):
        return self.Board
    def SetBoard(self,value):
        self.Board = value

    def Turn_Servo(self,value):
        self.SetAngle(value)
        print("Turning servo ",self.Pin," to",self.Angle)

        #kit.servo[self.Pin].angle=self.Angle + self.Offset




#---------------------------------------------Setting Servo info
Full_Servo_Info = []

Servo0 = Servo_Info(0)
Servo0.SetPin(0)
Servo0.SetOffset(0)
Servo0.SetAngle(0)
Servo0.SetBoard(0)
Full_Servo_Info.append(Servo0)

Servo1 = Servo_Info(0)
Servo1.SetPin(1)
Servo1.SetOffset(0)
Servo1.SetAngle(0)
Servo1.SetBoard(0)
Full_Servo_Info.append(Servo1)

Servo2 = Servo_Info(0)
Servo2.SetPin(2)
Servo2.SetOffset(0)
Servo2.SetAngle(0)
Servo2.SetBoard(0)
Full_Servo_Info.append(Servo2)

Servo3 = Servo_Info(0)
Servo3.SetPin(3)
Servo3.SetOffset(0)
Servo3.SetAngle(0)
Servo3.SetBoard(0)
Full_Servo_Info.append(Servo3)

Servo4 = Servo_Info(0)
Servo4.SetPin(4)
Servo4.SetOffset(0)
Servo4.SetAngle(0)
Servo4.SetBoard(0)
Full_Servo_Info.append(Servo4)

Servo5 = Servo_Info(0)
Servo5.SetPin(5)
Servo5.SetOffset(0)
Servo5.SetAngle(0)
Servo5.SetBoard(0)
Full_Servo_Info.append(Servo5)

Servo6 = Servo_Info(0)
Servo6.SetPin(6)
Servo6.SetOffset(0)
Servo6.SetAngle(0)
Servo6.SetBoard(0)
Full_Servo_Info.append(Servo6)

Servo7 = Servo_Info(0)
Servo7.SetPin(7)
Servo7.SetOffset(0)
Servo7.SetAngle(0)
Servo7.SetBoard(0)
Full_Servo_Info.append(Servo7)

Servo8 = Servo_Info(0)
Servo8.SetPin(8)
Servo8.SetOffset(0)
Servo8.SetAngle(0)
Servo8.SetBoard(0)
Full_Servo_Info.append(Servo8)

Servo9 = Servo_Info(0)
Servo9.SetPin(9)
Servo9.SetOffset(0)
Servo9.SetAngle(0)
Servo9.SetBoard(0)
Full_Servo_Info.append(Servo9)

Servo10 = Servo_Info(0)
Servo10.SetPin(10)
Servo10.SetOffset(0)
Servo10.SetAngle(0)
Servo10.SetBoard(0)
Full_Servo_Info.append(Servo10)


#---------------------------MAIN CLASS---------------------------------

class MainWindow(tk.Tk):

    def __init__(self):        
       
        tk.Tk.__init__(self)
        tk.Tk.title(self,"Bio Reactor")
        Window = tk.Frame(self)
     
        Window.pack(side="top", expand = True, fill="both")
        self.Frames={}

        for WindowFrame in (CurrentWindow):
            CurrentFrame = WindowFrame(Window,self)
            self.Frames[WindowFrame] = CurrentFrame
            CurrentFrame.grid(row=0,column=0,sticky="nsew")#
           
        self.Frames[CurrentWindow[0]].tkraise()
       
       
    def Exit(self):
        exit()    
   
    def ShowFrame(self,Pointer):

        CurrentFrame = self.Frames[Pointer]
        CurrentFrame.tkraise()
   
       
#--------------------------------PAGES---------------------------------

class MainMenu(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)

        self.XLable = ttk.Button(self,text="Angle Control",command = lambda:controller.ShowFrame(DirectControl))
        self.XLable.grid(row = 0,column = 0)        

        self.XLable = ttk.Button(self,text="Cart Control:",command = lambda:controller.ShowFrame(CartControl))
        self.XLable.grid(row = 1,column = 0)       

        self.XLable = ttk.Button(self,text="Instruction Set:",command = lambda:controller.ShowFrame(CartControl))
        self.XLable.grid(row = 2,column = 0)     
     
        SubFont1 = ("Arial",14)
       
    

class CartControl(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)



     
        SubFont1 = ("Arial",14)
       
        self.X=tk.DoubleVar()
        self.Y=tk.DoubleVar()
        self.Z=tk.DoubleVar()
        self.Gamma=tk.DoubleVar()
       
        self.x_scale =  ttk.Scale(self,
                                  from_=-200, to=200,
                                  orient=HORIZONTAL,
                                  variable=self.X,
                                  command= lambda x=None:self.Xslider())    
        self.x_scale.grid(row = 0,column = 1)  
       
        self.XLable = ttk.Label(self,text="X value:")
        self.XLable.grid(row = 0,column = 0)        
        self.XValue = ttk.Label(self,text=self.get_current_value_x())
        self.XValue.grid(row = 0,column = 2)            
       
        self.y_scale =  ttk.Scale(self,
                                  from_=-200, to=200,
                                  orient=HORIZONTAL,
                                  variable=self.Y,                                  
                                  command=lambda x=None:self.Yslider())
        self.y_scale.grid(row = 1,column = 1)  
        self.YLable = ttk.Label(self,text="Y value:")
        self.YLable.grid(row = 1,column = 0)  
        self.YValue= ttk.Label(self,text=self.get_current_value_y())
        self.YValue.grid(row = 1,column = 2)          
       
        self.z_scale =  ttk.Scale(self,
                                  from_=-200, to=200,
                                  orient=HORIZONTAL,
                                  variable=self.Z,                                  
                                  command=lambda x=None:self.Zslider())
        self.z_scale.grid(row = 2,column = 1)  
        self.ZLable = ttk.Label(self,text="Z value:")
        self.ZLable.grid(row = 2,column = 0)  
        self.ZValue = ttk.Label(self,text=self.get_current_value_z())
        self.ZValue.grid(row = 2,column = 2)          
       
        self.Gamma_scale =  ttk.Scale(self,
                                  from_=0, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.Gamma,                                  
                                  command=lambda x=None:self.Gammaslider())
        self.Gamma_scale.grid(row = 3,column = 1)  
        self.GammaLable = ttk.Label(self,text="Gamma:")
        self.GammaLable.grid(row = 3,column = 0)  
        self.GammaValue = ttk.Label(self,text=self.get_current_value_Gamma())
        self.GammaValue.grid(row = 3,column = 2)  
       
        self.x_scale.set(210)
        self.y_scale.set(0)                
        self.z_scale.set(120)  
        self.Gamma_scale.set(0)        
       
       
    def Xslider(self):
        self.XValue.configure(text=self.get_current_value_x())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_x(self):
        return '{: .2f}'.format(self.X.get())
   
    def Yslider(self):
        self.YValue.configure(text=self.get_current_value_y())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_y(self):
        return '{: .2f}'.format(self.Y.get())
   
    def Zslider(self):
        self.ZValue.configure(text=self.get_current_value_z())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_z(self):
        return '{: .2f}'.format(self.Z.get())
           
    def Gammaslider(self):
        self.GammaValue.configure(text=self.get_current_value_Gamma())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_Gamma(self):
        return '{: .2f}'.format(self.Gamma.get())            
       

class DirectControl(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)


        self.Angle0=tk.DoubleVar()
        self.Angle1=tk.DoubleVar()
        self.Angle2=tk.DoubleVar()
        self.Angle3=tk.DoubleVar()
        self.Angle4=tk.DoubleVar()
        self.Angle5=tk.DoubleVar()
        self.Angle6=tk.DoubleVar()
        self.Angle7=tk.DoubleVar()
        self.Angle8=tk.DoubleVar()
        self.Angle9=tk.DoubleVar()
        self.Angle10=tk.DoubleVar()

        self.Scale_0 =  ttk.Scale(self,
                                    from_=0, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle0,                                  
                                    command=lambda x=None: Full_Servo_Info[0].Turn_Servo(self.Angle0.get()))
        self.Scale_0.grid(row = 1,column = 1)  
        self.Scale_0 = ttk.Label(self,text="Servo 0:")
        self.Scale_0.grid(row = 1,column = 0)  

        
        self.Scale_1 =  ttk.Scale(self,
                                    from_=0, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle1,                                  
                                    command=lambda x=None: Full_Servo_Info[1].Turn_Servo(self.Angle1.get()))
        self.Scale_1.grid(row = 2,column = 1)  
        self.Scale_1 = ttk.Label(self,text="Servo 1:")
        self.Scale_1.grid(row = 2,column = 0)  

        self.Scale_2 =  ttk.Scale(self,
                                    from_=0, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle2,                                  
                                    command=lambda x=None: Full_Servo_Info[2].Turn_Servo(self.Angle2.get()))
        self.Scale_2.grid(row = 3,column = 1)  
        self.Scale_2 = ttk.Label(self,text="Servo 2:")
        self.Scale_2.grid(row = 3,column = 0)  

        self.Scale_3 =  ttk.Scale(self,
                                    from_=0, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle3,                                  
                                    command=lambda x=None: Full_Servo_Info[3].Turn_Servo(self.Angle3.get()))
        self.Scale_3.grid(row = 4,column = 1)  
        self.Scale_3 = ttk.Label(self,text="Servo 3:")
        self.Scale_3.grid(row = 4,column = 0)  

        self.Scale_4 =  ttk.Scale(self,
                                    from_=0, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle4,                                  
                                    command=lambda x=None: Full_Servo_Info[4].Turn_Servo(self.Angle4.get()))
        self.Scale_4.grid(row = 5,column = 1)  
        self.Scale_4 = ttk.Label(self,text="Servo 4:")
        self.Scale_4.grid(row = 5,column = 0)  
        



    def Xslider(self):
        self.XValue.configure(text=self.get_current_value_x())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_x(self):
        return '{: .2f}'.format(self.X.get())

   
#-------------------------kinimatics-------------------------

class Kinimatics():
   
    def __init__(self):
        self.L1=0
        self.L2=120
        self.L3=120
        self.L4=90
        self.L5=150
        self.L6=150
        self.L7=150
        self.L8=150
       
       
        self.End_Effector = [0,0,0]
       
        self.Theta1 = 0
        self.Theta2 = 0
        self.Theta3 = 0
        self.Theta4 = 0
       
        self.Theta5 = 0
        self.Theta6 = 0
        self.Theta7 = 0
        self.Theta8 = 0
        self.Theta9 = 0
       
        self.DH_Table = [[],[],[],[]]

    def foward_kin(selfServo4,Theta1,Theta2,Theta3,Theta4):
        return 0
   
    def inverse_kin(self,X,Y,Z,Gamma):
       
        return 0
   
    def inverse_kin_main_arm(self,X,Y,Z,Gamma):
        pi = math.pi
        
        Gamma_r = math.radians(Gamma)
   
        Theta1 = math.atan2(Y,Z)

        X_val=X-(math.cos(Theta1)*self.L4*math.cos(Gamma_r))
        Y_val=Y-(math.sin(Theta1)*self.L4*math.cos(Gamma_r))
        Z_val=Z-(self.L4*math.cos(Gamma_r))
       
   
        Beta = math.atan2(Z_val, math.sqrt(Y_val**2+X_val**2))
   
        Phi = math.acos((self.L2**2+Z_val**2+Y_val**2+X_val**2-self.L3**2)/(2*self.L2*math.sqrt(Z_val**2+Y_val**2+X_val**2)))
   
        Theta2 = Beta + Phi

        cTheta3 = (X_val*2+Y_val**2+X_val**2-self.L3**2)/(2*self.L2*math.sqrt(Z_val**2+Y_val**2+X_val**2))
        sTheta3 = math.sqrt(1-cTheta3**2)
        Theta3 = math.atan2(sTheta3,cTheta3)

        Theta4 = Gamma_r-(-Theta2)-Theta3      
       
        self.Theta1=math.degrees(Theta1)
        self.Theta2=math.degrees(Theta2)
        self.Theta3=math.degrees(Theta3)
        self.Theta4=math.degrees(Theta4)
       
        print(X,Y,Z,Gamma)
        self.set_arm()
       
        return self.Theta1,self.Theta2,self.Theta3,self.Theta4
   
    def inverse_kin_main_side_arm_1(self):
       
        return 0    
   
    def inverse_kin_main_side_arm_1(self):
       
        return 0  
   
    def set_arm(self):
        servo_control(self.Theta1,self.Theta2,self.Theta3,self.Theta4)
   
class servo_control():
   
    def __init__(self,T1,T2,T3,T4):
        
        Servo1_offset = 0
        Servo1_offset = -10
        Servo1_offset =0
        Servo1_offset =0

        #kit.servo[Servo1].angle=T1
        #kit.servo[Servo2].angle=180-60-T2
        #kit.servo[Servo3].angle=85-T3
        #kit.servo[Servo4].angle=105-T4
        print("Updated")
       
#-------------------------Main Loop-------------------------

if __name__ == "__main__":
    WindowLog = {"MainW" : [MainMenu,CartControl,DirectControl]}
   
    CurrentWindow = WindowLog["MainW"]
    app = MainWindow()

    app.mainloop()

input('Press ENTER to exit')
