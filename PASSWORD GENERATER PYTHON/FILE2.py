import tkinter as tk
from tkinter import messagebox
import SUB_SEQUENCER

def ANALYZER_WINDOW():
    def analyze_strength():
        password = password_var.get()
        password_length = len(password)

        suggestions = []

        # Check if the password contains upper case characters
        if not any(char.isupper() for char in password):
            suggestions.append("Add some upper case characters to your password.")

        # Check if the password contains lower case characters
        if not any(char.islower() for char in password):
            suggestions.append("Add some lower case characters to your password.")

        # Check if the password contains numbers
        if not any(char.isdigit() for char in password):
            suggestions.append("Add some numbers to your password.")

        # Check if the password contains special characters
        special_characters = set("!@#$%^&*()_-+=<>?/,.|~")
        if not any(char in special_characters for char in password):
            suggestions.append("Add some special characters to your password.")

        # Determine password strength based on length
        if password_length <= 4:
            strength = "Weak"
            suggestions.append("Increase the length of the password.")
            for i in range(4):
                strength_canvas.itemconfig(rectangles[i], fill="red")
        elif password_length <= 8:
            strength = "Moderate"
            suggestions.append("Increase the length of the password.")
            for i in range(2):
                strength_canvas.itemconfig(rectangles[i], fill="yellow")
            for i in range(2, 4):
                strength_canvas.itemconfig(rectangles[i], fill="white")
        elif password_length <= 20:
            strength = "Strong"
            for i in range(3):
                strength_canvas.itemconfig(rectangles[i], fill="light green")
            strength_canvas.itemconfig(rectangles[3], fill="white")
        else:
            strength = "Very Strong"
            for i in range(4):
                strength_canvas.itemconfig(rectangles[i], fill="light blue")

        strength_var.set(f"Password Strength: {strength}")
        strength_label_var.set(strength.upper())

        truth_value,substring2suggest=SUB_SEQUENCER.Subsequence_checker(password)

        if truth_value:
            suggestion_line="Kindly, Do not use "+ "\"" + substring2suggest + "\"" +  " in your password."
            suggestions.append(str(suggestion_line))

        # Display suggestions
        if strength in ("Strong", "Very Strong") and all((
                any(char.isupper() for char in password),
                any(char.islower() for char in password),
                any(char.isdigit() for char in password),
                any(char in special_characters for char in password))):
            suggestions_label_var.set("No Suggestion! Your password is Good to Go!")
        else:
            suggestions_label_var.set("SUGGESTIONS:\n" + "\n".join(suggestions))

    # GUI setup
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("600x400")

    # Password Entry
    password_var = tk.StringVar()
    password_label = tk.Label(root, text="Enter Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, textvariable=password_var)
    password_entry.pack(pady=5)

    # Check Strength Button
    check_button = tk.Button(root, text="Check Strength", command=analyze_strength)
    check_button.pack(pady=10)

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
        strength_canvas.create_rectangle(0, 0, 120, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(130, 0, 250, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(260, 0, 380, 40, fill="white", outline="black"),
        strength_canvas.create_rectangle(390, 0, 500, 40, fill="white", outline="black")
    ]

    # Label to display suggestions
    suggestions_label_var = tk.StringVar()
    suggestions_label = tk.Label(root, textvariable=suggestions_label_var, wraplength=500, justify="left")
    suggestions_label.pack(pady=5)

    # Run the GUI
    root.mainloop()

# Call the function to display the window
#ANALYZER_WINDOW()
