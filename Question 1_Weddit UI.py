#Question1
#We will be creating a UI APP of reddit unfunny version
import tkinter as tk
"""

class Weddit_GUI:

    def __init__(self):
        self.tk=Tk()
        self.tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.Title = Label(self.tk, text="Welcome to Weddit!", font=("Comic Sans MS", 30, "bold"))
        self.Title.pack(pady=10)

        self.Settings_Buttons = Button(self.tk, text="Settings")
        self.Genre_Buttons = Button(self.tk, text="Genre")
        self.Report_Buttons = Button(self.tk, text="Report")
        self.Settings_Buttons.pack(pady=10)
        self.Genre_Buttons.pack(pady=10)
        self.Report_Buttons.pack(pady=10)

        #self.tk(self.ListOfButtons)
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

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
"""
class Weddit_UIv2():
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.title("Weddit UI ")
        self.tk.geometry('800x600')


"""
root = tk.Tk()
root.title("YouTube-like Interface")
root.geometry("800x600")

# Navigation Bar
nav_bar = tk.Frame(root, bg="red", height=50)
nav_bar.pack(side="top", fill="x")

search_bar = tk.Entry(nav_bar, width=50)
search_bar.pack(side="left", padx=10, pady=10)

search_button = tk.Button(nav_bar, text="Search")
search_button.pack(side="left", padx=10, pady=10)

# Video Display Area
video_frame = tk.Frame(root, bg="black")
video_frame.pack(side="top", fill="both", expand=True)

video_label = tk.Label(video_frame, text="Video Display Area", bg="black", fg="white")
video_label.pack(expand=True)

# Sidebar
sidebar = tk.Frame(root, bg="gray", width=200)
sidebar.pack(side="left", fill="y")

home_button = tk.Button(sidebar, text="Home")
home_button.pack(pady=10)

subscriptions_button = tk.Button(sidebar, text="Subscriptions")
subscriptions_button.pack(pady=10)

root.mainloop()
"""