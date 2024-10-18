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

Question 1_Epic Calculator Converter

The calculator converter gui code script creates a graphical user interface (GUI) for a measurement converter application using the Tkinter library. The application allows users to convert metric measurements between different units such as millimeters (mm), centimeters (cm), meters (m), and kilometers (km). The code is organized into several classes and methods to handle the conversion logic and GUI components.
Functionality:
1.	Importing Libraries: 
o	The code starts by importing the necessary libraries: tkinter for creating the GUI and tkinter.messagebox for displaying error messages.

3.	MetricMeasurementConverter Class: 
o	This class contains static methods for converting metric measurements between different units.

o	Each method takes a value as input and returns the converted value based on the specific conversion formula.

o	The @staticmethod decorator is used to indicate that these methods can be called without creating an instance of the class.

5.	ImperialMeasurementConverter Class: 
o	This class is similar to the MetricMeasurementConverter class but is intended for imperial measurement conversions.

o	It includes static methods for converting between inches, feet, and miles.

o	However, the code for this class is commented out, indicating that it is a work in progress and not currently utilized in the application.

7.	ConverterApp Class: 
o	This class represents the main application window and inherits from the Tk class provided by Tkinter.

o	The __init__ method is the constructor for the class, which initializes the window, sets its title and size, and calls the create_widgets method to create the GUI components.

o	The create_widgets method is responsible for creating and arranging the various widgets (labels, entry fields, comboboxes, and buttons) in the application window using the Tkinter grid layout system.

o	The MetricConvert method is called when the "Convert" button is clicked. It retrieves the user input values, determines the appropriate conversion method based on the selected units, and updates the result label with the converted value.

o	If an invalid conversion is attempted or an error occurs, an error message is displayed using the showerror function from tkinter.messagebox.

o	The code for the ImperialConvert method is commented out, indicating that it is not currently implemented.

9.	Main Program: 
o	The if __name__ == "__main__": block is the entry point of the program.

o	It creates an instance of the ConverterApp class, which initializes the application window and starts the main event loop using the mainloop method.

o	The mainloop method keeps the application running and responsive to user interactions until the window is closed.

The code follows a modular and object-oriented approach, separating the conversion logic into separate classes (MetricMeasurementConverter and ImperialMeasurementConverter) and encapsulating the GUI functionality within the ConverterApp class. This design allows for easy extensibility and maintainability of the code.

The GUI is created using the Tkinter library, which provides a set of widgets and tools for building graphical interfaces in Python. The code utilizes labels, entry fields, comboboxes, and buttons to create an intuitive and user-friendly interface for performing measurement conversions.

The MetricConvert method handles the actual conversion process based on the user's input. It retrieves the entered value, the selected "from" unit, and the selected "to" unit. It then determines the appropriate conversion method to call from the MetricMeasurementConverter class based on the selected units. If a valid conversion is found, the result is displayed in the result label. If an invalid conversion is attempted or an error occurs, an error message is shown using the showerror function.

Overall, this code provides a functional and interactive measurement converter application with a graphical user interface. It demonstrates the use of Tkinter for creating GUI elements, handling user input, and displaying results. The code is well-structured and follows good practices such as using classes, static methods, and error handling. However, it is important to note that the imperial conversion functionality is currently commented out and not fully implemented in this version of the code.


