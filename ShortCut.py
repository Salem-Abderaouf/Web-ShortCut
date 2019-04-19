import os 
from Tkinter import *
root = Tk()
root.title('SHORTCUT')
root.iconbitmap(default='add.ico')
Pic = PhotoImage(file="add.gif")
root.geometry('200x60+0+200')
root.configure(background='#000000')
#Define The widgets  
val = StringVar()
name = Entry(root,width=60,textvariable=val)

#set functions
def set_file():
    get_name = val.get()
    os.mkdir('./%s' % (get_name))
    txt = open('msg.txt','r')
    data = txt.read()
    myFile = open(get_name + "/index.html", "w")
    myFile.write(data)
    js = os.mkdir(os.path.join(str(get_name),'js'))
    myFile = open(get_name + "/js/app.js", "w")
    css = os.mkdir(os.path.join(str(get_name),'css'))
    myFile = open(get_name + "/css/style.css", "w")

button = Button(root, image=Pic,command=set_file)

def passText(event):
    name.delete(0, END)
    passcheck=True
#widgets config style    
button.config(background="#000000")
button.pack(side=LEFT)
name.config(background="#000000",foreground="#9acd32")
name.pack(ipady=20)
root.overrideredirect(0)
name.insert(0,"Name Your Folder")
name.bind("<Button>",passText)
root.mainloop()
