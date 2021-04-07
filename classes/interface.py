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
    pages = {}

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
        maryland_welcome_sign = Image.open(filepath)
        maryland_welcome_sign = maryland_welcome_sign.resize((round(window_width * 0.1), round(window_height * 0.2)), Image.ANTIALIAS)
        maryland_welcome_sign_tk = ImageTk.PhotoImage(maryland_welcome_sign)
        image_label = tkinter.Label(image=maryland_welcome_sign_tk, borderwidth=0)
        image_label.image = maryland_welcome_sign_tk
        image_label.place(relx=0.05, rely=0.05)
        title_label = tkinter.Label(bg="#000", text="The Maryland Trail", fg="#fff", font=("Arial", 20))
        self.window.update()
        title_label.place(x=(toolbar_frame.winfo_width() - image_label.winfo_width())/4, y=round(window_height * 0.2) + round(window_height * 0.05) + 5)
        # create dynamic frame
        dynamic_frame = tkinter.Frame(self.window, bg="#1a1a1a")
        dynamic_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        # create welcome frame
        self.window.update()
        self.pages['welcome'] = tkinter.Frame(dynamic_frame, bg="#1a1a1a")
        self.pages['welcome'].place(relx=0.1, rely=0.1, relwidth=0.8, relheight=.9)
        welcome_text = "Welcome to the Maryland Trail!\n\nOn your journey you will have the opportunity to explore the Old Line State\n in all of its grandeur, with YOU deciding what to explore and how to explore it.\n\nMake wise decisions and make the most of your trip.\n\nSafe travels!\n"
        welcome_text_1 = tkinter.Label(self.pages['welcome'], bg="#1a1a1a", text=welcome_text, fg="#fff", font=("Arial", 20))
        welcome_text_1.pack()
        continue_label = tkinter.Label(self.pages['welcome'], bg="#1a1a1a", text="press <SPACE> to continue", fg="#fff", font=("Arial", 20))
        continue_label.place(relx=.15, rely=.9, relwidth=.7)
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
