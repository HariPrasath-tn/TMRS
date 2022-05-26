"""
    Traditional medicine recommendation system main window ui
"""

from tkinter import *
from tkinter import ttk, messagebox

global mainWindow
global symp_var
global disease_name
global medicine_type
global med_type_list
global left_disease_name
med_type_list = ['Ayurveda', 'Siddha', 'Unani']


class HomeUi:
    note = "(Note: Please enter a valid disease. Before pressing \"Confirm\" button please verify disease name spelling)"

    def __init__(self, window):
        self.home = window
        globals()['symp_var'] = StringVar()
        globals()['disease_name'] = StringVar()
        globals()['medicine_type'] = StringVar()
        globals()['left_disease_name'] = StringVar()
        globals()['symp_var'].set("symp")
        # globals()['symp_var'] = StringVar()
        # globals()['symp_var'] = StringVar()

        self.left_top = LabelFrame(self.home, width="749", height="39", bd=4)
        self.left_top.grid(row=0, column=0)

        self.symptoms_radio = Radiobutton(self.left_top,
                                          text="I don't know the disease name, I want to enter the symptoms",
                                          variable=globals()['symp_var'], value="symp", command=self.radio_change)
        self.symptoms_radio.grid(row=0, column=0)
        Label(self.left_top, text="                    ").grid(row=0, column=1)
        self.disease_radio = Radiobutton(self.left_top, text="I know the disease name", variable=globals()['symp_var'],
                                         value="disease", command=self.radio_change)
        self.disease_radio.grid(row=0, column=2)
        Label(self.left_top, text=" " * 54).grid(row=0, column=3)

        self.left_up = LabelFrame(self.home, width="749", height="459", bd=4)
        self.left_up.grid(row=1, column=0)
        self.symptoms_entry_label = Label(self.left_up, text="Disease Diagnosis Tab", font=("bold", 16))
        self.symptoms_entry_label.place(x=10, y=10)
        self.symptoms_entry_info_label = Label(self.left_up, text="Select the symptoms", font=("bold", 12))
        self.symptoms_entry_info_label.place(x=70, y=60)
        self.symptoms_frame = LabelFrame(self.left_up, width="450", height="280", bd=3, bg="white")
        self.symptoms_frame.place(x=70, y=90)
        self.left_top_add_button = Button(self.left_up, text="Add", width=12)
        self.left_top_add_button.place(x=530, y=95)
        self.left_top_remove_button = Button(self.left_up, text="Remove", width=12)
        self.left_top_remove_button.place(x=530, y=130)
        self.left_top_diagnosis_button = Button(self.left_up, text="Diagnosis", width=12, bg="orange")
        self.left_top_diagnosis_button.place(x=220, y=400)

        self.left_down = LabelFrame(self.home, width="749", height="307", bd=4)
        self.left_down.grid(row=2, column=0)

        self.disease_entry_label = Label(self.left_down, text="Disease Entry Tab", font=("bold", 16))
        self.disease_entry_label.place(x=10, y=10)
        self.left_down_note_label = Label(self.left_down, text=self.note)
        self.left_down_note_label.place(x=30, y=170)
        self.disease_info_label = Label(self.left_down, text="Disease Name : ", font=("bold", 14))
        self.disease_info_label.place(x=30, y=100)
        self.left_down_disease_entry = Entry(self.left_down, textvariable=globals()['disease_name'], width="50")
        self.left_down_disease_entry.place(x=180, y=104)
        self.left_down_confirm = Button(self.left_down, text="Confirm", bg="orange", font=("ariel", 12), width=14)
        self.left_down_confirm.place(x=550, y=94)

        self.right_up = LabelFrame(self.home, width="749", height="798", bd=4)
        self.right_up.grid(row=0, column=1, rowspan=3)

        self.right_up_label = Label(self.right_up, text="Medicine Recommendation Area", font=("bold", 22))
        self.right_up_label.place(x=20, y=50)
        self.disease_label = Label(self.right_up, text="Disease name : ", font=("bold", 12))
        self.disease_label.place(x=140, y=200)
        self.disease_entry = Entry(self.right_up, textvariable=globals()['disease_name'], width="50", state="disabled",
                                   bg="white")
        self.disease_entry.place(x=270, y=204)
        self.disease_label = Label(self.right_up, text="Medicine Type : ", font=("bold", 12))
        self.disease_label.place(x=140, y=240)
        self.med_type = ttk.Combobox(self.right_up, textvariable=globals()['medicine_type'])
        self.med_type['values'] = globals()['med_type_list']
        self.med_type.place(x=270, y=244)
        self.med_confirm = Button(self.right_up, text="Confirm and Fetch Medicine", bg="orange")
        self.med_confirm.place(x=270, y=284)
        self.sug_label = Label(self.right_up, text="List of Medicine suggested : ", font=("bold", 15))
        self.sug_label.place(x=50, y=400)
        self.sug_med = Text(self.right_up, width=70, height=20)
        self.sug_med.place(x=50, y=440)

        self.radio_change()

        self.home.mainloop()

    def radio_change(self):
        option = globals()['symp_var'].get()
        if option == "symp":
            self.left_down_disease_entry.config(state=DISABLED)
            self.left_down_confirm.config(state=DISABLED)
            self.left_top_remove_button.config(state=NORMAL)
            self.left_top_diagnosis_button.config(state=NORMAL)
            self.left_top_add_button.config(state=NORMAL)
        else:
            self.left_down_disease_entry.config(state=NORMAL)
            self.left_down_confirm.config(state=NORMAL)
            self.left_top_remove_button.config(state=DISABLED)
            self.left_top_diagnosis_button.config(state=DISABLED)
            self.left_top_add_button.config(state=DISABLED)


mainWindow = Tk()
mainWindow.title("Traditional medicine recommendation system")
mainWindow.geometry("1500x800+40+20")
if __name__ == "__main__":
    home_ui = HomeUi(mainWindow)
