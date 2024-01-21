import tkinter as tk
import tkinter.font as font
import FILE1
import FILE2

def generate():
    root.destroy()
    FILE1.GENERATOR_WINDOW()
def analyze():
    root.destroy()
    FILE2.ANALYZER_WINDOW()

# GUI setup
root = tk.Tk()
root.title("PASSWORD")
root.geometry("500x300")  # Set the window size

# Button Font
buttonFont = font.Font(size=16 , weight='bold')

# Generate Button
generate_button = tk.Button(root , text="GENERATE" , activebackground='#78d6ff' , bd=16 , font=buttonFont , command=generate , width=25, height=3)
generate_button.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="ANALYZE", activebackground='#78d6ff' , bd=16 , font=buttonFont , command=analyze, width=25, height=3)
analyze_button.pack(pady=10)

# Run the GUI
root.mainloop()
