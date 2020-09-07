import keyboard
import tkinter
from PIL import Image, ImageTk
import time
import os
from sys import platform



def resize(img, X, Y):
    resized = img.resize((round(img.size[0]*X), round(img.size[1]*Y)))
    return resized

        

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
        self.canvas.create_image(0,0,image=expImg["small_logo"],anchor=tkinter.NW)
        self.canvas.create_image(960,540,image=expImg["plus"],anchor=tkinter.CENTER)
        
            
        
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