import keyboard
import tkinter
from PIL import Image, ImageTk
import time
import os
os.chdir("/home/pi/piTV")
from sys import platform
def on_closing():
    pass


def resize(img, X, Y):
    resized = img.resize((round(img.size[0]*X), round(img.size[1]*Y)))
    return resized
warpzone_done = False
warpzone_exit = False
class warpzone:
    @staticmethod
    def start(canvas):
        keyboard.remove_all_hotkeys()
        secret_text1 = canvas.create_text(1000,100,fill="white",font="sans-serif 25",text="WELCOME TO WARP ZONE!")
        secret_text2 = canvas.create_text(1000,130,fill="white",font="sans-serif 25",text="press the key of the option you want to choose")
        secret_text3 = canvas.create_text(1000,160,fill="white",font="sans-serif 25",text="[W]at is dit? Waar is mijn Netflix gebleven?(druk op [W])")
        secret_text4 = canvas.create_text(1000,190,fill="white",font="sans-serif 25",text="[E]xlpore the desktop! Close this user-friendly menu!")
        secret_text5 = canvas.create_text(1000,220,fill="white",font="sans-serif 25",text="[T]ermial. Hackers only!")
        secret_text6 = canvas.create_text(1000,250,fill="white",font="sans-serif 25",text="[R]eboot! No, not reshoe.")
        canvas.update()
        warpzone.start_hotkeys()
        global warpzone_done
        global warpzone_exit
        while not warpzone_done:
            canvas.update()
            time.sleep(0.1)
        if warpzone_exit:
            exit()
        keyboard.remove_all_hotkeys()
        canvas.delete(secret_text1)
        canvas.delete(secret_text2)
        canvas.delete(secret_text3)
        canvas.delete(secret_text4)
        canvas.delete(secret_text5)
        canvas.delete(secret_text6)
    @staticmethod
    def exit():
        global warpzone_done
        warpzone_done = True
    @staticmethod
    def start_hotkeys():
        keyboard.add_hotkey("w",warpzone.exit)
        keyboard.add_hotkey("e",warpzone.close_app)
        keyboard.add_hotkey("t",warpzone.start_terminal)
        keyboard.add_hotkey("r",warpzone.reboot)
    @staticmethod
    def close_app():
        global warpzone_done
        global warpzone_exit
        warpzone_exit = True
        warpzone_done = True
        
    @staticmethod
    def start_terminal():
        print("term")
        os.system("su pi <<'END'\nlxterminal\nEND)")
    @staticmethod
    def reboot():
        os.system("sudo reboot")

class icon:
    def __init__(self,img,direction,canvas,command):
        self.command = command
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
                for _ in range(10):
                    self.canvas.move(self.id,0,-10)
                    time.sleep(0.001)
                self.y -=100
            elif self.direction == 'd':
                for _ in range(10):
                    self.canvas.move(self.id,0,10)
                    time.sleep(0.001)
                self.y += 100
        if self.x == self.x_init:
            if self.direction == 'l':
                for _ in range(10):
                    self.canvas.move(self.id,-10,0)
                    time.sleep(0.001)
                self.x -= 100
            elif self.direction == 'r':
                for _ in range(10):
                    self.canvas.move(self.id,10,0)
                    time.sleep(0.001)
                self.x += 100
    def unselect(self):
        if self.y != self.y_init:
            if self.direction == 'u':
                for _ in range(10):
                    self.canvas.move(self.id,0,10)
                    time.sleep(0.001)
                self.y += 100
            elif self.direction == 'd':
                for _ in range(10):
                    self.canvas.move(self.id,0,-10)
                    time.sleep(0.001)
                self.y -= 100
        if self.x != self.x_init:
            if self.direction == 'l':
                for _ in range(10):
                    self.canvas.move(self.id,10,0)
                    time.sleep(0.001)
                self.x += 100
            elif self.direction == 'r':
                for _ in range(10):
                    self.canvas.move(self.id,-10,0)
                    time.sleep(0.001)
                self.x -= 100
    def run(self):
        os.system(self.command)

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
        self.root.protocol("WM_DELETE_WINDOW", on_closing)
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
        if keyboard.is_pressed("d"):
            warpzone.start(self.canvas)
        self.wheel_items = {}
        self.canvas.create_image(0,0,image=expImg["small_logo"],anchor=tkinter.NW)
        self.canvas.create_image(960,540,image=expImg["plus"],anchor=tkinter.CENTER)
        #self.directions["shutdown"]=self.canvas.create_image(960,440,image=expIcons["Sshutdown"],anchor=tkinter.CENTER)
        #self.directions["netflix"]=self.canvas.create_image(860,540,image=expIcons["Snetflix"],anchor=tkinter.CENTER)
        #self.directions["kodi"]=self.canvas.create_image(1060,540,image=expIcons["Skodi"],anchor=tkinter.CENTER)
        #self.directions["firefox"]=self.canvas.create_image(960,640,image=expIcons["Sfirefox"],anchor=tkinter.CENTER)
        self.wheel_items["up"] = icon(expIcons["Sshutdown"],"u",self.canvas,"sudo shutdown now")
        self.wheel_items["down"] = icon(expIcons["Sfirefox"],"d",self.canvas,"su pi <<'END'\nfirefox-esr\nEND")
        self.wheel_items["left"] = icon(expIcons["Snetflix"],"l",self.canvas,"su pi <<'END'\nchromium-browser %U --kiosk --user-agent=\"Mozilla/5.0 (X11; CrOS armv7l 12371.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36\" www.netflix.com\nEND")
        self.wheel_items["right"] = icon(expIcons["Skodi"],"r",self.canvas,"su pi <<'END'\nkodi\nEND")
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
        self.wheel_items["left"].unselect()
        self.wheel_items["right"].unselect()
        self.wheel_items["up"].unselect()
        self.wheel_items["down"].select()
    def left(self):
        self.selection = "left"
        self.wheel_items["down"].unselect()
        self.wheel_items["right"].unselect()
        self.wheel_items["up"].unselect()
        self.wheel_items["left"].select()
    def right(self):
        self.selection = "right"
        self.wheel_items["down"].unselect()
        self.wheel_items["left"].unselect()
        self.wheel_items["up"].unselect()
        self.wheel_items["right"].select()

    def submit(self):
        if self.selection != None:
            keyboard.remove_all_hotkeys()
            self.wheel_items[self.selection].run()
            keyboard.add_hotkey('up', root.up)
            keyboard.add_hotkey('down', root.down)
            keyboard.add_hotkey('left', root.left)
            keyboard.add_hotkey('right', root.right)
            keyboard.add_hotkey('enter', root.submit)



            
        
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