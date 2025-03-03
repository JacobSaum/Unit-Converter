import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def round_to_significant_figures(number, sig_figures):
    if number == 0:
        return 0  # Handle zero case
    # Use scientific notation to round to significant figures
    return round(number, sig_figures - 1 - int(math.floor(math.log10(abs(number)))))

# Define unit options for each category
unit_options = {
    "distance": ["Meters", "Feet", "Inches", "Kilometers", "Miles", "Yards", "Centimeters", "Millimeters", "Nautical Miles"],

    "mass": ["Kilograms", "Pounds", "Ounces", "Grams", "Tons", "Milligrams", "Stones"],

    "volume": ["Liters", "Gallons", "Milliliters", "Cubic Meters", "Cubic Feet", "Cups", "Pints", "Quarts", "Fluid Ounces"],    

    "temperature": ["Celsius", "Fahrenheit", "Kelvin"],

    "time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"],

    "speed": ["Meters per Second", "Kilometers per Hour", "Miles per Hour",  "Knots"],

    "energy": ["Joules", "Kilojoules", "Calories", "Kilowatt-Hours"],

    "pressure": ["Pascals", "Bars", "Atmospheres"],

    "area": ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres", "Hectares"]
}

unit_symbol_options = {
    "distance": {"Meters": "m","Feet": "ft","Inches": "in","Kilometers": "km","Miles": "mi","Yards": "yd","Centimeters": "cm","Millimeters": "mm","Nautical Miles": "nmi"
    },
    "mass": {"Kilograms": "kg","Pounds": "lbs","Ounces": "oz","Grams": "g","Tons": "t","Milligrams": "mg","Stones": "st"
    },
    "volume": {"Liters": "L","Gallons": "gal","Milliliters": "ml","Cubic Meters": "m^3","Cubic Feet": "ft^3","Cups": "c","Pints": "pt","Quarts": "qt","Fluid Ounces": "fl oz"
    },
    "temperature": {"Celsius": "°C","Fahrenheit": "°F","Kelvin": "K"
    },
    "time": {"Seconds": "s","Minutes": "mins","Hours": "hrs","Days": "days","Weeks": "weeks","Months": "months","Years": "yrs"
    },
    "speed": {"Meters per Second": "m/s","Kilometers per Hour": "km/hr","Miles per Hour": "mph","Knots": "kn"
    },
    "energy": {"Joules": "J","Kilojoules": "kJ","Calories": "cal","Kilowatt-Hours": "kW h"
    },
    "pressure": {"Pascals": "Pa","Bars": "bar","Atmospheres": "atm"
    },
    "area": {"Square Meters": "m^2", "Square Kilometers": "km^2","Square Feet": "ft^2","Square Miles": "mi^2","Acres": "ac","Hectares": "ha"
    }
}


def update_unit_menus(*args):
    """Update the unit menus based on the selected radio button."""
    selected_category = radio_var.get()  # Get the selected radio button value
    if selected_category in unit_options:
        # Update the options in the unit menus
        unit_menu1.configure(values=unit_options[selected_category])
        unit_menu2.configure(values=unit_options[selected_category])
        # Reset the selected option to the first item in the list
        unit_menu1.set(unit_options[selected_category][0])
        unit_menu2.set(unit_options[selected_category][1])  # Default to the second option for "Convert to"

def errorMessage(errorMsg):
        resultLabel.configure(text=errorMsg, text_color = "red", font = ("Roboto",16))  # Update the resultLabel

def convert():
    convertFrom = unit_menu1.get()
    convertTo = unit_menu2.get()
    error = False
    errorMsg = ""
    resultLabel.configure(text=errorMsg, text_color = "white", font = ("Roboto",24))

    try:
        value = float(entry1.get())

        if convertFrom == convertTo:
            errorMsg = "Error: Unit must be different!"
            error = True
        else:
            convertLength(convertFrom, convertTo, value)

    except ValueError:
        errorMsg = "Error: A number must be entered!"
        error = True

    if error:
        errorMessage(errorMsg)
     

def convertLength(convertFrom, convertTo, value):
    category = radio_var.get()
    conversion_factors = {
    "distance": {
        "Meters": {"Feet": 3.28084, "Miles": 0.000621371, "Inches": 39.3701, "Kilometers": 0.001, "Yards": 1.09361, "Centimeters": 100, "Millimeters": 1000, "Nautical Miles": 0.000539957},
        "Feet": {"Meters": 0.3048, "Miles": 0.000189394, "Inches": 12, "Kilometers": 0.0003048, "Yards": 0.333333, "Centimeters": 30.48, "Millimeters": 304.8, "Nautical Miles": 0.000164579},
        "Miles": {"Meters": 1609.34, "Feet": 5280, "Inches": 63360, "Kilometers": 1.60934, "Yards": 1760, "Centimeters": 160934, "Millimeters": 1609340, "Nautical Miles": 0.868976},
        "Inches": {"Meters": 0.0254, "Feet": 0.0833333, "Kilometers": 0.0000254, "Miles": 0.0000157828, "Yards": 0.0277778, "Centimeters": 2.54, "Millimeters": 25.4, "Nautical Miles": 0.0000137149},
        "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Miles": 0.621371, "Inches": 39370.1, "Yards": 1093.61, "Centimeters": 100000, "Millimeters": 1000000, "Nautical Miles": 0.539957},
        "Yards": {"Meters": 0.9144, "Feet": 3, "Miles": 0.000568182, "Inches": 36, "Kilometers": 0.0009144, "Centimeters": 91.44, "Millimeters": 914.4, "Nautical Miles": 0.000493737},
        "Centimeters": {"Meters": 0.01, "Feet": 0.0328084, "Miles": 0.00000621371, "Inches": 0.393701, "Kilometers": 0.00001, "Yards": 0.0109361, "Millimeters": 10, "Nautical Miles": 0.00000539957},
        "Millimeters": {"Meters": 0.001, "Feet": 0.00328084, "Miles": 0.000000621371, "Inches": 0.0393701, "Kilometers": 0.000001, "Yards": 0.00109361, "Centimeters": 0.1, "Nautical Miles": 0.000000539957},
        "Nautical Miles": {"Meters": 1852, "Feet": 6076.12, "Miles": 1.15078, "Inches": 72913.4, "Kilometers": 1.852, "Yards": 2025.37, "Centimeters": 185200, "Millimeters": 1852000}
    },
    "mass": {
        "Kilograms": {"Pounds": 2.20462, "Ounces": 35.274, "Grams": 1000, "Tons": 0.001, "Milligrams": 1000000, "Stones": 0.157473},
        "Pounds": {"Kilograms": 0.453592, "Ounces": 16, "Grams": 453.592, "Tons": 0.000453592, "Milligrams": 453592, "Stones": 0.0714286},
        "Ounces": {"Kilograms": 0.0283495, "Pounds": 0.0625, "Grams": 28.3495, "Tons": 0.0000283495, "Milligrams": 28349.5, "Stones": 0.00446429},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274, "Tons": 0.000001, "Milligrams": 1000, "Stones": 0.000157473},
        "Tons": {"Kilograms": 1000, "Pounds": 2204.62, "Ounces": 35274, "Grams": 1000000, "Milligrams": 1000000000, "Stones": 157.473},
        "Milligrams": {"Kilograms": 0.000001, "Pounds": 0.00000220462, "Ounces": 0.000035274, "Grams": 0.001, "Tons": 0.000000001, "Stones": 0.000000157473},
        "Stones": {"Kilograms": 6.35029, "Pounds": 14, "Ounces": 224, "Grams": 6350.29, "Tons": 0.00635029, "Milligrams": 6350290}
    },
    "volume": {
        "Liters": {"Gallons": 0.264172, "Milliliters": 1000, "Cubic Meters": 0.001, "Cubic Feet": 0.0353147, "Cups": 4.22675, "Pints": 2.11338, "Quarts": 1.05669, "Fluid Ounces": 33.814},
        "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Cubic Meters": 0.00378541, "Cubic Feet": 0.133681, "Cups": 16, "Pints": 8, "Quarts": 4, "Fluid Ounces": 128},
        "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Cubic Meters": 0.000001, "Cubic Feet": 0.0000353147, "Cups": 0.00422675, "Pints": 0.00211338, "Quarts": 0.00105669, "Fluid Ounces": 0.033814},
        "Cups": {"Liters": 0.236588, "Gallons": 0.0625, "Milliliters": 236.588, "Pints": 0.5, "Quarts": 0.25, "Fluid Ounces": 8},
        "Pints": {"Liters": 0.473176, "Gallons": 0.125, "Milliliters": 473.176, "Cups": 2, "Quarts": 0.5, "Fluid Ounces": 16},
        "Quarts": {"Liters": 0.946353, "Gallons": 0.25, "Milliliters": 946.353, "Cups": 4, "Pints": 2, "Fluid Ounces": 32},
        "Fluid Ounces": {"Liters": 0.0295735, "Gallons": 0.0078125, "Milliliters": 29.5735, "Cups": 0.125, "Pints": 0.0625, "Quarts": 0.03125}
    },
    "time": {
        "Seconds": {"Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Weeks": 1/604800, "Months":3.80517e-7, "Years":3.17098e-8},
        "Minutes": {"Seconds": 60, "Hours": 1/60, "Days": 1/1440, "Weeks": 1/10080, "Months":2.2831e-5, "Years":1.90259e-6},
        "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 1/24, "Weeks": 1/168, "Months":0.00136986, "Years":0.000114155},
        "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24, "Weeks": 1/7, "Months":0.0328767, "Years":0.00273973},
        "Weeks": {"Seconds": 604800, "Minutes": 10080, "Hours": 168, "Days": 7, "Months":0.230137, "Years":0.0191781},
        "Months": {"Seconds": 2628000, "Minutes": 43800, "Hours": 730.001, "Days": 30.4167, "Years": 0.0833334},
        "Years": {"Seconds": 31540000, "Minutes": 525600, "Hours":8760, "Days": 365.25, "Months":12}
    },
    "temperature": {
            "Celsius": {"Fahrenheit": lambda c: c * 9/5 + 32, "Kelvin": lambda c: c + 273.15},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
    },

    "speed": {
        "Meters per Second": {"Kilometers per Hour": 3.6, "Miles per Hour": 2.23694, "Knots": 1.94384, "Feet per Second": 3.28084},
        "Kilometers per Hour": {"Meters per Second": 0.277778, "Miles per Hour": 0.621371, "Knots": 0.539957, "Feet per Second": 0.911344},
        "Miles per Hour": {"Meters per Second": 0.44704, "Kilometers per Hour": 1.60934, "Knots": 0.868976, "Feet per Second": 1.46667},
        "Knots": {"Meters per Second": 0.514444, "Kilometers per Hour": 1.852, "Miles per Hour": 1.15078, "Feet per Second": 1.68781}
    },

    "energy": {
        "Joules": {"Kilojoules": 0.001, "Calories": 0.239006, "Kilowatt-hours": 0.000000277778},
        "Kilojoules": {"Joules": 1000, "Calories": 239.006, "Kilowatt-hours": 0.000277778},
        "Calories": {"Joules": 4.184, "Kilojoules": 0.004184, "Kilowatt-hours": 0.00000116222},
        "Kilowatt-hours": {"Joules": 3600000, "Kilojoules": 3600, "Calories": 860421}
    },

    "pressure": {
        "Pascals": {"Atmospheres": 0.0000098692, "Bars": 0.00001},
        "Atmospheres": {"Pascals": 101325,"Bars": 1.01325},
        "Bars": {"Pascals": 100000, "Atmospheres": 0.986923},
    },

    "area": {
        "Square Meters": {"Square Kilometers": 0.000001, "Square Miles": 0.0000003861, "Square Feet": 10.7639, "Acres": 0.000247105, "Hectares": 0.0001},
        "Square Kilometers": {"Square Meters": 1000000, "Square Miles": 0.386102, "Square Feet": 10760000, "Acres": 247.105, "Hectares": 100},
        "Square Feet": {"Square Meters": 0.092903, "Square Kilometers": 0.000000092903, "Square Miles": 0.00000003587, "Acres": 0.000022957, "Hectares": 0.0000092903},
        "Square Miles": {"Square Meters": 2590000, "Square Kilometers": 2.58999, "Square Feet": 27880000, "Acres": 640, "Hectares": 258.999},
        "Acres": {"Square Meters": 4046.86, "Square Kilometers": 0.00404686, "Square Miles": 0.0015625, "Square Feet": 43560, "Hectares": 0.404686},
        "Hectares": {"Square Meters": 10000, "Square Kilometers": 0.01, "Square Miles": 0.00386102, "Square Feet": 107639, "Acres": 2.47105}
    }


}

    if category == "temperature":
        # For temperature, call the lambda function
        result = conversion_factors[category][convertFrom][convertTo]
    else:
        # For other categories, multiply by the conversion factor
        result = value * conversion_factors[category][convertFrom][convertTo]

    decimalPoints = 4
    result_rounded = round_to_significant_figures(result, decimalPoints)
    resultText = str(result_rounded) + unit_symbol_options[category][convertTo]
    print(resultText)
    resultLabel.configure(text=resultText, fg_color="gray20", corner_radius=10)  # Update the resultLabel with background color and rounded corners

root = customtkinter.CTk()
root.geometry("700x570")

# Create a frame to hold all the widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

frame.grid_rowconfigure(4, weight=1)  # Add a new row for the resultLabel

# Add the "Unit Converter" label at the top
label = customtkinter.CTkLabel(master=frame, text="Unit Converter", font=("Roboto", 42))
label.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

# Add radio buttons on the left third of the screen
radio_frame = customtkinter.CTkFrame(master=frame)
radio_frame.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

radio_var = customtkinter.StringVar(value="distance")
radio_var.trace("w", update_unit_menus)  # Call `update_unit_menus` when the radio button changes

distance_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Distance",font=("Calibri", 20), variable=radio_var, value="distance")
distance_radio.pack(pady=10, padx=10, anchor="w")

mass_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Mass",font=("Calibri", 20), variable=radio_var, value="mass")
mass_radio.pack(pady=10, padx=10, anchor="w")

volume_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Volume",font=("Calibri", 20), variable=radio_var, value="volume")
volume_radio.pack(pady=10, padx=10, anchor="w")

temperature_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Temperature",font=("Calibri", 20), variable=radio_var, value="temperature")
temperature_radio.pack(pady=10, padx=10, anchor="w")

time_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Time",font=("Calibri", 20), variable=radio_var, value="time")
time_radio.pack(pady=10, padx=10, anchor="w")

speed_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Speed",font=("Calibri", 20), variable=radio_var, value="speed")
speed_radio.pack(pady=10, padx=10, anchor="w")

energy_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Energy",font=("Calibri", 20), variable=radio_var, value="energy")
energy_radio.pack(pady=10, padx=10, anchor="w")

pressure_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Pressure",font=("Calibri", 20), variable=radio_var, value="pressure")
pressure_radio.pack(pady=10, padx=10, anchor="w")

area_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Area",font=("Calibri", 20), variable=radio_var, value="area")
area_radio.pack(pady=10, padx=10, anchor="w")

# Add the value entry box and option menus on the right two-thirds of the screen
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Value 1")
entry1.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

unit_menu1 = customtkinter.CTkOptionMenu(master=frame, values=unit_options["distance"])
unit_menu1.grid(row=1, column=2, pady=10, padx=10, sticky="ew")

convert_to_label = customtkinter.CTkLabel(master=frame, text="Convert to:")
convert_to_label.grid(row=2, column=1, pady=10, padx=10, sticky="e")

unit_menu2 = customtkinter.CTkOptionMenu(master=frame, values=unit_options["distance"])
unit_menu2.grid(row=2, column=2, pady=10, padx=10, sticky="ew")

# Add the convert button at the bottom
convert_button = customtkinter.CTkButton(master=frame, text="Convert", command=convert)
convert_button.grid(row=3, column=1, columnspan=2, pady=2, padx=10, sticky="ew")

resultLabel = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 24), fg_color="gray20", corner_radius=7)
resultLabel.grid(row=4, column=1, columnspan=2, pady=2, padx=10, sticky="ew")

# Configure the grid to expand properly
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)
frame.grid_columnconfigure(2, weight=2)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)

# Initialize the unit menus with the default category (distance)
update_unit_menus()

root.mainloop()