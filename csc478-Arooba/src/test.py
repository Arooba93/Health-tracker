import tkinter as tk

class CalorieCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Calculator")

        # Dictionary to store daily calorie entries
        self.daily_calories = {}

        # Create labels and entry widgets for each meal
        self.breakfast_label = tk.Label(root, text="Breakfast Calories:")
        self.breakfast_label.pack()
        self.breakfast_entry = tk.Entry(root)
        self.breakfast_entry.pack()

        self.lunch_label = tk.Label(root, text="Lunch Calories:")
        self.lunch_label.pack()
        self.lunch_entry = tk.Entry(root)
        self.lunch_entry.pack()

        self.snack_label = tk.Label(root, text="Snack Calories:")
        self.snack_label.pack()
        self.snack_entry = tk.Entry(root)
        self.snack_entry.pack()

        self.dinner_label = tk.Label(root, text="Dinner Calories:")
        self.dinner_label.pack()
        self.dinner_entry = tk.Entry(root)
        self.dinner_entry.pack()

        self.additional_label = tk.Label(root, text="Additional Calories:")
        self.additional_label.pack()
        self.additional_entry = tk.Entry(root)
        self.additional_entry.pack()

        # Create a label and entry field for the date
        self.date_label = tk.Label(root, text="Date (e.g., YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        # Create a button to calculate and update total calories
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_total_calories)
        self.calculate_button.pack()

        # Create a label to display the total calories for the day
        self.total_calories_label = tk.Label(root, text="Total Calories: 0 kcal")
        self.total_calories_label.pack()

        # Create a Listbox to display the total calories for each day
        self.calories_listbox = tk.Listbox(root)
        self.calories_listbox.pack()

    def calculate_total_calories(self):
        # Get calorie inputs for each meal
        breakfast_calories = int(self.breakfast_entry.get())
        lunch_calories = int(self.lunch_entry.get())
        snack_calories = int(self.snack_entry.get())
        dinner_calories = int(self.dinner_entry.get())
        additional_calories = int(self.additional_entry.get())

        # Calculate total calories for the day
        total_calories = breakfast_calories + lunch_calories + snack_calories + dinner_calories + additional_calories

        # Get the selected date
        selected_date = self.date_entry.get()

        # Update the total calories label
        self.total_calories_label.config(text=f"Total Calories for {selected_date}: {total_calories} kcal")

        # Store the daily calorie entry in the dictionary
        self.daily_calories[selected_date] = f"{selected_date}: {total_calories} kcal"

        # Update the Listbox with all daily entries
        self.calories_listbox.delete(0, tk.END)
        for entry in self.daily_calories.values():
            self.calories_listbox.insert(tk.END, entry)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = CalorieCalculatorApp(root)
    root.mainloop()
