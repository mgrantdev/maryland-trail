import os
import keyboard
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox

class Interface(object):
    """handles graphical interface"""
    window = None
    loader = None
    window_width =  None
    window_height = None
    dynamic_frame = None
    scenes = {}
    players = {}

    def __init__(self, loader):
        # initalize window and loader
        self.window = tkinter.Tk()
        self.loader = loader
        window_width = self.window.winfo_screenwidth()
        window_height = self.window.winfo_screenheight()
        # create dynamic frame
        self.dynamic_frame = tkinter.Frame(self.window, bg="#1a1a1a")
        self.dynamic_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        # set window properties
        self.window.attributes('-fullscreen', True)
        # create menu frame (toolbar)
        toolbar_frame = tkinter.Frame(self.window, bg="#000")
        toolbar_frame.place(relwidth=.2, relheight=1)
        toolbar_buttons = {}
        toolbar_buttons['exit'] = tkinter.Button(toolbar_buttons, text = 'exit', command=self.close)
        toolbar_buttons['exit'].place(relwidth=0.18, relheight=0.05, relx=0.005, rely=0.9)
        # toolbar image
        current_dir = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(current_dir, "../bin/images/welcome_maryland.png")
        toolbar_buttons['image'] = {}
        toolbar_buttons['image']['welcome_sign'] = Image.open(filepath)
        toolbar_buttons['image']['welcome_sign'] = toolbar_buttons['image']['welcome_sign'].resize((round(window_width * 0.1), round(window_height * 0.2)), Image.ANTIALIAS)
        toolbar_buttons['image']['welcome_sign_widget'] = ImageTk.PhotoImage(toolbar_buttons['image']['welcome_sign'])
        toolbar_buttons['image']['label'] = tkinter.Label(image=toolbar_buttons['image']['welcome_sign_widget'], borderwidth=0)
        toolbar_buttons['image']['label'].image = toolbar_buttons['image']['welcome_sign_widget']
        toolbar_buttons['image']['label'].place(relx=0.05, rely=0.05)
        toolbar_buttons['image']['heading'] = tkinter.Label(bg="#000", text="The Maryland Trail", fg="#fff", font=("Arial", 20))
        self.window.update() # updates window dimensions
        toolbar_buttons['image']['heading'].place(x=(toolbar_frame.winfo_width() - toolbar_buttons['image']['label'].winfo_width())/4, y=round(window_height * 0.2) + round(window_height * 0.05) + 5)
        # create scene 1 (game intro)
        self.window.update() # updates window dimensions
        self.scenes['scene1'] = {}
        self.scenes['scene1']['frame'] = tkinter.Frame(self.dynamic_frame, bg="#1a1a1a")
        self.scenes['scene1']['frame'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
        self.scenes['scene1']['text'] = "Welcome to the Maryland Trail!\n\nOn your journey you will have the opportunity to explore the Old Line State\n in all of its grandeur, with YOU deciding what to explore and how to explore it.\n\nMake wise decisions and make the most of your trip.\n\nSafe travels!\n"
        self.scenes['scene1']['text_label'] = tkinter.Label(self.scenes['scene1']['frame'], bg="#1a1a1a", text=self.scenes['scene1']['text'], fg="#fff", font=("Arial", 20))
        self.scenes['scene1']['text_label'].pack()
        self.scenes['scene1']['continue_label'] = tkinter.Label(self.scenes['scene1']['frame'], bg="#1a1a1a", text="CLICK HERE TO CONTINUE", fg="#fff", font=("Arial", 20))
        self.scenes['scene1']['continue_label'].bind( "<Button>", lambda e:self.open_scene('scene2'))  
        self.scenes['scene1']['continue_label'].place(relx=.15, rely=.9, relwidth=.7)
        # create scene 2 (player count)
        self.window.update() # updates window dimensions
        self.scenes['scene2'] = {}
        self.scenes['scene2']['frame'] = tkinter.Frame(self.dynamic_frame, bg="#1a1a1a")
        self.scenes['scene2']['frame'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
        self.scenes['scene2']['text'] = "How many people will be traveling with you?\n\nPlease enter a value between 0-7"
        self.scenes['scene2']['text_label'] = tkinter.Label(self.scenes['scene2']['frame'], bg="#1a1a1a", text=self.scenes['scene2']['text'], fg="#fff", font=("Arial", 20))
        self.scenes['scene2']['text_label'].pack()
        self.scenes['scene2']['continue_label'] = tkinter.Label(self.scenes['scene2']['frame'], bg="#1a1a1a", text="CLICK HERE TO CONTINUE", fg="#fff", font=("Arial", 20))
        self.scenes['scene2']['input1'] = tkinter.Entry(self.scenes['scene2']['frame'], fg="#fff", bg="#1a1a1a", borderwidth=1, relief="sunken", font=("Arial", 16), justify="center")
        self.scenes['scene2']['input1'].place(relx=0.35, rely=0.2, relheight=0.08, relwidth=0.3)
        self.scenes['scene2']['continue_label'].bind( "<Button>", lambda e:self.create_players())  
        self.scenes['scene2']['continue_label'].place(relx=.15, rely=.9, relwidth=.7)
        self.scenes['scene2']['frame'].place_forget()
        # finish window creation
        self.window.mainloop()


    # close window
    def close(self):
        self.window.destroy()

    # hide all pages during navigation
    def hide_frames(self):
        for scene in self.scenes:
            self.scenes[scene]['frame'].place_forget()

    # creates (and validates number of) players (scene2)
    def create_players(self):
        if(not self.scenes['scene2']['input1'].get().isnumeric()):
            messagebox.showinfo("Oops!", "Please enter a valid number")
        else:
            if(int(self.scenes['scene2']['input1'].get()) > 7 and int(self.scenes['scene2']['input1'].get()) < 0):
                messagebox.showinfo("Oops!", "Please enter a number from 0-7")
            else:
                # if all conditions met, create outline for players
                players_created = 0
                while(players_created < int(self.scenes['scene2']['input1'].get())):
                    self.players[players_created] = {}
                    self.players[players_created]['id'] = players_created
                    players_created += 1
                self.name_players()

    # name players (scene 3)
    def name_players(self):
        if(len(self.players) > 0):
            self.scenes['scene3'] = {}
            self.scenes['scene3']['frame'] = tkinter.Frame(self.dynamic_frame, bg="#1a1a1a")
            self.scenes['scene3']['frame'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
            self.scenes['scene3']['text'] = "What are the names of your passengers?"
            self.scenes['scene3']['text_label'] = tkinter.Label(self.scenes['scene3']['frame'], bg="#1a1a1a", text=self.scenes['scene3']['text'], fg="#fff", font=("Arial", 20))
            self.scenes['scene3']['text_label'].pack()
            self.scenes['scene3']['continue_label'] = tkinter.Label(self.scenes['scene3']['frame'], bg="#1a1a1a", text="CLICK HERE TO CONTINUE", fg="#fff", font=("Arial", 20))
            for x in self.players:
                self.scenes['scene3']['input' + str(x)] = tkinter.Entry(self.scenes['scene3']['frame'], fg="#fff", bg="#1a1a1a", borderwidth=1, relief="sunken", font=("Arial", 16), justify="center")
                self.scenes['scene3']['input' + str(x)].place(relx=0.3, rely=0.2 + (x * .08), relheight=0.08, relwidth=0.4)
            self.scenes['scene3']['continue_label'].bind("<Button>", lambda e:self.open_scene("scene4"))  
            self.scenes['scene3']['continue_label'].place(relx=.15, rely=.9, relwidth=.7)

    # navigate to page
    def open_scene(self, scene_to_open):
        self.hide_frames()
        self.scenes[scene_to_open]['frame'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
