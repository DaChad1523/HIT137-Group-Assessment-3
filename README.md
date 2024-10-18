# HIT137-Group-Assessment-3 Report
Question 1_Weddit UI
The Weddit_UIv2 class represents a graphical user interface (GUI) for a Reddit-like application called "Weddit." The class is implemented using the Tkinter library, which is a standard GUI library for Python.
The init method is the constructor of the class, and it initializes the main window of the application. It sets the window title to "Weddit UI V2" and sets the window size to 1600x1000 pixels. The constructor then calls several methods to create different components of the user interface.
The orange_line method is responsible for drawing orange lines at the top of the window. It takes two optional parameters: num_lines, which specifies the number of lines to draw (default is 5), and lines_height, which specifies the height of each line (default is 5). The method creates a frame for each line, sets its background color to orange, and packs it at the top of the window using the pack geometry manager with the fill='x' option to make the lines stretch horizontally.
The Titles method creates a title label for the application. It uses the font module to create a font object with the Comic Sans MS font family, size 30, and bold weight. It then creates a label widget with the text "Welcome to WedditV2," sets the font to the created font object, and sets the background color to white. The label is packed at the top of the window using the pack geometry manager with the fill='x' option to make it stretch horizontally.
The Buttons method creates a frame for holding buttons and packs it at the top of the window, aligned to the left side using the anchor='w' option. It creates three buttons: "Settings," "Home," and "???" (which closes the application when clicked). The buttons are created using the Button widget and are packed within the button frame using the pack geometry manager with the side='left' option to arrange them horizontally. The padx option is used to add horizontal padding between the buttons.
The create_entry_area method creates an entry area where users can type and post messages. It creates a frame called entry_frame and packs it at the top of the window using the pack geometry manager with the fill='none' option to prevent it from expanding. Inside the entry frame, it creates a Text widget called post_entry with a height of 5 lines and a width of 800 pixels. The wrap='word' option is used to wrap the text at word boundaries. The post_entry widget is packed within the entry frame using the pack geometry manager with the fill='none' and expand=True options to allow it to expand vertically. It also adds horizontal and vertical padding using the padx and pady options. Finally, it creates a "Post" button below the entry area, which triggers the Submit method when clicked.
The Display_Feed method creates a frame called Display_Feed and packs it at the bottom of the window using the pack geometry manager with the fill='none' option. Inside the Display_Feed frame, it creates a Text widget called Display with a height of 500 lines and a width of 500 pixels. The wrap='word' option is used to wrap the text at word boundaries. The Display widget is packed within the Display_Feed frame using the pack geometry manager with the fill='none' and expand=False options to prevent it from expanding.
The Submit method is called when the "Post" button is clicked. It retrieves the text entered in the post_entry widget using the get method, specifying the range from the first line (1.0) to the end of the text (tk.END). It then configures the Display widget to be in the normal state (allowing modifications), inserts the retrieved text at the end of the Display widget, and appends a newline character. After inserting the text, it configures the Display widget back to the disabled state to prevent further modifications. Finally, it clears the content of the post_entry widget using the delete method.
The if name == 'main': block at the end of the code is the entry point of the program. It creates an instance of the Weddit_UIv2 class called Weddit_UI and starts the main event loop of the Tkinter application by calling the mainloop method on the tk attribute of the Weddit_UI instance. This allows the application to run and respond to user interactions until it is closed.
Overall, the Weddit_UIv2 class provides a basic user interface for a Reddit-like application. It includes a title, buttons for navigation, an entry area for posting messages, and a display area to show the posted messages. The code demonstrates the usage of various Tkinter widgets such as Frame, Label, Button, Text, and the pack geometry manager to arrange the widgets within the window. It also showcases how to retrieve and insert text into the Text widget and how to enable/disable the widget state.
