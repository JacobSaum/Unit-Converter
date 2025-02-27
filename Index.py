import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Define unit options for each category
unit_options = {
    "distance": ["Meters", "Feet", "Inches", "Kilometers", "Miles"],
    "weight": ["Kilograms", "Pounds", "Ounces", "Grams", "Tons"],
    "volume": ["Liters", "Gallons", "Milliliters", "Cubic Meters", "Cubic Feet"]
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


def convert():
    convertFrom = unit_menu1.get()
    convertTo = unit_menu2.get()
    val = entry1.get()
    if val.isnumeric():
        value = float(val)

        if convertFrom == convertTo:
            print("Error: Unit must be different!")
        else:
            convertLength(convertFrom, convertTo, value)

    else:
        print("Error: A number must be entered!")
     

def convertLength(convertFrom, convertTo, value):
    category = radio_var.get()
    conversion_factors = {
    "distance": {
        "Meters": {"Feet": 3.28084, "Miles": 0.000621371, "Inches": 39.3701, "Kilometers": 0.001},
        "Feet": {"Meters": 0.3048, "Miles": 0.000189394, "Inches": 12, "Kilometers": 0.0003048},
        "Miles": {"Meters": 1609.34, "Feet": 5280, "Inches": 63360, "Kilometers": 1.60934},
        "Inches": {"Meters": 0.0254, "Feet": 0.0833333, "Kilometers": 0.0000254, "Miles": 0.0000157828},
        "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Miles": 0.621371, "Inches": 39370.1}
    },
    "weight": {
        "Kilograms": {"Pounds": 2.20462, "Ounces": 35.274, "Grams": 1000, "Tons": 0.001},
        "Pounds": {"Kilograms": 0.453592, "Ounces": 16, "Grams": 453.592, "Tons": 0.000453592},
        "Ounces": {"Kilograms": 0.0283495, "Pounds": 0.0625, "Grams": 28.3495, "Tons": 0.0000283495},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274, "Tons": 0.000001},
        "Tons": {"Kilograms": 1000, "Pounds": 2204.62, "Ounces": 35274, "Grams": 1000000}
    },
    "volume": {
        "Liters": {"Gallons": 0.264172, "Milliliters": 1000, "Cubic Meters": 0.001, "Cubic Feet": 0.0353147},
        "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Cubic Meters": 0.00378541, "Cubic Feet": 0.133681},
        "Milliliters": {"Liters": 0.001, "Gallons": 0.000264172, "Cubic Meters": 0.000001, "Cubic Feet": 0.0000353147},
        "Cubic Meters": {"Liters": 1000, "Gallons": 264.172, "Milliliters": 1000000, "Cubic Feet": 35.3147},
        "Cubic Feet": {"Liters": 28.3168, "Gallons": 7.48052, "Milliliters": 28316.8, "Cubic Meters": 0.0283168}
    }
}
    print(value * conversion_factors[category][convertFrom][convertTo])
    #return value * conversion_factors[category][convertFrom][convertTo]


root = customtkinter.CTk()
root.geometry("600x400")

# Create a frame to hold all the widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add the "Unit Converter" label at the top
label = customtkinter.CTkLabel(master=frame, text="Unit Converter", font=("Roboto", 42))
label.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

# Add radio buttons on the left third of the screen
radio_frame = customtkinter.CTkFrame(master=frame)
radio_frame.grid(row=1, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")

radio_var = customtkinter.StringVar(value="distance")
radio_var.trace("w", update_unit_menus)  # Call `update_unit_menus` when the radio button changes

distance_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Distance", variable=radio_var, value="distance")
distance_radio.pack(pady=10, padx=10, anchor="w")

weight_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Weight", variable=radio_var, value="weight")
weight_radio.pack(pady=10, padx=10, anchor="w")

volume_radio = customtkinter.CTkRadioButton(master=radio_frame, text="Volume", variable=radio_var, value="volume")
volume_radio.pack(pady=10, padx=10, anchor="w")

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
convert_button.grid(row=3, column=1, columnspan=2, pady=20, padx=10, sticky="ew")

# Configure the grid to expand properly
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)
frame.grid_columnconfigure(2, weight=2)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)

# Initialize the unit menus with the default category (distance)
update_unit_menus()

#if radio_var.get() == "Length" and convert_button.
    #convertLength()

root.mainloop()