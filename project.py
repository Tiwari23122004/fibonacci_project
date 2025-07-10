
import tkinter as tk

def calculate_fibonacci():
    try:
        num = int(entry.get())
        if num < 0:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Please enter a positive integer")
            return
        elif num == 0:
            fib_series = [0]
        elif num == 1:
            fib_series = [0, 1]
        else:
            fib_series = [0, 1]
            for i in range(2, num + 1):
                fib_series.append(fib_series[i - 1] + fib_series[i - 2])

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Fibonacci Series:\n" + ", ".join(map(str, fib_series)))
    except ValueError:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Invalid input. Please enter a number")

# Create main window
root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("500x400")

# Entry Label
tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)

# Input Field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

# Button
calculate_button = tk.Button(root, text="Generate", font=("Arial", 12), command=calculate_fibonacci)
calculate_button.pack(pady=10)

# Scrollable Text Output
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(frame, height=10, wrap=tk.WORD, font=("Arial", 11), yscrollcommand=scrollbar.set)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=output_text.yview)

# Start GUI
root.mainloop()
