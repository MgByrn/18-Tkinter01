###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

def submit_form():
    name = name_entry.get()
    address_line1 = address_line1_entry.get()
    address_line2 = address_line2_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_code_entry.get()
    phone_number = phone_number_entry.get()
    email = email_entry.get()
    print("Name:", name)
    print("Address Line 1:", address_line1)
    print("Address Line 2:", address_line2)
    print("City:", city)
    print("State:", state)
    print("Zip Code:", zip_code)
    print("Phone Number:", phone_number)
    print("Email Address:", email)

window = tk.Tk()
window.title("Form")

window.configure(bg="beige")
label_bg = "beige"
entry_bg = "white"

name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

address_line1_label = tk.Label(window, text="Address Line 1:")
address_line1_label.grid(row=1, column=0)
address_line1_entry = tk.Entry(window)
address_line1_entry.grid(row=1, column=1)

address_line2_label = tk.Label(window, text="Address Line 2:")
address_line2_label.grid(row=2, column=0)
address_line2_entry = tk.Entry(window)
address_line2_entry.grid(row=2, column=1)

city_label = tk.Label(window, text="City:")
city_label.grid(row=3, column=0)
city_entry = tk.Entry(window)
city_entry.grid(row=3, column=1)

state_label = tk.Label(window, text="State:")
state_label.grid(row=4, column=0)
state_entry = tk.Entry(window)
state_entry.grid(row=4, column=1)

zip_code_label = tk.Label(window, text="Zip Code:")
zip_code_label.grid(row=5, column=0)
zip_code_entry = tk.Entry(window)
zip_code_entry.grid(row=5, column=1)

phone_number_label = tk.Label(window, text="Phone Number:")
phone_number_label.grid(row=6, column=0)
phone_number_entry = tk.Entry(window)
phone_number_entry.grid(row=6, column=1)

email_label = tk.Label(window, text="Email Address:")
email_label.grid(row=7, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=7, column=1)

submit_button = tk.Button(window, text="Submit", command=submit_form, bg="beige", fg="black")
submit_button.grid(row=8, column=0, columnspan=2)

window.mainloop()
