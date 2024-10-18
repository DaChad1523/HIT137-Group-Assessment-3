#Question1
#We will be creating a UI APP of reddit unfunny version
import tkinter as tk
from tkinter import font
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
#Ignore the above ^
class Weddit_UIv2:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.title("Weddit UI V2")
        self.tk.geometry('1600x1000')
        self.orange_line()
        self.Titles()
        self.orange_line()
        self.Buttons()
        self.create_entry_area()
        self.Display_Feed()

    #Draw an orange line on top
    def orange_line(self, num_lines=5, lines_height=5):
        for _ in range (num_lines):
            lines = tk.Frame(self.tk, bg='orange', height=lines_height)
            lines.pack(side="top", fill='x')
    #Title placed above the top and below orange line
    def Titles(self):
        title_font = font.Font(family='Comic Sans MS', size=30, weight='bold')
        title_label = tk.Label(self.tk, text="Welcome to WedditV2", font=title_font, bg='white')
        title_label.pack(side='top', fill='x')

    #Useless buttons...
    def Buttons(self):
        Button_frame = tk.Frame(self.tk)
        Button_frame.pack(side='top', anchor='w')

        button1 = tk.Button(Button_frame, text= 'Settings')
        button1.pack(side='left', padx=5)

        button2 = tk.Button(Button_frame, text= 'Home')
        button2.pack(side='left', padx=5)

        button3 = tk.Button(Button_frame, text= '???', command=self.tk.destroy)
        button3.pack(side='left', padx=5)

    #A box allows you to type and post it on a display feed
    def create_entry_area(self):
        entry_frame = tk.Frame(self.tk)
        entry_frame.pack(side='top', fill='none', padx=10, pady=10)

        self.post_entry = tk.Text(entry_frame, height=5, width=800, wrap='word')
        self.post_entry.pack(side='top', fill='none', expand=True, padx=10, pady=10)

        Post_Button = tk.Button (text= 'Post', command=self.Submit)
        Post_Button.pack(side='top', padx=10, pady= 10)


    def Display_Feed(self):
        Display_Feed = tk.Frame(self.tk)
        Display_Feed.pack(side='bottom', fill='none', padx= 10, pady= 10)

        self.Display = tk.Text(Display_Feed, height=500, width=500, wrap='word')
        self.Display.pack(side='bottom', fill='none', expand=False)
    
    def Submit(self):
        post = self.post_entry.get('1.0', tk.END)
        self.Display.config(state='normal')
        self.Display.insert(tk.END, f"You: {post}\n")
        self.Display.config(state='disabled')
        self.post_entry.delete('1.0', tk.END)



if __name__ == '__main__':
    Weddit_UI = Weddit_UIv2()
    Weddit_UI.tk.mainloop()


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