#Question1
#We will be creating a UI APP of reddit unfunny version
from tkinter import * 


class Weddit_GUI:

    def __init__(self):
        self.tk=Tk()
        self.tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.Title = Label(self.tk, text="Welcome to Weddit!", font=("Comic Sans MS", 30, "bold"))
        self.Title.pack()

        self.Settings_Buttons = Button(self.frame, text="Settings")
        self.Genre_Buttons = Button(self.frame, text="Genre")
        self.Report_Buttons = Button(self.frame, text="Report")
        self.Settings_Buttons.pack()
        self.Genre_Buttons.pack()
        self.Report_Buttons.pack()

        #self.tk(self.ListOfButtons)
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    """
    def ListOfButtons(self): #For user going to different page/window

        self.Settings_Buttons = Button(self.topFrame, text="Settings")
        self.Genre_Buttons = Button(self.topFrame, text="Genre")
        self.Report_Buttons = Button(self.topFrame, text="Report")
    """
    def toggle_fullscreen(self, event=None): #"event=None" allows Toggle and end fullscreen script.
        self.state = not self.state  
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    Weddit = Weddit_GUI()
    Weddit.tk.mainloop()
