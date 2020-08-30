from tkinter import *
import os
from playsound import playsound


#os.system("splash_screen1.py")
root=Tk()
root.geometry('5000x4000')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Welcome To Face Detection System!!!')
frame.config(background='light blue')
label = Label(frame, text="Face Detection System",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
label = Label(frame, text="Tilak deepti viplavi",bg='light blue',font=('Times 17 bold'))
label.pack(side=BOTTOM)
filename = PhotoImage(file="D:\\Drowsiness_detection_system\\demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)


def function2():
    os.system("D:\\Drowsiness_detection_system\\drowsinessDetect.py")


def function3():
    os.system("D:\\Drowsiness_detection_system\\gender_age_detection.py")


def function4():
    os.system("")

def function5():
    os.system("")

def function6():
    root.destroy()


menu = Menu(root)
root.config(menu=menu)

but1=Button(frame,padx=40,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function2,text='Drowsiness Detection',font=('helvetica 15 bold'))
but1.place(x=400,y=200)


but3=Button(frame,padx=40,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=function3,text='Age and Gender Detection',font=('helvetica 15 bold'))
but3.place(x=400,y=300)

but5=Button(frame,padx=40,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=function6,font=('helvetica 15 bold'))
but5.place(x=610,y=620)
#playsound("sounds/welcome.mp3")


root.mainloop()
