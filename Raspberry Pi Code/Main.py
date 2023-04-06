# ------------------------------------------------
#
# Third Year Project - UCL EEE
# Author: Harry Softley-Graham
# Supervisor: Dr. Chow Yin Lai
#
# ------------------------------------------------

#-------------------------IMPORTS---------------------------------------

#Board Imports
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels = 16)
delay = 2

#UI Impots
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Maths and timing imports
import math
import numpy as np
import time
import sys

#-------------------------TKINTER STYLISATIONS-------------------------
TitleFont = ("Arial",20)
SubFont1 = ("Arial",10)
SubFont2 = ("Arial",5)



#-------------------------Servo Setup and Calibration-------------------------


#This class is the object for a given servo
class Servo_Info:

    def __init__(self,Number):
        self.ServoNumber = Number
        self.Angle = 0
        self.Offset = 0
        self.Pin =0
        self.Board = 0
        self.Inverse = False

    #Sets Direction
    def SetInverse(self,Value):
        self.Inverse = Value

    #Sets and Gets servo pin
    def GetPin(self):
        return self.Pin
    def SetPin(self,value):
        self.Pin = value

    #Sets and Gets servo offset
    def GetOffset(self):
        return self.Offset
    def SetOffset(self,value):
        self.Offset = value

    #Sets and Gets servo angle
    def GetAngle(self):
        return self.Angle
    def SetAngle(self,value):
        self.Angle = value

    #Sets and Gets board address
    def GetBoard(self):
        return self.Board
    def SetBoard(self,value):
        self.Board = value

    #Turns servo and updates positional value
    def Turn_Servo(self,value):
        self.SetAngle(value)
        print("Turning servo ",self.ServoNumber," to",self.Angle," on pin",self.Pin)

        if self.Inverse ==False:
            kit.servo[self.Pin].angle=self.Angle + self.Offset
            pass
        else:
            kit.servo[self.Pin].angle=180 -(self.Angle + self.Offset)
            pass

#Array of servo info
Full_Servo_Info = []

#Servo 1
Servo0 = Servo_Info(0)
Servo0.SetPin(0)
Servo0.SetOffset(90)
Servo0.SetAngle(0)
Servo0.SetBoard(0)
Servo0.SetInverse(True)

Full_Servo_Info.append(Servo0)

#Servo 2
Servo1 = Servo_Info(1)
Servo1.SetPin(4)
Servo1.SetOffset(35)
Servo1.SetAngle(0)
Servo1.SetBoard(0)
Servo1.SetInverse(True)
Full_Servo_Info.append(Servo1)

#Servo 3
Servo2 = Servo_Info(2)
Servo2.SetPin(8)
Servo2.SetOffset(5)
Servo2.SetAngle(0)
Servo2.SetBoard(0)
Servo2.SetInverse(True)
Full_Servo_Info.append(Servo2)

#Servo 4
Servo3 = Servo_Info(3)
Servo3.SetPin(9)
Servo3.SetOffset(80)
Servo3.SetAngle(0)
Servo3.SetBoard(0)
Full_Servo_Info.append(Servo3)

#Servo 5
Servo4 = Servo_Info(4)
Servo4.SetPin(12)
Servo4.SetOffset(45)
Servo4.SetAngle(0)
Servo4.SetBoard(0)
Full_Servo_Info.append(Servo4)

#Servo 6
Servo5 = Servo_Info(5)
Servo5.SetPin(1)
Servo5.SetOffset(0)
Servo5.SetAngle(0)
Servo5.SetBoard(0)
Full_Servo_Info.append(Servo5)

#Servo 7
Servo6 = Servo_Info(6)
Servo6.SetPin(2)
Servo6.SetOffset(0)
Servo6.SetAngle(0)
Servo6.SetBoard(0)
Full_Servo_Info.append(Servo6)

#Servo 8
Servo7 = Servo_Info(7)
Servo7.SetPin(5)
Servo7.SetOffset(0)
Servo7.SetAngle(0)
Servo7.SetBoard(0)
Full_Servo_Info.append(Servo7)

#Servo 9
Servo8 = Servo_Info(8)
Servo8.SetPin(10)
Servo8.SetOffset(0)
Servo8.SetAngle(0)
Servo8.SetBoard(0)
Servo8.SetInverse(True)

Full_Servo_Info.append(Servo8)

#Servo 10
Servo9 = Servo_Info(9)
Servo9.SetPin(13)
Servo9.SetOffset(0)
Servo9.SetAngle(0)
Servo9.SetBoard(0)
Full_Servo_Info.append(Servo9)

#Servo 11
Servo10 = Servo_Info(9)
Servo10.SetPin(14)
Servo10.SetOffset(0)
Servo10.SetAngle(0)
Servo10.SetBoard(0)
Full_Servo_Info.append(Servo10)



#---------------------------MAIN UI CLASS---------------------------------

#Class for the main window that contains the frames that are shown
class MainWindow(tk.Tk):

    def __init__(self):        
       
        tk.Tk.__init__(self)
        tk.Tk.title(self,"Robot Control")
        Window = tk.Frame(self)
     
        Window.pack(side="top", expand = True, fill="both")

        DropDownMenu = tk.Menu(Window)
        tk.Tk.config(self,menu=DropDownMenu)
        #system menu
        SystemMenu = tk.Menu(DropDownMenu)
        DropDownMenu.add_cascade(label="System",menu=SystemMenu)
        SystemMenu.add_command(label="Home",command=lambda:self.Frames[CurrentWindow[0]].tkraise())
        SystemMenu.add_separator()
        SystemMenu.add_command(label="Cart Control",command=lambda:self.ShowFrame(CartControl))
        SystemMenu.add_command(label="Angle Control",command=lambda:self.ShowFrame(DirectControl)) #opens graph
        SystemMenu.add_command(label="Demo",command=lambda:self.ShowFrame(InstructionSet)) #opens graph
        SystemMenu.add_separator()
        SystemMenu.add_command(label="Exit",command=lambda:self.Exit()) #opens graph

        self.Frames={}

        for WindowFrame in (CurrentWindow):
            CurrentFrame = WindowFrame(Window,self)
            self.Frames[WindowFrame] = CurrentFrame
            CurrentFrame.grid(row=0,column=0,sticky="nsew")#
           
        self.Frames[CurrentWindow[0]].tkraise()

       
    #To exit code
    def Exit(self):
        sys.exit()    

    #Function to show a page
    def ShowFrame(self,Pointer):

        CurrentFrame = self.Frames[Pointer]
        CurrentFrame.tkraise()
   
       
#--------------------------------PAGES---------------------------------


#MAIN MENU UI
class MainMenu(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)

        self.Spacer = ttk.Label(self,text="                                                                    ")
        self.Spacer.grid(row = 0,column = 0,columnspan = 7),  
       

        self.Button1 = ttk.Button(self,text="Angle Control", width=20,command = lambda:controller.ShowFrame(DirectControl))
        self.Button1.grid(row = 2,column = 2, columnspan=3)  
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 3,column = 0,columnspan = 7), 

        self.Button2 = ttk.Button(self,text="Cart Control:", width=20,command = lambda:controller.ShowFrame(CartControl))
        self.Button2.grid(row = 4,column = 2, columnspan=3)     
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 5,column = 0,columnspan = 7),   

        self.Button3 = ttk.Button(self,text="Instruction Set:", width=20,command = lambda:controller.ShowFrame(InstructionSet))
        self.Button3.grid(row = 6,column = 2, columnspan=3)    
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 7,column = 0,columnspan = 7),  
            
    
#Cartistian Control of the end effectors 
class CartControl(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)



     
        SubFont1 = ("Arial",14)
       
        self.X=tk.DoubleVar()
        self.Y=tk.DoubleVar()
        self.Z=tk.DoubleVar()
        self.Gamma=tk.DoubleVar()


        
        self.sa1_X=tk.DoubleVar()
        self.sa1_Y=tk.DoubleVar()
        self.sa1_Z=tk.DoubleVar()

        self.sa2_X=tk.DoubleVar()
        self.sa2_Y=tk.DoubleVar()
        self.sa2_Z=tk.DoubleVar()

        self.Sub_Arm_Origin=tk.BooleanVar()
        self.Mirror_Sub_Arm=tk.BooleanVar()
        self.Gripper1=tk.BooleanVar()
        self.Gripper2=tk.BooleanVar()

        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 0,column = 0,columnspan = 7),  


        self.Title = ttk.Label(self,text="Main ARM")
        self.Title.grid(row = 1,column = 0,columnspan = 7),  
       
        self.x_scale =  ttk.Scale(self,
                                  from_=-350, to=350,
                                  orient=HORIZONTAL,
                                  variable=self.X,
                                  command= lambda x=None:self.Change_Arm())    
        self.x_scale.grid(row = 2,column = 1,columnspan = 5)  
       
        self.XLable = ttk.Label(self,text="X value:")
        self.XLable.grid(row = 2,column = 0)        
        self.XValue = ttk.Label(self,text=self.getvalue(self.X))
        self.XValue.grid(row = 2,column = 6,columnspan = 1)            
       
        self.y_scale =  ttk.Scale(self,
                                  from_=-350, to=350,
                                  orient=HORIZONTAL,
                                  variable=self.Y,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.y_scale.grid(row = 3,column = 1,columnspan = 5)  
        self.YLable = ttk.Label(self,text="Y value:")
        self.YLable.grid(row = 3,column = 0)  
        self.YValue= ttk.Label(self,text=self.getvalue(self.Y))
        self.YValue.grid(row = 3,column = 6)          
       
        self.z_scale =  ttk.Scale(self,
                                  from_=-350, to=350,
                                  orient=HORIZONTAL,
                                  variable=self.Z,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.z_scale.grid(row = 4,column = 1,columnspan = 5)  
        self.ZLable = ttk.Label(self,text="Z value:")
        self.ZLable.grid(row = 4,column = 0)  
        self.ZValue = ttk.Label(self,text=self.getvalue(self.Z))
        self.ZValue.grid(row = 4,column = 6)          
       
        self.Gamma_scale =  ttk.Scale(self,
                                  from_=0, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.Gamma,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Gamma_scale.grid(row = 5,column = 1,columnspan = 5)  
        self.GammaLable = ttk.Label(self,text="Gamma:")
        self.GammaLable.grid(row = 5,column = 0)  
        self.GammaValue = ttk.Label(self,text=self.getvalue(self.Gamma))
        self.GammaValue.grid(row = 5,column = 6)



        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 6,column = 0,columnspan = 3),  


        self.Title = ttk.Label(self,text="SUB ARM 1")
        self.Title.grid(row = 7,column = 0,columnspan = 3),  


        self.Sub1_X_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa1_X,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub1_X_scale.grid(row = 8,column = 1)  
        self.Sub1_XLable = ttk.Label(self,text="X:")
        self.Sub1_XLable.grid(row = 8,column = 0)  
        self.Sub1_XValue = ttk.Label(self,text=self.getvalue(self.sa1_X))
        self.Sub1_XValue.grid(row = 8,column = 2)  

        self.Sub1_Y_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa1_Y,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub1_Y_scale.grid(row = 9,column = 1)  
        self.Sub1_YLable = ttk.Label(self,text="Y:")
        self.Sub1_YLable.grid(row = 9,column = 0)  
        self.Sub1_YValue = ttk.Label(self,text=self.getvalue(self.sa1_Y))
        self.Sub1_YValue.grid(row = 9,column = 2)   

        self.Sub1_Z_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa1_Z,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub1_Z_scale.grid(row = 10,column = 1)  
        self.Sub1_ZLable = ttk.Label(self,text="Z:")
        self.Sub1_ZLable.grid(row = 10,column = 0)  
        self.Sub1_ZValue = ttk.Label(self,text=self.getvalue(self.sa1_Z))
        self.Sub1_ZValue.grid(row = 10,column = 2) 

        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 6,column = 4,columnspan = 3),  


        self.Title = ttk.Label(self,text="SUB ARM 2")
        self.Title.grid(row = 7,column = 4,columnspan = 3),  


        
        self.Sub2_X_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa2_X,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub2_X_scale.grid(row = 8,column = 5)  
        self.Sub2_XLable = ttk.Label(self,text="X:")
        self.Sub2_XLable.grid(row = 8,column = 4)  

        self.Sub2_XValue = ttk.Label(self,text=self.getvalue(self.sa2_X))
        self.Sub2_XValue.grid(row = 8,column = 6) 

        self.Sub2_Y_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa2_Y,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub2_Y_scale.grid(row = 9,column = 5)  
        self.Sub2_YLable = ttk.Label(self,text="Y:")
        self.Sub2_YLable.grid(row = 9,column = 4)  
        self.Sub2_YValue = ttk.Label(self,text=self.getvalue(self.sa2_Y))
        self.Sub2_YValue.grid(row = 9,column = 6)   

        self.Sub2_Z_scale =  ttk.Scale(self,
                                  from_=-120, to=360,
                                  orient=HORIZONTAL,
                                  variable=self.sa2_Z,                                  
                                  command=lambda x=None:self.Change_Arm())
        self.Sub2_Z_scale.grid(row = 10,column = 5)  
        self.Sub2_ZLable = ttk.Label(self,text="Z:")
        self.Sub2_ZLable.grid(row = 10,column = 4)  
        self.Sub2_ZValue = ttk.Label(self,text=self.getvalue(self.sa2_Z))
        self.Sub2_ZValue.grid(row = 10,column = 6) 

        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 11,column = 0,columnspan = 3),  

        self.Enable_Mirror = ttk.Button(self,text="Mirror",command = lambda x=None:self.Flip(self.Mirror_Sub_Arm))
        self.Enable_Mirror.grid(row = 12,column = 0,columnspan = 3),  
        self.Enable_Origin = ttk.Button(self,text="Change Origin",command = lambda x=None:self.Flip(self.Sub_Arm_Origin))
        self.Enable_Origin.grid(row = 12,column = 4,columnspan = 3),  

        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 13,column = 0,columnspan = 7),  

        self.Claw1 = ttk.Button(self,text="Claw1",command = lambda x=None:self.Flip(self.Gripper1))
        self.Claw1.grid(row = 14,column = 0,columnspan = 3),  
        self.Claw2 = ttk.Button(self,text="Claw2",command = lambda x=None:self.Flip(self.Gripper2))
        self.Claw2.grid(row = 14,column = 4,columnspan = 3),  

        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 15,column = 0,columnspan = 7),  



        self.x_scale.set(133)
        self.y_scale.set(0)                
        self.z_scale.set(216)  
        self.Gamma_scale.set(0)        

        self.sa1_X.set(120)
        self.sa1_Y.set(0)                
        self.sa1_Z.set(60)  

        self.sa2_X.set(120)
        self.sa2_Y.set(0)                
        self.sa2_Z.set(60)  
        


       
    def Change_Arm(self):
        self.XValue.configure(text=self.getvalue(self.X))
        self.YValue.configure(text=self.getvalue(self.Y))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        self.ZValue.configure(text=self.getvalue(self.Z))
        self.GammaValue.configure(text=self.getvalue(self.Gamma))

        self.Sub1_XValue.configure(text=self.getvalue(self.sa1_X))
        self.Sub1_YValue.configure(text=self.getvalue(self.sa1_Y))
        self.Sub1_ZValue.configure(text=self.getvalue(self.sa1_Z))
        self.Sub2_XValue.configure(text=self.getvalue(self.sa2_X))
        self.Sub2_YValue.configure(text=self.getvalue(self.sa2_Y))
        self.Sub2_ZValue.configure(text=self.getvalue(self.sa2_Z))        
        
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        
        if self.Sub_Arm_Origin.get():
            if self.Mirror_Sub_Arm:
                kin.inverse_kin_main_side_arm_1(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),True)
                kin.inverse_kin_main_side_arm_2(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),True)

            else:
                kin.inverse_kin_main_side_arm_1(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),True)
                kin.inverse_kin_main_side_arm_2(self.sa2_X.get(),self.sa2_Y.get(),self.sa2_Z.get(),True)


        else:
            if self.Mirror_Sub_Arm.get():
                kin.inverse_kin_main_side_arm_1(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),False)
                kin.inverse_kin_main_side_arm_2(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),False)
            else:
                kin.inverse_kin_main_side_arm_1(self.sa1_X.get(),self.sa1_Y.get(),self.sa1_Z.get(),False)
                kin.inverse_kin_main_side_arm_2(self.sa2_X.get(),self.sa2_Y.get(),self.sa2_Z.get(),False)
                

       
    def getvalue(self,VAR):
        return '{: .2f}'.format(VAR.get())
    
    def Flip(self,Var):

        if Var.get() == True:
            Var.set(False)
        else:
            Var.set(True)
        print(Var.get())


        Temp = Kinimatics()
        Temp.Gripper(1,self.Gripper1.get())
        Temp.Gripper(2,self.Gripper2.get())


#Direct control of each servos angles
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
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle0,                                  
                                    command=lambda x=None: Full_Servo_Info[0].Turn_Servo(self.Angle0.get()))
        self.Scale_0.grid(row = 1,column = 1)  
        self.Scale_0 = ttk.Label(self,text="Servo 0:")
        self.Scale_0.grid(row = 1,column = 0)  

        
        self.Scale_1 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle1,                                  
                                    command=lambda x=None: Full_Servo_Info[1].Turn_Servo(self.Angle1.get()))
        self.Scale_1.grid(row = 2,column = 1)  
        self.Scale_1 = ttk.Label(self,text="Servo 1:")
        self.Scale_1.grid(row = 2,column = 0)  

        self.Scale_2 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle2,                                  
                                    command=lambda x=None: Full_Servo_Info[2].Turn_Servo(self.Angle2.get()))
        self.Scale_2.grid(row = 3,column = 1)  
        self.Scale_2 = ttk.Label(self,text="Servo 2:")
        self.Scale_2.grid(row = 3,column = 0)  

        self.Scale_3 =  ttk.Scale(self,
                                    from_=-180, to=180,
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
        
        self.Scale_5 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle5,                                  
                                    command=lambda x=None: Full_Servo_Info[5].Turn_Servo(self.Angle5.get()))
        self.Scale_5.grid(row = 6,column = 1)  
        self.Scale_5 = ttk.Label(self,text="Servo 5:")
        self.Scale_5.grid(row = 6,column = 0)  

        self.Scale_6 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle6,                                  
                                    command=lambda x=None: Full_Servo_Info[6].Turn_Servo(self.Angle6.get()))
        self.Scale_6.grid(row = 1,column = 3)  
        self.Scale_6 = ttk.Label(self,text="Servo 6:")
        self.Scale_6.grid(row = 1,column = 2) 

        self.Scale_7 =  ttk.Scale(self,
                                    from_=50, to=145,
                                    orient=HORIZONTAL,
                                    variable=self.Angle7,                                  
                                    command=lambda x=None: Full_Servo_Info[7].Turn_Servo(self.Angle7.get()))
        self.Scale_7.grid(row = 2,column = 3)  
        self.Scale_7 = ttk.Label(self,text="Servo 7:")
        self.Scale_7.grid(row = 2,column = 2)  

        self.Scale_8 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle8,                                  
                                    command=lambda x=None: Full_Servo_Info[8].Turn_Servo(self.Angle8.get()))
        self.Scale_8.grid(row = 3,column = 3)  
        self.Scale_8 = ttk.Label(self,text="Servo 8:")
        self.Scale_8.grid(row = 3,column = 2)  

        self.Scale_9 =  ttk.Scale(self,
                                    from_=-180, to=180,
                                    orient=HORIZONTAL,
                                    variable=self.Angle9,                                  
                                    command=lambda x=None: Full_Servo_Info[9].Turn_Servo(self.Angle9.get()))
        self.Scale_9.grid(row = 4,column = 3)  
        self.Scale_9 = ttk.Label(self,text="Servo 9:")
        self.Scale_9.grid(row = 4,column = 2)  

        self.Scale_10 =  ttk.Scale(self,
                                    from_= 50, to=145,
                                    orient=HORIZONTAL,
                                    variable=self.Angle10,                                  
                                    command=lambda x=None: Full_Servo_Info[10].Turn_Servo(self.Angle10.get()))
        self.Scale_10.grid(row = 5,column = 3)  
        self.Scale_10 = ttk.Label(self,text="Servo 10:")
        self.Scale_10.grid(row = 5,column = 2)  

    def Xslider(self):
        self.XValue.configure(text=self.get_current_value_x())
        kin = Kinimatics()
        T1,T2,T3,T4 = kin.inverse_kin_main_arm(self.X.get(),self.Y.get(),self.Z.get(),self.Gamma.get())
        print(T1,T2,T3,T4)
       
    def get_current_value_x(self):
        return '{: .2f}'.format(self.X.get())

   
#To play pre programed instruction sets
class InstructionSet(tk.Frame):

    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)

        self.Spacer = ttk.Label(self,text="                                                                    ")
        self.Spacer.grid(row = 0,column = 0,columnspan = 7),  
       

        self.Button1 = ttk.Button(self,text="Set 1", width=20,command = lambda:self.Instruction_Set_1())
        self.Button1.grid(row = 2,column = 2, columnspan=3)  
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 3,column = 0,columnspan = 7), 

        self.Button2 = ttk.Button(self,text="Set 2", width=20,command = lambda:self.Instruction_Set_2())
        self.Button2.grid(row = 4,column = 2, columnspan=3)     
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 5,column = 0,columnspan = 7),   

        self.Button3 = ttk.Button(self,text="Set 3", width=20,command = lambda:self.Instruction_Set_3())
        self.Button3.grid(row = 6,column = 2, columnspan=3)    
        
        self.Spacer = ttk.Label(self,text="             ")
        self.Spacer.grid(row = 7,column = 0,columnspan = 7),  
            
    def Instruction_Set_1(self):
        kin = Kinimatics()

        To = [160,0,60,360]
        From = [160,0,60,270]

        Time = 4
        Int = 50
        time.sleep(5)

        kin.TrajectoryPlanningMain(To[0],To[1],To[2],To[3],From[0],From[1],From[2],From[3],Time,Int)
        time.sleep(2)
        kin.TrajectoryPlanningMain(From[0],From[1],From[2],From[3],To[0],To[1],To[2],To[3],Time,Int)
        time.sleep(2)


    def Instruction_Set_2(self):
            
        kin = Kinimatics()

        Main_Home = [140,0,80]
        Object = [160,0,40]
        Object_press = [220,0,40]

        Arm_Placement = [140,0,20]
                
        Arm_Press = [140-60,0,20]

        Arm_Home = [80,0,60]
        Away = []

        Time = 2
        Int = 20

        kin.inverse_kin_main_arm(Main_Home[0],Main_Home[1],Main_Home[2],0)
        Full_Servo_Info[4].Turn_Servo(120)
        time.sleep(1)
        kin.inverse_kin_main_side_arm_1(Arm_Home[0],Arm_Home[1],Arm_Home[2])
        kin.inverse_kin_main_side_arm_2(Arm_Home[0],Arm_Home[1],Arm_Home[2])

        time.sleep(1)
        Full_Servo_Info[4].Turn_Servo(0)

        kin.TrajectoryPlanningMain(Main_Home[0],Main_Home[1],Main_Home[2],0,Object[0],Object[1],Object[2],0,Time,Int)
        kin.TrajectoryPlanningSubArm(Arm_Home[0],Arm_Home[1],Arm_Home[2],Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Time,Int)
        kin.Gripper(1,True)
        kin.Gripper(2,True)
        kin.Both_Arms(Object[0],Object[1],Object[2],Object_press[0],Object_press[1],Object_press[2],0,Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Time,Int)
        kin.Both_Arms(Object_press[0],Object_press[1],Object_press[2],Object[0],Object[1],Object[2],0,Arm_Press[0],Arm_Press[1],Arm_Press[2],Time,Int)
        kin.Gripper(1,False)
        kin.Gripper(2,False)
        kin.TrajectoryPlanningSubArm(Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Arm_Home[0],Arm_Home[1],Arm_Home[2],Time,Int)
        kin.TrajectoryPlanningMain(Object[0],Object[1],Object[2],0,Main_Home[0],Main_Home[1],Main_Home[2],0,Time,Int)
        Full_Servo_Info[4].Turn_Servo(120)

        pass

    def Instruction_Set_3(self):
                    
        kin = Kinimatics()

        Main_Home = [140,0,80]
        Object = [160,0,80]
        Object_press = [220,0,80]

        Arm_Placement = [140,0,20]
                
        Arm_Press = [140-60,0,20]

        Arm_Home = [80,0,20]
        Away = []

        Time = 2
        Int = 30

        kin.inverse_kin_main_arm(Main_Home[0],Main_Home[1],Main_Home[2],0)
        Full_Servo_Info[4].Turn_Servo(120)
        time.sleep(1)
        kin.inverse_kin_main_side_arm_1(Arm_Home[0],Arm_Home[1],Arm_Home[2])
        kin.inverse_kin_main_side_arm_2(Arm_Home[0],Arm_Home[1],Arm_Home[2])

        time.sleep(1)
        Full_Servo_Info[4].Turn_Servo(0)
        time.sleep(1)
        kin.TrajectoryPlanningMain(Main_Home[0],Main_Home[1],Main_Home[2],0,Object[0],Object[1],Object[2],0,Time,Int)
        kin.TrajectoryPlanningSubArm(Arm_Home[0],Arm_Home[1],Arm_Home[2],Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Time,Int)
        kin.Gripper(1,True)
        kin.Gripper(2,True)
        kin.Both_Arms(Object[0],Object[1],Object[2],Object_press[0],Object_press[1],Object_press[2],0,Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Time,Int)
        time.sleep(1)
        kin.Both_Arms(Object_press[0],Object_press[1],Object_press[2],Object[0],Object[1],Object[2],0,Arm_Press[0],Arm_Press[1],Arm_Press[2],Time,Int)
        kin.Gripper(1,False)
        kin.Gripper(2,False)
        kin.TrajectoryPlanningSubArm(Arm_Placement[0],Arm_Placement[1],Arm_Placement[2],Arm_Home[0],Arm_Home[1],Arm_Home[2],Time,Int)
        kin.TrajectoryPlanningMain(Object[0],Object[1],Object[2],0,Main_Home[0],Main_Home[1],Main_Home[2],0,Time,Int)
        Full_Servo_Info[4].Turn_Servo(120)
        pass



#-------------------------Kinimatics and Control-------------------------

class Kinimatics():

    def __init__(self):

        #Set angles
        self.L1=0
        self.L2=120
        self.L3=120
        self.L4=110

        self.MindPoint = 0

        self.L5=60
        self.L6=120
        self.L7=60
        self.L8=120
       
       #End effector position
        self.End_Effector = [0,0,0]


        #Servo angles

        #Main Body
        self.Theta1 = 0
        self.Theta2 = 0
        self.Theta3 = 0
        self.Theta4 = 0

        #Pivot
        self.Theta5 = 0

        #Arm 1
        self.Theta6 = 0
        self.Theta7 = 0

        #Arm 2
        self.Theta9 = 0
        self.Theta10 = 0

        #Gripper
        self.Theta8 = 0
        self.Theta11 = 0


        self.DH_Table = [[],[],[],[]]

        self.ClosedAngle = 50

        self.OpenAngle = 145

    def Calc_Gamma(self):
        Gamma = self.Theta3+self.Theta4-self.Theta2
        return Gamma
   
    #Claculates inverse kinimatics of the main arm
    def inverse_kin_main_arm(self,X,Y,Z,Gamma,output = True):
        try:
            pi = math.pi
            
            Gamma_r = math.radians(Gamma)
    
            Theta1 = math.atan2(Y,Z)

            X_val=X-(math.cos(Theta1)*self.L4*math.cos(Gamma_r))
            Y_val=Y-(math.sin(Theta1)*self.L4*math.cos(Gamma_r))
            Z_val=Z-(self.L4*math.sin(Gamma_r))
    
            Beta = math.atan2(Z_val, math.sqrt(Y_val**2+X_val**2))
    
            Phi = math.acos((self.L2**2+Z_val**2+Y_val**2+X_val**2-self.L3**2)/(2*self.L2*math.sqrt(Z_val**2+Y_val**2+X_val**2)))
    
            Theta2 = Beta + Phi
            cTheta3 = (X_val**2+Y_val**2+Z_val**2-self.L3**2-self.L3**2)/(2*self.L2*self.L3)
            sTheta3 = math.sqrt(1-(cTheta3**2))

            Theta3 = math.atan2(sTheta3,cTheta3)

            Theta4 = Gamma_r-(-Theta2)-Theta3      

            self.Theta1=math.degrees(Theta1)
            self.Theta2=math.degrees(Theta2)
            self.Theta3=math.degrees(Theta3)
            self.Theta4=math.degrees(Theta4)
           
            if output:
                self.set_arm()
                print("____________________________________________")
        
            return self.Theta1,self.Theta2,self.Theta3,self.Theta4
        except:
            return self.Theta1,self.Theta2,self.Theta3,self.Theta4

    #calculates mathmatical transform from end effector to origin, used for sub end effectors
    def Transform_origin_to_midpoint(self,X,Y,Z,Theta1,Gamma,Midpoint):

        Gamma = math.radians(Gamma)
        Theta1 = math.radians(Theta1)

        X_RJ=X-(math.cos(Theta1)*Midpoint*math.cos(Gamma))

        Y_RJ=Y-(math.sin(Theta1)*Midpoint*math.cos(Gamma))

        Z_RJ=Z-(Midpoint*math.sin(Gamma))
        

        P_R = [[X-X_RJ], Y-Y_RJ, Z-Z_RJ ]
        
        R = np.matmul([[math.cos(Theta1), -math.sin(Theta1), 0], [math.sin(Theta1), math.cos(Theta1), 0], [0, 0, 1]],
                      [[math.cos(Gamma), 0, math.sin(Gamma)], [0, 1, 0], [-math.sin(Gamma), 0, math.cos(Gamma)]])

        P_SER = np.matmul(R,P_R)

        X_val = P_SER[0]

        Y_val = P_SER[1]

        Z_val = P_SER[2]

        return X_val, Y_val, Z_val
   
    #Inverse kinimatics for sub arm 1
    def inverse_kin_main_side_arm_1(self,X,Y,Z,Origin_at_mid = False,output = True):
        try:
            X_val=X
            Y_val=Y
            Z_val=Z 
    

            if Origin_at_mid:
                X_val, Y_val, Z_val = self.Transform_origin_to_midpoint(X,Y,Z,self.Theta1,self.Calc_Gamma,self.MindPoint)

            Theta5 = math.atan2(Y,Z)

            Beta = math.atan2(math.sqrt(Y_val**2+Z_val**2), X_val)
    
            Phi = math.acos((self.L5**2+Z_val**2+Y_val**2+X_val**2-self.L6**2)/(2*self.L5*math.sqrt(Z_val**2+Y_val**2+X_val**2)))
    
            Theta6 = Beta + Phi

            Theta7 = math.acos((X_val**2+Y_val**2+Z_val**2-self.L5**2-self.L6**2)/(2*self.L5*self.L6))

            self.Theta5=math.degrees(Theta5)
            self.Theta6=math.degrees(Theta6)
            self.Theta7=math.degrees(Theta7)
            if output:
                self.set_arm("sub1")
                print("____________________________________________")

            return self.Theta5,self.Theta6,self.Theta7 
        except:
            print("SubArm1 Out of Range")
            return self.Theta5,self.Theta6,self.Theta7 
   
    #Inverse kinimatics for sub arm 2
    def inverse_kin_main_side_arm_2(self,X,Y,Z,Origin_at_mid = False,output = True):
        try:
            X_val=X
            Y_val=Y
            Z_val=Z


            if Origin_at_mid:
                X_val, Y_val, Z_val = self.Transform_origin_to_midpoint(X,Y,Z,self.Theta1,self.Calc_Gamma,self.MindPoint)

            Beta = math.atan2(math.sqrt(Y_val**2+Z_val**2), X_val)
    
            Phi = math.acos((self.L5**2+Z_val**2+Y_val**2+X_val**2-self.L6**2)/(2*self.L5*math.sqrt(Z_val**2+Y_val**2+X_val**2)))
    
            Theta9 = Beta + Phi

            Theta10 = math.acos((X_val**2+Y_val**2+Z_val**2-self.L5**2-self.L6**2)/(2*self.L5*self.L6))

            self.Theta9=math.degrees(Theta9)
            self.Theta10=math.degrees(Theta10)

            if output:
                self.set_arm("sub2")
                print("____________________________________________")

            return self.Theta9,self.Theta10   
        except:
            print("SubArm2 Out of Range")
            return self.Theta5,self.Theta9,self.Theta10   

    #updates real location of the servos through the servo class
    def set_arm(self,val="main"):

        if val == "main":
            #Updates Main arm
            Full_Servo_Info[0].Turn_Servo(self.Theta1)
            Full_Servo_Info[1].Turn_Servo(self.Theta2)
            Full_Servo_Info[2].Turn_Servo(self.Theta3)
            Full_Servo_Info[3].Turn_Servo(self.Theta4)

        elif val == "sub1":
            #Updates Pivot
            Full_Servo_Info[4].Turn_Servo(self.Theta5)

            #Updates sub arm 1
            Full_Servo_Info[5].Turn_Servo(self.Theta6)
            Full_Servo_Info[6].Turn_Servo(self.Theta7)

        elif val == "sub2":
            #Updates Pivot
            Full_Servo_Info[4].Turn_Servo(self.Theta5)

            #Updates sub arm 2
            Full_Servo_Info[8].Turn_Servo(self.Theta9)
            Full_Servo_Info[9].Turn_Servo(self.Theta10)


    #Trajectory planning function for main arm
    def TrajectoryPlanningMain(self,FromX,FromY,FromZ,FromGamma,TO_X,TO_Y,TO_Z,To_Gamma,Time =3,Steps = 50):

        #Generate trajectory constants
        Xa_0,Xa_3,Xa_4,Xa_5 = self.GenerateConstants(Time,TO_X,FromX)
        Ya_0,Ya_3,Ya_4,Ya_5 = self.GenerateConstants(Time,TO_Y,FromY)
        Za_0,Za_3,Za_4,Za_5 = self.GenerateConstants(Time,TO_Z,FromZ)
        Gamma_0,Gamma_3,Gamma_4,Gamma_5 = self.GenerateConstants(Time,To_Gamma,FromGamma)

        #Arrays that store locations
        X_Locs = []
        Y_Locs = []
        Z_Locs = []
        Gamma_Change = []
        timeinterval = Time/Steps

        Time_List =  np.linspace(0, Time, num=Steps)

        for current_step in Time_List:
            X = Xa_0 + Xa_3*current_step**3 + Xa_4*current_step**4 + Xa_5*current_step**5
            Y = Ya_0 + Ya_3*current_step**3 + Ya_4*current_step**4 + Ya_5*current_step**5
            Z = Za_0 + Za_3*current_step**3 + Za_4*current_step**4 + Za_5*current_step**5
            Gamma = Gamma_0 + Gamma_3*current_step**3 + Gamma_4*current_step**4 + Gamma_5*current_step**5

            X_Locs.append(X)
            Y_Locs.append(Y)
            Z_Locs.append(Z)
            Gamma_Change.append(Gamma)

        Angles = []
        for i in range(0,len(Time_List)):
            T1,T2,T3,T4 = self.inverse_kin_main_arm(X_Locs[i],Y_Locs[i],Z_Locs[i],Gamma_Change[i],False)
            Angles.append([T1,T2,T3,T4])
             #time.sleep(timeinterval)
        for j in Angles:
            Full_Servo_Info[0].Turn_Servo(j[0])
            Full_Servo_Info[1].Turn_Servo(j[1])
            Full_Servo_Info[2].Turn_Servo(j[2])
            Full_Servo_Info[3].Turn_Servo(j[3])

    #Trajectory planning of
    def TrajectoryPlanningSubArm(self,FromX,FromY,FromZ,TO_X,TO_Y,TO_Z,Time =3,Steps = 50):
        
        Xa_0,Xa_3,Xa_4,Xa_5 = self.GenerateConstants(Time,TO_X,FromX)

        Ya_0,Ya_3,Ya_4,Ya_5 = self.GenerateConstants(Time,TO_Y,FromY)

        Za_0,Za_3,Za_4,Za_5 = self.GenerateConstants(Time,TO_Z,FromZ)

        X_Locs = []
        Y_Locs = []
        Z_Locs = []
        timeinterval = Time/Steps

        Time_List =  np.linspace(0, Time, num=Steps)

        for current_step in Time_List:
            X = Xa_0 + Xa_3*current_step**3 + Xa_4*current_step**4 + Xa_5*current_step**5
            Y = Ya_0 + Ya_3*current_step**3 + Ya_4*current_step**4 + Ya_5*current_step**5
            Z = Za_0 + Za_3*current_step**3 + Za_4*current_step**4 + Za_5*current_step**5

            X_Locs.append(X)
            Y_Locs.append(Y)
            Z_Locs.append(Z)
        Angles = []
        for i in range(0,len(Time_List)):
            T5,T6,T7 = self.inverse_kin_main_side_arm_1(X_Locs[i],Y_Locs[i],Z_Locs[i],False,False)
            T9,T10 = self.inverse_kin_main_side_arm_2(X_Locs[i],Y_Locs[i],Z_Locs[i],False,False)
            Angles.append([T5,T6,T7,T9,T10])

        for j in Angles:
            Full_Servo_Info[4].Turn_Servo(j[0])
            Full_Servo_Info[5].Turn_Servo(j[1])
            Full_Servo_Info[6].Turn_Servo(j[2])
            Full_Servo_Info[8].Turn_Servo(j[3])
            Full_Servo_Info[9].Turn_Servo(j[3])

            #time.sleep(timeinterval)

    #Trajectory planning for when both arms are attached and want to move similtaniously
    def Both_Arms(self,FromX,FromY,FromZ,TO_X,TO_Y,TO_Z,Gamma,SA_X,SA_Y,SA_Z,Time =3,Steps = 50):
        
        #generate constants
        Xa_0,Xa_3,Xa_4,Xa_5 = self.GenerateConstants(Time,TO_X,FromX)
        Ya_0,Ya_3,Ya_4,Ya_5 = self.GenerateConstants(Time,TO_Y,FromY)
        Za_0,Za_3,Za_4,Za_5 = self.GenerateConstants(Time,TO_Z,FromZ)

        #Stores values
        X_Locs = []
        Y_Locs = []
        Z_Locs = []

        SA_NewX = []
        SA_NewY = []
        SA_NewZ = []


        timeinterval = Time/Steps

        Time_List =  np.linspace(0, Time, num=Steps)

        for current_step in Time_List:
            X = Xa_0 + Xa_3*current_step**3 + Xa_4*current_step**4 + Xa_5*current_step**5
            Y = Ya_0 + Ya_3*current_step**3 + Ya_4*current_step**4 + Ya_5*current_step**5
            Z = Za_0 + Za_3*current_step**3 + Za_4*current_step**4 + Za_5*current_step**5

            X_Locs.append(X)
            Y_Locs.append(Y)
            Z_Locs.append(Z)
        
        for current_step in range (0,len(X_Locs)):
            SA_NewX.append(SA_X+(X_Locs[0]-X_Locs[current_step]))
            SA_NewY.append(SA_Y+(Y_Locs[0]-Y_Locs[current_step]))
            SA_NewZ.append(SA_Z+(Z_Locs[0]-Z_Locs[current_step]))
        Angles = []

        for i in range(0,len(Time_List)):
            T1,T2,T3,T4 = self.inverse_kin_main_arm(X_Locs[i],Y_Locs[i],Z_Locs[i],Gamma,False)#
            T5,T6,T7 =self.inverse_kin_main_side_arm_1(SA_NewX[i],SA_NewY[i],SA_NewZ[i],False,False)
            T9,T10 =self.inverse_kin_main_side_arm_2(SA_NewX[i],SA_NewY[i],SA_NewZ[i],False,False)
            Angles.append([T1,T2,T3,T4,T5,T6,T7,T9,T10])

        for j in Angles:
            Full_Servo_Info[0].Turn_Servo(j[0])
            Full_Servo_Info[1].Turn_Servo(j[1])
            Full_Servo_Info[2].Turn_Servo(j[2])
            Full_Servo_Info[3].Turn_Servo(j[3])
            Full_Servo_Info[4].Turn_Servo(j[4])
            Full_Servo_Info[5].Turn_Servo(j[5])
            Full_Servo_Info[6].Turn_Servo(j[6])
            Full_Servo_Info[8].Turn_Servo(j[7])
            Full_Servo_Info[9].Turn_Servo(j[8])


            #time.sleep(timeinterval)

    #Function to calcualte qunitic constants for trajectories
    def GenerateConstants(self,t_f,u_f,u_0):
        a_0 = u_0
        try:
            a_3 = (10/(t_f**3))*(u_f-u_0)

            a_4 = (-15/(t_f**4))*(u_f-u_0)

            a_5 = (6/(t_f**5))*(u_f-u_0)
        except:
            a_3 = 0
            a_4 = 0
            a_5 = 0

        return a_0,a_3,a_4,a_5
    
    #Function used to open and close sub end effector grippers
    def Gripper(self,Number,State):
        if Number == 1:
            if State == True:
                Full_Servo_Info[7].Turn_Servo(int(145))

            else:
                Full_Servo_Info[7].Turn_Servo(int(50))

        elif Number == 2:
            if State== True:
                Full_Servo_Info[10].Turn_Servo(int(145))

            else:
                Full_Servo_Info[10].Turn_Servo(int(50))



class servo_control():
   
    def __init__(self,T1,T2,T3,T4):

        Full_Servo_Info[0].Turn_Servo(T1)
        Full_Servo_Info[1].Turn_Servo(T2)
        Full_Servo_Info[2].Turn_Servo(T3)
        Full_Servo_Info[3].Turn_Servo(T4)


        print("Updated")
       






       
#-------------------------Main Loop-------------------------

if __name__ == "__main__":
    #Sets up frames
    WindowLog = {"MainW" : [MainMenu,CartControl,DirectControl,InstructionSet]}
    #Opens main menu
    CurrentWindow = WindowLog["MainW"]
    app = MainWindow()

    #Sets up top menu bar
    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="MainMenu", command=app.ShowFrame(MainMenu))
    filemenu.add_command(label="Angle Control", command=lambda:app.ShowFrame(DirectControl))
    filemenu.add_command(label="Cart Control", command=lambda:app.ShowFrame(CartControl))
    filemenu.add_command(label="Machine Code", command=lambda:app.ShowFrame(DirectControl))

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=app.Exit)
    menubar.add_cascade(label="File", menu=filemenu)

    #Runs program
    app.mainloop()

