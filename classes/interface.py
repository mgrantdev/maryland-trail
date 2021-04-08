import os
import tkinter
from PIL import Image, ImageTk

class Interface(object):
    """handles graphical interface"""
    window = None
    loader = None
    window_width =  None
    window_height = None
    dynamic_frame = None
    scenes = {}

    def __init__(self, loader):
        # initalize window and loader
        self.window = tkinter.Tk()
        self.loader = loader
        window_width = self.window.winfo_screenwidth()
        window_height = self.window.winfo_screenheight()
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
        # create dynamic frame
        dynamic_frame = tkinter.Frame(self.window, bg="#1a1a1a")
        dynamic_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        # create welcome frame
        self.window.update() # updates window dimensions
        self.scenes['scene1'] = {}
        self.scenes['scene1']['frame'] = tkinter.Frame(dynamic_frame, bg="#1a1a1a")
        self.scenes['scene1']['frame'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
        self.scenes['scene1']['text'] = "Welcome to the Maryland Trail!\n\nOn your journey you will have the opportunity to explore the Old Line State\n in all of its grandeur, with YOU deciding what to explore and how to explore it.\n\nMake wise decisions and make the most of your trip.\n\nSafe travels!\n"
        self.scenes['scene1']['text_label'] = tkinter.Label(self.scenes['scene1']['frame'], bg="#1a1a1a", text=self.scenes['scene1']['text'], fg="#fff", font=("Arial", 20))
        self.scenes['scene1']['text_label'].pack()
        self.scenes['scene1']['continue_label'] = tkinter.Label(self.scenes['scene1']['frame'], bg="#1a1a1a", text="press <SPACE> to continue", fg="#fff", font=("Arial", 20))
        self.scenes['scene1']['continue_label'].place(relx=.15, rely=.9, relwidth=.7)
        # finish window creation
        self.window.mainloop()


    # close window
    def close(self):
        self.window.destroy()

    # hide all pages during navigation
    def hide_frames(self):
        for page in self.pages:
            self.pages[page].place_forget()

    # navigate to page
    def open_page(self, page_to_open):
        self.hide_frames()
        self.pages[page_to_open].place(relwidth=1, relheight=1)
