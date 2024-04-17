import tkinter as tk
from tkinter import scrolledtext, Label, font as tkfont
import re

def process_input(input_string):
    # Normalize and extract airport codes
    input_string = re.sub(r'[^A-Z]+', ',', input_string.upper())
    return list(filter(None, input_string.split(',')))

def update_counts():
    # Update count for set A
    count_a = len(process_input(text_area_a.get("1.0", tk.END)))
    count_label_a.config(text=f"Total Codes: {count_a}")
    
    # Update count for set B
    count_b = len(process_input(text_area_b.get("1.0", tk.END)))
    count_label_b.config(text=f"Total Codes: {count_b}")

    # Update count for results
    result_codes = results_area.get("1.0", tk.END).strip().split(',')
    count_label_results.config(text=f"Total Codes: {len(result_codes) if result_codes[0] != '' else 0}")

def calculate_difference():
    set_a = process_input(text_area_a.get("1.0", tk.END))
    set_b = process_input(text_area_b.get("1.0", tk.END))
    difference = sorted(list(set(set_a) - set(set_b)))
    result = ','.join(difference)
    results_area.config(state=tk.NORMAL)  # Enable text area to modify
    results_area.delete("1.0", tk.END)  # Clear existing content
    results_area.insert("1.0", result)  # Insert new result
    results_area.config(state=tk.DISABLED)  # Disable editing
    update_counts()  # Update counts after calculation

# Create the main window
root = tk.Tk()
root.title("Airport Code Difference Calculator")
root.geometry("600x800")  # Set the size of the window

# Define smaller font for count labels and italic font for quote
small_font = tkfont.Font(size=8)
button_font = tkfont.nametofont("TkDefaultFont")  # Get the default font used in buttons
italic_font = tkfont.Font(family=button_font.actual("family"), size=button_font.actual("size"), slant="italic")

# Frame for set A
frame_a = tk.Frame(root)
frame_a.pack(padx=10, pady=10, fill='x')
label_a = tk.Label(frame_a, text="Enter Airline Zones in Bunker Database:")
label_a.pack()
text_area_a = scrolledtext.ScrolledText(frame_a, wrap=tk.WORD, width=60, height=10)
text_area_a.pack(fill='x')
count_label_a = Label(frame_a, text="Total Codes: 0", font=small_font)
count_label_a.pack()

# Frame for set B
frame_b = tk.Frame(root)
frame_b.pack(padx=10, pady=10, fill='x')
label_b = tk.Label(frame_b, text="Enter Airport Codes in the Rate Sheet:")
label_b.pack()
text_area_b = scrolledtext.ScrolledText(frame_b, wrap=tk.WORD, width=60, height=10)
text_area_b.pack(fill='x')
count_label_b = Label(frame_b, text="Total Codes: 0", font=small_font)
count_label_b.pack()

# Frame for results
frame_results = tk.Frame(root)
frame_results.pack(padx=10, pady=10, fill='x')
label_results = tk.Label(frame_results, text="Difference Results:")
label_results.pack()
results_area = scrolledtext.ScrolledText(frame_results, wrap=tk.WORD, width=60, height=5)
results_area.pack(fill='x')
results_area.config(state=tk.DISABLED)  # Disable editing of results area
count_label_results = Label(frame_results, text="Total Codes: 0", font=small_font)
count_label_results.pack()

# Button to trigger the difference calculation
calculate_button = tk.Button(root, text="Calculate Difference", command=calculate_difference)
calculate_button.pack(pady=10)

# Custom quote at the bottom right
quote_label = tk.Label(root, text="Made by Gaj", font=italic_font)
quote_label.pack(side='right', padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
