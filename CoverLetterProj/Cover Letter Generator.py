import tkinter as tk
import re
import pyperclip


def get_template():
    template = input_box.get("1.0", "end-1c")
    print("Place a template with fillable fields contained in [brackets]:", template)

    bracketed_areas = re.findall(r'\[(.*?)\]', template)
    
    variable_data = {}
    data_input_window = tk.Toplevel(root)
    data_input_window.title("Fillable Fields")
    data_input_window.geometry("400x400")

    for variable_name in bracketed_areas:
        if variable_name not in variable_data:
            label = tk.Label(data_input_window, text=f"Enter value for '{variable_name}':")
            label.pack()
        
            entry = tk.Entry(data_input_window)
            entry.pack()
        
            # Store the Entry widget in the dictionary using the variable name as the key
            variable_data[variable_name] = entry
    
    def submit_input():
        for variable_name, entry_widget in variable_data.items():
            user_input = entry_widget.get()
            variable_data[variable_name] = user_input
        
         # Replace bracketed areas in the input text with user inputs
        filled_text = template
        for variable_name, user_input in variable_data.items():
            filled_text = filled_text.replace(f"[{variable_name}]", user_input)
        
        # Create a new window to display the filled text
        display_window = tk.Toplevel(root)
        display_window.title("Filled Text")
        # display_window.geometry("600x300")
        
        text_widget = tk.Text(display_window, width=100, height=50)
        text_widget.pack()
        
        # Insert the filled text into the Text widget
        text_widget.insert("1.0", filled_text)

        button_frame = tk.Frame(display_window)
        button_frame.pack(side=tk.BOTTOM)

        copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=lambda: copy_to_clipboard(filled_text))
        copy_button.pack(side=tk.LEFT)
        close_button = tk.Button(button_frame, text="Close Filled-out Letter", command=display_window.destroy)
        close_button.pack(side=tk.RIGHT)
    
    submit_button = tk.Button(data_input_window, text="Submit", command=submit_input)
    submit_button.pack()

def copy_to_clipboard(text):
    pyperclip.copy(text)
root = tk.Tk()
root.title("Import Letter")

label = tk.Label(root,text="Cover letter:")
label.pack()

input_box = tk.Text(root, width=100, height=50)
input_box.pack()

submit_button = tk.Button(root, text="Submit", command=get_template)
submit_button.pack()

root.mainloop()