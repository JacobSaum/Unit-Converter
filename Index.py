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
convert_button = customtkinter.CTkButton(master=frame, text="Convert")
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

root.mainloop()