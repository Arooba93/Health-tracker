import tkinter as tk
from tkinter import ttk
from db_agent import DbAgent
from person import Person



class Gui:
    def __init__(self, _root: tk.Tk, _person: Person, _db_agent: DbAgent):
        self.root = _root
        self.notebook = ttk.Notebook(self.root)
        self.person = _person
        self.person.calculate_bmi()
        self.person.calculate_bmr()
        self.db_agent = _db_agent
        self.frames = {}
        self.labels = {}
        self.Combobox= {}
        self.Button = {}
        self.Entry= {}
        self.txt_vars = {}
        self.create_widgets()


    def create_widgets(self):
        self.txt_vars["name"] = tk.StringVar(self.root, value=self.person.get_name())
        self.txt_vars["age"] = tk.StringVar(self.root, value=f"{self.person.get_age()}")
        self.txt_vars["gender"] = tk.StringVar(self.root, value=self.person.get_gender())
        self.txt_vars["height"] = tk.StringVar(self.root, value=f"{self.person.get_height()//12}' {self.person.get_height()%12}\"")
        self.txt_vars["bmi"] = tk.StringVar(self.root, value=f"{self.person.get_bmi():.1f}")
        self.txt_vars["bmr"] = tk.StringVar(self.root, value=f"{self.person.get_bmr():.1f}")

        self.root.title("Fitness Health Calculator")

        self.notebook.pack(fill="both", expand=True)
        
        # Create the info (Information) frame
        self.frames["info"] = ttk.Frame(self.notebook)
        self.notebook.add(self.frames["info"], text="Information")

        max_width = len("Biological Gender: ")

        self.labels["name"] = ttk.Label(self.frames["info"], text="Name: ", anchor="w", width=max_width)
        self.labels["name"].grid(row=0, column=0, pady=5)
        self.labels["name_var"] = ttk.Label(self.frames["info"], textvariable=self.txt_vars["name"], anchor="w", width=max_width)
        self.labels["name_var"].grid(row=0, column=1, pady=5)

        self.labels["gender"] = ttk.Label(self.frames["info"], text="Biological Gender: ", anchor="w", width=max_width)
        self.labels["gender"].grid(row=1, column=0, pady=5)
        self.labels["gender_var"] = ttk.Label(self.frames["info"], textvariable=self.txt_vars["gender"], anchor="w", width=max_width)
        self.labels["gender_var"].grid(row=1, column=1, pady=5)

        self.labels["age"] = ttk.Label(self.frames["info"], text="Age: ", anchor="w", width=max_width)
        self.labels["age"].grid(row=2, column=0, pady=5)
        self.labels["age_var"] = ttk.Label(self.frames["info"], textvariable=self.txt_vars["age"], anchor="w", width=max_width)
        self.labels["age_var"].grid(row=2, column=1, pady=5)

        self.labels["height"] = ttk.Label(self.frames["info"], text="Height: ", anchor="w", width=max_width)
        self.labels["height"].grid(row=3, column=0, pady=5)
        self.labels["height_var"] = ttk.Label(self.frames["info"], textvariable=self.txt_vars["height"], anchor="w", width=max_width)
        self.labels["height_var"].grid(row=3, column=1, pady=5)

        # Create the stats (Statistics) frame
        self.frames["stats"] = ttk.Frame(self.notebook)
        self.notebook.add(self.frames["stats"], text="Statistics")

        max_width = len("BMI: ")

        self.labels["bmi"] = ttk.Label(self.frames["stats"], text="BMI: ", anchor="w", width=max_width)
        self.labels["bmi"].grid(row=0, column=0, pady=5)
        self.labels["bmi_var"] = ttk.Label(self.frames["stats"], textvariable=self.txt_vars["bmi"], anchor="w", width=max_width)
        self.labels["bmi_var"].grid(row=0, column=1, pady=5)

        self.labels["bmr"] = ttk.Label(self.frames["stats"], text="BMR: ", anchor="w", width=max_width)
        self.labels["bmr"].grid(row=1, column=0, pady=5)
        self.labels["bmr_var"] = ttk.Label(self.frames["stats"], textvariable=self.txt_vars["bmr"], anchor="w", width=max_width)
        self.labels["bmr_var"].grid(row=1, column=1, pady=5)

        self.frames["setcal"] = ttk.Frame(self.notebook)
        self.notebook.add(self.frames["setcal"], text="Set Daily Calorie Intake")

        self.labels["gender_cal"] = ttk.Label(self.frames["setcal"], text="Gender:", anchor="w", width=max_width)
        self.labels["gender_cal"].grid(row=0, column=0, pady=5)
        self.Combobox["gender_var_cal"] = ttk.Combobox(self.frames["setcal"], values=["Male", "Female"])
        self.Combobox["gender_var_cal"].grid(row=0, column=1, pady=5)

        self.labels["age_cal"]= ttk.Label(self.frames["setcal"], text="Age:", anchor="w", width=max_width)
        self.labels["age_cal"].grid(row=1, column=0, pady=5)
        self.Entry["age_var_cal"] = ttk.Entry(self.frames["setcal"])
        self.Entry["age_var_cal"] .grid(row=1, column=1, pady=5)

        self.labels["weight_cal"]= ttk.Label(self.frames["setcal"], text="Weight (lbs):", anchor="w", width=max_width)
        self.labels["weight_cal"].grid(row=2, column=0, pady=5)
        self.Entry["weight_cal_var"] = ttk.Entry(self.frames["setcal"])
        self.Entry["weight_cal_var"].grid(row=2, column=1, pady=5)

        self.labels["feet_cal"]= ttk.Label(self.frames["setcal"], text="Height (feet):", anchor="w", width=max_width)
        self.labels["feet_cal"].grid(row=3, column=0, pady=5)
        self.Entry["feet_cal_var"] = ttk.Entry(self.frames["setcal"])
        self.Entry["feet_cal_var"].grid(row=3, column=0, pady=5)

        self.labels["inches_cal"] = ttk.Label(self.frames["setcal"], text="Height (inches):")
        self.labels["inches_cal"].grid(row=4, column=0, pady=5)
        self.labels["inches_cal_var"] = ttk.Entry(self.frames["setcal"])
        self.labels["inches_cal_var"].grid(row=4, column=1, pady=5)

        self.labels["weight_loss_cal"] = ttk.Label(self.frames["setcal"], text="Weight Loss Goal (lbs per week):")
        self.labels["weight_loss_cal"].grid(row=5, column=0, pady=5)
        self.labels["weight_loss_cal_var"] = ttk.Entry(self.frames["setcal"])
        self.labels["weight_loss_cal_var"] .grid(row=5, column=1, pady=5)

        self.Button["calculate_button_goal"] = ttk.Button(self.frames["setcal"], text="Calculate Calories", command=calculate_calories)
        self.Button["calculate_button_goal"] .grid(row=6, column=0,columnspan=2, pady=5)

        self.labels["result_label_goal"] = ttk.Label(self.frames["setcal"], text="")
        self.labels["result_label_goal"].grid(row=7, column=0, pady=5 ,columnspan=2)

        # # Frames for the page
        # # (name_of_frame, displayed_name)
        # self.frames = [
        #     ("info", "Information"),
        #     ("stats", "Statistics")
        # ]
        # for (frame_name, display_name) in self.frames:
        #     self.frames[frame_name] = ttk.Frame(self.notebook)
        #     self.notebook.add(self.frames[frame_name], text=display_name)
        
        # # Info fields are the label and then the value
        # # label_name, text, text_variable
        # info_fields = [
        #     ("lblName",             "Name: ",               ""),
        #     ("lblNameVar",          "",                     "person.name"),
        #     ("lblGender",           "Gender: ",             ""),
        #     ("lblGenderVar",        "",                     "person.gender"),
        #     ("lblAge",              "Age: ",                ""),
        #     ("lblAgeVar",           "",                     "person.age"),
        #     ("lblHeightFeet",       "Height (feet): ",      ""),
        #     ("lblHeightFeetVar",    "",                     "person.feet"),
        #     ("lblHeightInches",     "Height (inches): ",    ""),
        #     ("lblHeightInchesVar",  "",                     "person.inches")
        # ]
        # 
        # stat_fields = [
        #     ("lblBmi",              "BMI: ",                ""),
        #     ("lblBmiVar",           "",                     "person.bmi"),
        #     ("lblBmi",              "BMR: ",                ""),
        #     ("lblBmi",              "",                     "person.bmr"),
        # ]
        # 
        # fields_array = [info_fields, stat_fields]
        # 
        # for fields in fields_array:
        #     for (widget_name, display_name, textvar_name) in fields:
        #         self.labels[widget_name] = ttk.Label(self.frames[i], text=display_name, textvariable=textvar_name)
        #     label = ttk.Label(self.frames['bmi'], text=text + ":")
        #     label.grid(column=0, row=i, pady=5)
        #     if widget_type == 'combobox':
        #         widget = ttk.Combobox(self.frames['bmi'], values=values)
        #     else:
        #         widget = ttk.Entry(self.frames['bmi'])
        #     widget.grid(column=1, row=i, pady=5)
        #     self.frames['bmi'].text_field[text] = widget


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = Gui(root, Person(), DbAgent())
    root.mainloop()
