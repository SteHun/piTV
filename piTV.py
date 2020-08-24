import keyboard
import tkinter
from PIL import Image, ImageTk
import time
import os



def resize(img, X, Y):
    resized = img.resize((round(img.size[0]*X), round(img.size[1]*Y)))
    return resized

        

class window:
    def __init__(self):
        global img
        global expImg
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
        self.canvas.create_image(0,0,image=expImg["small_logo"],anchor=tkinter.NW)
            
        
img = {}
expImg = {}
icons = {}
expIcons = {}
root = window()
#image loading
img["small_logo"] = Image.open("img/logo.png")#change this for a windows port
img["small_logo"] = resize(img["small_logo"],0.2,0.2)
expImg["small_logo"] = ImageTk.PhotoImage(img["small_logo"])

#icon loading
for x in os.listdir("icons"):
    name = x[0:len(x)-4]
    image = Image.open(f"icons/{x}")#change this for a windows port
    image = image.resize((300,300))#might change when developing the ui
    icons[name] = image
    expIcons[name] = ImageTk.PhotoImage(icons[name])
    
    name = x[0:len(x)-4]
    image = Image.open(f"icons/{x}")#change this for a windows port
    image = image.resize((100,100))#might change when developing the ui
    icons[f"S{name}"] = image
    expIcons[f"S{name}"] = ImageTk.PhotoImage(icons[f"S{name}"])
    
root.logo_disapear()