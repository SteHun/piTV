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
        img["logo"] = Image.open("img/logo.png")
        img["logo"] = resize(img["logo"], 0.5, 0.5)
        
        
        self.root = tkinter.Tk()
        expImg["logo"] = ImageTk.PhotoImage(img["logo"])
        self.root.attributes("-fullscreen", True)
        self.canvas = tkinter.Canvas(self.root, width=1920, height= 1080, highlightthickness=0, bg="blue")
        self.rasp_logo = self.canvas.create_image(960,540, image=expImg["logo"], anchor = tkinter.CENTER)
        self.canvas.pack()
        self.root.update()
    
    def logo_disapear(self):
        image = img["logo"]
        for x in range(0,9):
            image = resize(image, 1-x*0.1, 1-x*0.1)
            imageExp = ImageTk.PhotoImage(image)
            self.canvas.delete(self.rasp_logo)
            print(x)
            self.rasp_logo = self.canvas.create_image(960,540,image=imageExp,anchor=tkinter.CENTER)
            self.root.update()
        

                
        
img = {}
expImg = {}
root = window()
for x in os.listdir("img"):
    if x != "logo.png":
        name = x[0:len(x)-4]
        original = Image.open(f"img/{x}")
        img[f"S{name}"] = resize(original, 0.25, 0.25)
        expImg[f"S{name}"] = ImageTk.PhotoImage(img[f"S{name}"])
        
        img[name] = original
        expImg[name] = ImageTk.PhotoImage(img[name])
root.logo_disapear()
tkinter.mainloop()