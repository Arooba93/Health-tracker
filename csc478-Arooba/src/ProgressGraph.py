import tkinter as tk
from tkinter import ttk
from db_agent import DbAgent
from person import Person
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Sample data , would have to replace this with our data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
weights_lbs = [154, 156, 155, 153, 152, 151, 152, 153, 154, 156, 158, 159]

def update_graph():
    # Generate random data for demonstration purposes
    weights_lbs = [random.randint(140, 170) for _ in months]
    update_progress_graph(weights_lbs)

def update_progress_graph(weights_lbs):
    # Clear the existing graph
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a new figure
    fig = Figure(figsize=(6, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(months, weights_lbs, marker='o', linestyle='-')
    plot.set_title("Weight Progress Over Months")
    plot.set_xlabel("Month")
    plot.set_ylabel("Weight (lbs)")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    canvas.draw()

root = tk.Tk()
root.title("Weight Progress Graph (lbs)")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

update_progress_graph(weights_lbs)

update_button = ttk.Button(root, text="Update Graph", command=update_graph)
update_button.pack(pady=10)

#root.mainloop()

