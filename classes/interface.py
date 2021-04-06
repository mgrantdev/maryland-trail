import tkinter

class Interface(object):
    """handles graphical interface"""
    window = None
    loader = None
    pages = {}

    def __init__(self, loader):
        # initalize window and loader
        self.window = tkinter.Tk()
        self.loader = loader
        # set window properties
        self.window.attributes('-fullscreen', True)
        # create main frame
        self.pages['main'] = tkinter.Frame(self.window, bg="#8ce4ff")
        self.pages['main'].place(relwidth=1, relheight=1)
        # create menu frame (toolbar)
        toolbar_frame = tkinter.Frame(self.window, bg="#000")
        toolbar_frame.place(relwidth=.1, relheight=1)
        toolbar_buttons = {}
        toolbar_buttons['exit'] = tkinter.Button(toolbar_buttons, text = 'exit', command=self.close)
        toolbar_buttons['exit'].place(relwidth=0.09, relheight=0.05, relx=0.005, rely=0.9)
        # create dynamic frame
        dynamic_frame = tkinter.Frame(self.window, bg="red")
        dynamic_frame.place(relx=0.125, rely=0.03, relwidth=0.85, relheight=0.94)
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
