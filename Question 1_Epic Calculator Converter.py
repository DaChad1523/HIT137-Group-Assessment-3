#Question1 Creating a UI that can convert any conversion
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
#For Metric Conversion Only
class MetricMeasurementConverter:
    @staticmethod #staticmethod means that it cannot be modified within the class
    def mm_to_cm(x):
        return x / 10
    
    @staticmethod
    def cm_to_m(x):
        return x / 100

    @staticmethod
    def m_to_km(x):
        return x / 1000
    
    @staticmethod
    def km_to_m(x):
        return x * 1000

    @staticmethod
    def m_to_cm(x):
        return x * 100

    @staticmethod
    def cm_to_mm(x):
        return x * 10

#For Imperial Conversion Only | Feel free to expand!
class ImperialMeasurementConverter:
    @staticmethod 
    def Inch_to_Foot(x):
        return x / 12
    @staticmethod 
    def Foot_to_Mile(x):
        return x / 5280
    @staticmethod 
    def Mile_to_Foot(x):
        return x * 5280
    @staticmethod 
    def Foot_to_Inch(x):
        return x * 12

class ConverterApp(Tk):
    def __init__(self):
        super().__init__() #super aka secondary class or child class
        self.title("Your Average Measurement Converter")
        self.geometry('800x400') #Had to make it little bigger as on the left is metric, center in imperial and right would be you guys for something to add
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        #For Metric Conversion
        self.Mvalue_label = ttk.Label(self, text="Value:") #Added Top Left
        self.Mvalue_label.grid(column=0, row=0, padx=10, pady=10)

        self.Mvalue_entry = ttk.Entry(self) #Added next to value that allow user input
        self.Mvalue_entry.grid(column=1, row=0, padx=10, pady=10)

        self.from_unit_label = ttk.Label(self, text="From Unit:") #Same thing but below it
        self.from_unit_label.grid(column=0, row=1, padx=10, pady=10)

        self.from_unit = StringVar() #Allow user to choose which measurement they can convert from
        self.from_unit_combobox = ttk.Combobox(self, textvariable=self.from_unit)
        self.from_unit_combobox['values'] = ('mm', 'cm', 'm', 'km')
        self.from_unit_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.to_unit_label = ttk.Label(self, text="To Unit:")
        self.to_unit_label.grid(column=0, row=2, padx=10, pady=10)

        self.to_unit = StringVar() #This box can output
        self.to_unit_combobox = ttk.Combobox(self, textvariable=self.to_unit)
        self.to_unit_combobox['values'] = ('mm', 'cm', 'm', 'km')
        self.to_unit_combobox.grid(column=1, row=2, padx=10, pady=10)

        self.convert_button = ttk.Button(self, text="Convert", command=self.MetricConvert)
        self.convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self, text="") #poop out the result located botton of the convert
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        #For Imperial Conversion (WIP)
        self.Ivalue_label = ttk.Label(self, text="Value:")
        self.Ivalue_label.grid(column=3, row=0, padx=10, pady=10)
        
        self.Ivalue_entry = ttk.Entry(self)
        self.Ivalue_entry.grid(column=4, row=0, padx=10, pady=10)
        
        self.from_unit_label = ttk.Label(self, text="From Unit:")
        self.from_unit_label.grid(column=3, row=1, padx=10, pady=10)

        self.from_unit = StringVar()
        self.from_unit_combobox = ttk.Combobox(self, textvariable=self.from_unit)
        self.from_unit_combobox['values'] = ('Inch', 'Foot', 'Mile')
        self.from_unit_combobox.grid(column=4, row=1, padx=10, pady=10)

        self.to_unit_label = ttk.Label(self, text="To Unit:")
        self.to_unit_label.grid(column=3, row=2, padx=10, pady=10)

        self.to_unit = StringVar() #This box can output
        self.to_unit_combobox = ttk.Combobox(self, textvariable=self.to_unit)
        self.to_unit_combobox['values'] = ('Inch', 'Foot', 'Mile')
        self.to_unit_combobox.grid(column=4, row=2, padx=10, pady=10)

        self.convert_button = ttk.Button(self, text="Convert", command=self.ImperialConvert)
        self.convert_button.grid(column=3, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self, text="") #poop out the result located botton of the convert
        self.result_label.grid(column=4, row=4, columnspan=2, padx=10, pady=10)




    def MetricConvert(self): #Bunch of methods and calculation
        try:
            value = float(self.Mvalue_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            if from_unit == 'mm' and to_unit == 'cm':
                result = MetricMeasurementConverter.mm_to_cm(value)
            elif from_unit == 'cm' and to_unit == 'm':
                result = MetricMeasurementConverter.cm_to_m(value)
            elif from_unit == 'm' and to_unit == 'km':
                result = MetricMeasurementConverter.m_to_km(value)
            elif from_unit == 'km' and to_unit == 'm':
                result = MetricMeasurementConverter.km_to_m(value)
            elif from_unit == 'm' and to_unit == 'cm':
                result = MetricMeasurementConverter.m_to_cm(value)
            elif from_unit == 'cm' and to_unit == 'mm':
                result = MetricMeasurementConverter.cm_to_mm(value)
            else:
                raise ValueError("Invalid conversion")

            self.result_label.config(text=f"Result: {result} {to_unit}")
        except ValueError as e:
            showerror(title="Error", message=str(e))

    def ImperialConvert(self):
        try:
            value = float(self.Ivalue_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            if from_unit == 'Inch' and to_unit == 'Foot':
                result = ImperialMeasurementConverter.Inch_to_Foot(value)
            elif from_unit == 'Foot' and to_unit == 'Mile':
                result = ImperialMeasurementConverter.Foot_to_Mile(value)
            elif from_unit == 'Mile' and to_unit == 'Foot':
                result = ImperialMeasurementConverter.Mile_to_Foot(value)
            elif from_unit == 'Foot' and to_unit == 'Inch':
                result = ImperialMeasurementConverter.Mile_to_Foot(value)
            else:
                raise ValueError("Invalid conversion")

            self.result_label.config(text=f"Result: {result} {to_unit}")
        except ValueError as e:
            showerror(title="Error", message=str(e))

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop() #Keep it opened
