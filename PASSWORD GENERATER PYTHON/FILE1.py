import tkinter as tk
from tkinter import messagebox
import random
import string
import SUB_SEQUENCER

def GENERATOR_WINDOW():
    def generate_password():
        password_length = length_scale.get()
        
        character_sets = []
        if uppercase_var.get():
            character_sets.append(string.ascii_uppercase)
        if lowercase_var.get():
            character_sets.append(string.ascii_lowercase)
        if numbers_var.get():
            character_sets.append(string.digits)
        if special_var.get():
            character_sets.append(string.punctuation)

        if not character_sets:
            messagebox.showerror("Error", "Please select at least one character set.")
            return

        all_characters = ''.join(character_sets)
        if password_length > len(all_characters):
            messagebox.showerror("Error", "Password length exceeds the total available characters.")
            return

        generated_password = ''.join(random.choice(all_characters) for _ in range(password_length))
        password_var.set(generated_password)

        analyze_strength()

    def analyze_strength():
        password = password_var.get()
        password_length = len(password)

        # Check for uppercase characters
        if any(c.isupper() for c in password):
            uppercase_suggestion_var.set("")
        else:
            uppercase_suggestion_var.set("Add some Uppercase characters to your Password")

        # Check for lowercase characters
        if any(c.islower() for c in password):
            lowercase_suggestion_var.set("")
        else:
            lowercase_suggestion_var.set("Add some Lowercase characters to your Password")

        # Check for numbers
        if any(c.isdigit() for c in password):
            numbers_suggestion_var.set("")
        else:
            numbers_suggestion_var.set("Add some Numbers to your Password")

        # Check for special characters
        if any(c in string.punctuation for c in password):
            special_suggestion_var.set("")
        else:
            special_suggestion_var.set("Add some Special characters to your Password")

        if password_length <= 4:
            strength_var.set("Weak")
            for i in range(4):
                strength_canvas.itemconfig(rectangles[i], fill="red", outline="black")
            length_suggestion_var.set("Increase the length of the password")
        elif password_length <= 8:
            strength_var.set("Moderate")
            for i in range(2):
                strength_canvas.itemconfig(rectangles[i], fill="yellow", outline="black")
            for i in range(2, 4):
                strength_canvas.itemconfig(rectangles[i], fill="white", outline="black")
            length_suggestion_var.set("Increase the length of the password")
        elif password_length <= 20:
            strength_var.set("Strong")
            for i in range(3):
                strength_canvas.itemconfig(rectangles[i], fill="light green", outline="black")
            strength_canvas.itemconfig(rectangles[3], fill="white", outline="black")
            length_suggestion_var.set("")
        else:
            strength_var.set("Very Strong")
            for i in range(4):
                strength_canvas.itemconfig(rectangles[i], fill="light blue", outline="black")
            length_suggestion_var.set("")

        if (
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password) and
            strength_var.get() in ["Strong", "Very Strong"]
        ):
            general_suggestion_var.set("No Suggestion! Your password is Good to Go!")
        else:
            general_suggestion_var.set("")

        #Checking for certain Specific phrases
        truth_value,substring2suggest=SUB_SEQUENCER.Subsequence_checker(password)
        if truth_value:
            suggestion_line="You could remove "+ substring2suggest +" from your password."
            specialcase_suggestion_var.set(suggestion_line)


        strength_label_var.set(strength_var.get().upper())

    # GUI setup
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("900x600")

    # Password Length Scale
    length_label = tk.Label(root, text="Password Length:")
    length_label.pack(pady=5)
    length_scale = tk.Scale(root, from_=4, to=32, orient=tk.HORIZONTAL)
    length_scale.pack(pady=5)

    # Character Set Checkboxes
    uppercase_var = tk.BooleanVar()
    lowercase_var = tk.BooleanVar()
    numbers_var = tk.BooleanVar()
    special_var = tk.BooleanVar()

    uppercase_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
    lowercase_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
    numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
    special_checkbox = tk.Checkbutton(root, text="Special Characters", variable=special_var)

    uppercase_checkbox.pack(anchor="center")
    lowercase_checkbox.pack(anchor="center")
    numbers_checkbox.pack(anchor="center")
    special_checkbox.pack(anchor="center")

    # Generate Password Button
    generate_button = tk.Button(root, text="Generate Password", command=generate_password)
    generate_button.pack(pady=10)

    # Display Generated Password
    password_var = tk.StringVar()
    generated_password_label = tk.Label(root, text="Generated Password:")
    generated_password_label.pack(pady=5)
    password_entry = tk.Entry(root, textvariable=password_var, state="readonly")
    password_entry.pack(pady=10)

    # Password Strength
    strength_var = tk.StringVar()
    strength_label = tk.Label(root, text="Password Strength:")
    strength_label.pack(pady=5)

    # Label to display strength_var
    strength_label_var = tk.StringVar()
    strength_display_label = tk.Label(root, textvariable=strength_label_var)
    strength_display_label.pack(pady=5)

    # Canvas for Strength Indicator
    strength_canvas = tk.Canvas(root, width=500, height=40)
    strength_canvas.pack()

    # Create sub-rectangles with equal length and spacing
    rectangles = [
        strength_canvas.create_rectangle(0, 0, 100, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(120, 0, 220, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(240, 0, 340, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(360, 0, 460, 40, fill="white", outline="black")
    ]
 
    # Label for Suggestions
    suggestions_label = tk.Label(root, text="SUGGESTIONS : ")
    suggestions_label.pack()

    # Suggestions
    general_suggestion_var = tk.StringVar()
    general_suggestion_label = tk.Label(root, textvariable=general_suggestion_var, fg="green")
    general_suggestion_label.pack()

    # Uppercase suggestion
    uppercase_suggestion_var = tk.StringVar()
    uppercase_suggestion_label = tk.Label(root, textvariable=uppercase_suggestion_var, fg="red")
    uppercase_suggestion_label.pack()

    # Lowercase suggestion
    lowercase_suggestion_var = tk.StringVar()
    lowercase_suggestion_label = tk.Label(root, textvariable=lowercase_suggestion_var, fg="red")
    lowercase_suggestion_label.pack()

    # Numbers suggestion
    numbers_suggestion_var = tk.StringVar()
    numbers_suggestion_label = tk.Label(root, textvariable=numbers_suggestion_var, fg="red")
    numbers_suggestion_label.pack()

    # Special Characters suggestion
    special_suggestion_var = tk.StringVar()
    special_suggestion_label = tk.Label(root, textvariable=special_suggestion_var, fg="red")
    special_suggestion_label.pack()

    # Length suggestion
    length_suggestion_var = tk.StringVar()
    length_suggestion_label = tk.Label(root, textvariable=length_suggestion_var, fg="red")
    length_suggestion_label.pack()

    # Special case suggestion
    specialcase_suggestion_var = tk.StringVar()
    specialcase_suggestion_var_label = tk.Label(root, textvariable=length_suggestion_var, fg="red")
    specialcase_suggestion_var_label.pack()


    # Run the GUI
    root.mainloop()

# Call the function to run the GUI
#GENERATOR_WINDOW()
