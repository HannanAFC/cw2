import smtplib
import openpyxl
from tkinter import Tk, Label, Entry, Button, messagebox, Text
from tkinter import ttk


class TakeHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Home Pay Calculator")
        self.root.geometry('400x500')

        # Create labels and entry fields for each input
        self.create_label_and_entry("Username")
        self.create_label_and_entry("Password")
        self.create_label_and_combobox("Annual Gross Income", ["< £12,570", "£12,571-£50,270", "£50,271-£125,140", ">£125,140"])
        self.create_label_and_combobox("Employment Status", ["Employed", "Self Employed", "Unemployed", "Student", "Other"])
        self.create_label_and_entry("Debt")
        self.create_label_and_textbox("Additional Information")

        sign_up_button = Button(self.root, text="Sign Up", command=self.Sign_Up)
        sign_up_button.pack()
    def create_label_and_entry(self, text):
        label = Label(self.root, text=text)
        label.pack()
        entry = Entry(self.root)
        entry.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Entry", entry)

    def create_label_and_combobox(self, text, values):
        label = Label(self.root, text=text)
        label.pack()
        combobox = ttk.Combobox(self.root, state="readonly", values=values)
        combobox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Combobox", combobox)

    def create_label_and_textbox(self, text):
        label = Label(self.root, text=text)
        label.pack()
        textbox = Text(self.root, height=10, width=30)
        textbox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Textbox", textbox)

    def Sign_Up(self):
        Username = self.usernameEntry.get()
        Password = self.passwordEntry.get()
        Annual_Gross_Income = self.annual_gross_incomeCombobox.get()
        Employment_Status = self.employment_statusCombobox.get()
        Debt = self.debtEntry.get()
        Additional_Information = self.additional_informationTextbox.get("1.0", "end-1c")
        



if __name__ == "__main__":
    root = Tk()
    app = TakeHomeGUI(root)
    root.mainloop()
    
