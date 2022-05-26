"""
    Traditional medicine recommendation system main window ui
"""

from tkinter import *
from tkinter import ttk, messagebox
from register import *

global mainWindow
global symp_var
global disease_name
global medicine_type
global med_type_list
global left_disease_name
global lang
key = ""
med_type_list = ""
font = ""
size = ""
note = ""
language= "English"


def get_attr():
    globals()['key'] = ui_key_english if language == "English" else ui_key_tamil
    globals()['med_type_list'] = med_type_in_english if language == "English" else med_type_in_tamil
    globals()['font'] = english_font if language == "English" else tamil_font
    globals()['size'] = ui_size_english if language == "English" else ui_size_tamil
    globals()['note'] = key[16]


class HomeUi:
    note = globals()['note']

    def __init__(self, window):
        get_attr()
        self.home = window
        self.home.title(key[0])
        globals()['symp_var'] = StringVar()
        globals()['disease_name'] = StringVar()
        globals()['medicine_type'] = StringVar()
        globals()['left_disease_name'] = StringVar()
        globals()['symp_var'].set("symp")
        globals()['lang'] = StringVar()
        # globals()['symp_var'] = StringVar()

        self.left_top = LabelFrame(self.home, width="749", height="39", bd=4)
        self.left_top.grid(row=0, column=0)

        self.symptoms_radio = Radiobutton(self.left_top,
                                          text=key[1],
                                          variable=globals()['symp_var'], value="symp", command=self.radio_change)
        self.symptoms_radio.grid(row=0, column=0)
        Label(self.left_top, text="                ").grid(row=0, column=1)
        self.disease_radio = Radiobutton(self.left_top, text=key[2], variable=globals()['symp_var'],
                                         value="disease", command=self.radio_change)
        self.disease_radio.grid(row=0, column=2)
        Label(self.left_top, text=" " * 10).grid(row=0, column=3)

        self.left_up = LabelFrame(self.home, width="749", height="459", bd=4)
        self.left_up.grid(row=1, column=0)
        self.symptoms_entry_label = Label(self.left_up, text=key[3], font=("bold", 16))
        self.symptoms_entry_label.place(x=10, y=12)
        self.lang_label = Label(self.left_up, text=key[17])
        self.lang_label.place(x=350, y=10)
        self.lang_combo = ttk.Combobox(self.left_up, textvariable=globals()['lang'])
        self.lang_combo['values'] = lang_
        self.lang_combo.place(x=400, y=12)
        self.lang_button = Button(self.left_up, text="select" if language == "English" else "தேர்ந்தெடு", font=("ariel", 8),
                                  command=self.change)
        self.lang_button.place(x=580, y=10)

        self.symptoms_entry_info_label = Label(self.left_up, text=key[4], font=("bold", 12))
        self.symptoms_entry_info_label.place(x=70, y=60)
        self.symptoms_frame = LabelFrame(self.left_up, width="450", height="280", bd=3, bg="white")
        self.symptoms_frame.place(x=70, y=90)
        self.left_top_add_button = Button(self.left_up, text=key[5], width=12, command=self.get_symptoms)
        self.left_top_add_button.place(x=530, y=95)
        self.left_top_remove_button = Button(self.left_up, text=key[6], width=12)
        self.left_top_remove_button.place(x=530, y=130)
        self.left_top_diagnosis_button = Button(self.left_up, text=key[7], width=12, bg="orange")
        self.left_top_diagnosis_button.place(x=220, y=400)

        self.left_down = LabelFrame(self.home, width="749", height="307", bd=4)
        self.left_down.grid(row=2, column=0)

        self.disease_entry_label = Label(self.left_down, text=key[8], font=("bold", 16))
        self.disease_entry_label.place(x=10, y=10)
        self.left_down_note_label = Label(self.left_down, text=self.note)
        self.left_down_note_label.place(x=30, y=170)
        self.disease_info_label = Label(self.left_down, text=key[9], font=("bold", 14))
        self.disease_info_label.place(x=30, y=100)
        self.left_down_disease_entry = Entry(self.left_down, textvariable=globals()['disease_name'], width="40")
        self.left_down_disease_entry.place(x=180, y=104)
        self.left_down_confirm = Button(self.left_down, text=key[10], bg="orange", font=("ariel", 12), width=16)
        self.left_down_confirm.place(x=510, y=98)

        self.right_up = LabelFrame(self.home, width="749", height="798", bd=4)
        self.right_up.grid(row=0, column=1, rowspan=3)

        self.right_up_label = Label(self.right_up, text=key[11], font=("bold", 22))
        self.right_up_label.place(x=20, y=50)
        self.disease_label = Label(self.right_up, text=key[12], font=("bold", 12))
        self.disease_label.place(x=140, y=200)
        self.disease_entry = Entry(self.right_up, textvariable=globals()['disease_name'], width="50", state="disabled",
                                   bg="white")
        self.disease_entry.place(x=270, y=204)
        self.disease_label = Label(self.right_up, text=key[13], font=("bold", 12))
        self.disease_label.place(x=140, y=240)
        self.med_type = ttk.Combobox(self.right_up, textvariable=globals()['medicine_type'])
        self.med_type['values'] = globals()['med_type_list']
        self.med_type.place(x=270, y=244)
        self.med_confirm = Button(self.right_up, text=key[14], bg="orange")
        self.med_confirm.place(x=270, y=284)
        self.sug_label = Label(self.right_up, text=key[15], font=("bold", 15))
        self.sug_label.place(x=50, y=400)
        self.sug_med = Text(self.right_up, width=70, height=20)
        self.sug_med.place(x=50, y=440)

        self.radio_change()

        self.home.mainloop()

    def change(self):
        globals()['language'] = globals()['lang'].get()
        self.home.destroy()
        main_window = Tk()
        main_window.geometry("1500x800+40+20")
        HomeUi(main_window)

    def get_symptoms(self):
        temp_window = Tk()
        temp_window.title("Symptoms Selection Window")
        temp_window.geometry("500x200+700+300")

        symptom_var = StringVar()

        def set_symptom():
            print("  ", symptom_var.get())
                # temp_window.destroy()

        symptoms_label = Label(temp_window, text="Select Symptom", font=("Bold", 14))
        symptoms_label.place(x=40, y=20)
        symptoms_combo = ttk.Combobox(temp_window, textvariable=symptom_var, font=("Italic", 13))
        symptoms_combo['values'] = symptoms_english
        symptoms_combo.place(x=40, y=80)
        confirm_button = Button(temp_window, text="Confirm", command=set_symptom)
        confirm_button.place(x=320, y=78)
        temp_window.mainloop()

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
mainWindow.geometry("1500x800+40+20")
if __name__ == "__main__":
    home_ui = HomeUi(mainWindow)

