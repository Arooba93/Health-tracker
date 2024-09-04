from gui import Gui
from db_agent import DbAgent
import tkinter as tk


if __name__ == "__main__":
    db_agent = DbAgent()
    person = db_agent.get_person()
    root = tk.Tk()
    app = Gui(root, person, db_agent)
    root.mainloop()
