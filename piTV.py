import keyboard
import tkinter
from PIL import Image, ImageTk
import time
import os
from sys import platform



def resize(img, X, Y):
    resized = img.resize((round(img.size[0]*X), round(img.size[1]*Y)))
    return resized

class icon:
    def __init__(self,img,direction,canvas):
        self.img = img
        self.direction = direction
        self.canvas = canvas
        if self.direction == "u":
            self.x_init = 960
            self.y_init = 440
            self.x = self.x_init
            self.y = self.y_init
        elif self.direction == "d":
            self.x_init = 960
            self.y_init = 640
            self.x = self.x_init
            self.y = self.y_init
        elif self.direction == "l":
            self.x_init = 860
            self.y_init = 540
            self.x = self.x_init
            self.y = self.y_init
        elif self.direction == "r":
            self.x_init = 1060
            self.y_init = 540
            self.x = self.x_init
            self.y = self.y_init
        else:
            raise RuntimeError("direction argument must be u,d,l or r")
        self.id = self.canvas.create_image(self.x_init,self.y_init,image=self.img,anchor=tkinter.CENTER)
    def select(self):
        if self.y == self.y_init:
            if self.direction == 'u':
                self.canvas.move(self.id,0,-100)
                self.y -=100
            elif self.direction == 'd':
                self.canvas.move(self.id,0,100)
                self.y += 100
        if self.x == self.x_init:
            if self.direction == 'l':
                self.canvas.move(self.id,-100,0)
                self.x -= 100
            elif self.direction == 'r':
                self.canvas.move(self.id,100,0)
                self.x += 100
    def unselect(self):
        if self.y != self.y_init:
            if self.direction == 'u':
                self.canvas.move(self.id,0,100)
                self.y += 100
            elif self.direction == 'd':
                self.canvas.move(self.id,0,-100)
                self.y -= 100
        if self.x != self.x_init:
            if self.direction == 'l':
                self.canvas.move(self.id,100,0)
                self.x += 100
            elif self.direction == 'r':
                self.canvas.move(self.id,-100,0)
                self.x -= 100

class window:
    def __init__(self):
        global img
        global expImg
        if platform == "win32":
            img["splash"] = Image.open("img\\logo.png")
        else:
            img["splash"] = Image.open("img/logo.png")
        img["splash"] = resize(img["splash"], 0.5, 0.5)
        
        
        self.root = tkinter.Tk()
        expImg["splash"] = ImageTk.PhotoImage(img["splash"])
        self.root.attributes("-fullscreen", True)
        self.canvas = tkinter.Canvas(self.root, width=1920, height= 1080, highlightthickness=0, bg="blue")
        self.rasp_logo = self.canvas.create_image(960,540, image=expImg["splash"], anchor = tkinter.CENTER)
        self.canvas.pack()
        self.root.update()
    
    def logo_disapear(self):
        image = img["splash"]
        for x in range(0,9):
            image = resize(image, 1-x*0.1, 1-x*0.1)
            imageExp = ImageTk.PhotoImage(image)
            self.canvas.delete(self.rasp_logo)
            self.rasp_logo = self.canvas.create_image(960,540,image=imageExp,anchor=tkinter.CENTER)
            self.root.update()
    def start_wheel(self):
        self.wheel_items = {}
        self.canvas.create_image(0,0,image=expImg["small_logo"],anchor=tkinter.NW)
        self.canvas.create_image(960,540,image=expImg["plus"],anchor=tkinter.CENTER)
        #self.directions["shutdown"]=self.canvas.create_image(960,440,image=expIcons["Sshutdown"],anchor=tkinter.CENTER)
        #self.directions["netflix"]=self.canvas.create_image(860,540,image=expIcons["Snetflix"],anchor=tkinter.CENTER)
        #self.directions["kodi"]=self.canvas.create_image(1060,540,image=expIcons["Skodi"],anchor=tkinter.CENTER)
        #self.directions["firefox"]=self.canvas.create_image(960,640,image=expIcons["Sfirefox"],anchor=tkinter.CENTER)
        self.wheel_items["up"] = icon(expIcons["Sshutdown"],"u",self.canvas)
        self.wheel_items["down"] = icon(expIcons["Sfirefox"],"d",self.canvas)
        self.wheel_items["left"] = icon(expIcons["Snetflix"],"l",self.canvas)
        self.wheel_items["right"] = icon(expIcons["Skodi"],"r",self.canvas)
        self.selection = None
        keyboard.add_hotkey('up', root.up)
        keyboard.add_hotkey('down', root.down)
        keyboard.add_hotkey('left', root.left)
        keyboard.add_hotkey('right', root.right)
        keyboard.add_hotkey('enter', root.submit)
        self.root.mainloop()
    def up(self):
        self.selection = "up"
        self.wheel_items["down"].unselect()
        self.wheel_items["left"].unselect()
        self.wheel_items["right"].unselect()
        self.wheel_items["up"].select()
    def down(self):
        self.selection = "down"
        self.wheel_items["down"].select()
        self.wheel_items["left"].unselect()
        self.wheel_items["right"].unselect()
        self.wheel_items["up"].unselect()
    def left(self):
        self.selection = "left"
        self.wheel_items["down"].unselect()
        self.wheel_items["left"].select()
        self.wheel_items["right"].unselect()
        self.wheel_items["up"].unselect()
    def right(self):
        self.selection = "right"
        self.wheel_items["down"].unselect()
        self.wheel_items["left"].unselect()
        self.wheel_items["right"].select()
        self.wheel_items["up"].unselect()
    def submit(self):
        pass



            
        
img = {}
expImg = {}
icons = {}
expIcons = {}
root = window()
#image loading
if platform == "win32":
    img["small_logo"] = Image.open("img\\logo.png")
else:
    img["small_logo"] = Image.open("img/logo.png")
img["small_logo"] = resize(img["small_logo"],0.2,0.2)
expImg["small_logo"] = ImageTk.PhotoImage(img["small_logo"])
if platform == "win32":
    img["plus"] = Image.open("img\\plus.png")
else:
    img["plus"] = Image.open("img/plus.png")
expImg["plus"] = ImageTk.PhotoImage(img["plus"])

#icon loading
for x in os.listdir("icons"):
    name = x[0:len(x)-4]
    if platform == "win32":
        image = Image.open(f"icons\\{x}")
    else:
        image = Image.open(f"icons/{x}")
    image = image.resize((300,300))#might change when developing the ui
    icons[name] = image
    expIcons[name] = ImageTk.PhotoImage(icons[name])
    
    name = x[0:len(x)-4]
    if platform == "win32":
        image = Image.open(f"icons\\{x}")
    else:
        image = Image.open(f"icons/{x}")
    image = image.resize((100,100))#might change when developing the ui
    icons[f"S{name}"] = image
    expIcons[f"S{name}"] = ImageTk.PhotoImage(icons[f"S{name}"])
    
root.logo_disapear()
root.start_wheel()
root.root.mainloop()