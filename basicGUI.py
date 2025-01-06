# gui for the project ~Matthew
# initially added on 3/12/24, updated on 4/12/24
from tkinter import Tk, Label, Entry, Button, messagebox, Text
from tkinter import ttk
from calculations import Income


class TakeHomeGUI:
    # creates the size and title of the tkinter window
    def __init__(self, root):
        self.root = root
        self.root.title("Take Home Pay Calculator")
        self.root.geometry('400x500')

        # Create labels and entry/combobox/textbox fields for each input
        self.create_label_and_entry("Username")
        self.create_label_and_entry("Annual Gross Income")
        self.create_label_and_entry("Interest Rate")
        self.create_label_and_entry("Student Loan Debt Remaining")
        self.create_label_and_combobox("Student Loan Plan", ["1", "2", "3", "4", "5"])
        self.create_label_and_combobox("National Insurance Plan",
                                       ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "s", "v",
                                        "z"])
        self.create_label_and_entry("Errors")
        self.create_label_and_entry("Take Home Pay")

        # Creates sign up button, when clicked runs the function Sign_Up
        sign_up_button = Button(self.root, text="Calculate", command=self.Sign_Up)
        sign_up_button.pack()

    def create_label_and_entry(self, text):
        label = Label(self.root, text=text)
        label.pack()
        entry = Entry(self.root)
        entry.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Entry", entry)
        # Function allows you to create a label and entry and takes the label text to create the entry name

    def create_label_and_combobox(self, text, values):
        label = Label(self.root, text=text)
        label.pack()
        combobox = ttk.Combobox(self.root, state="readonly", values=values)
        combobox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Combobox", combobox)
        # Function allows you to create a label and combobox and takes the label text to create the combobox name

    def create_label_and_textbox(self, text):
        label = Label(self.root, text=text)
        label.pack()
        textbox = Text(self.root, height=10, width=30)
        textbox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Textbox", textbox)
        # Function allows you to create a label and textbox and takes the label text to create the textbox name

    def Sign_Up(self):
        Username = self.usernameEntry.get()
        Annual_Gross_Income = self.annual_gross_incomeEntry.get()
        Interest_Rate = self.interest_rateEntry.get()
        National_Insurance_Plan = self.national_insurance_planCombobox.get()
        Student_Loan_Debt_Remaining = self.student_loan_debt_remainingEntry.get()
        Student_Loan_Plan = self.student_loan_planCombobox.get()
        Errors = self.errorsEntry.get()
        try:
            user = Income(Username, float(Annual_Gross_Income), float(Annual_Gross_Income)/12, National_Insurance_Plan, float(Student_Loan_Debt_Remaining), Student_Loan_Plan, float(Interest_Rate))
            self.take_home_payEntry.delete(0)
            self.take_home_payEntry.insert(0, (user.returnIncomeAfterTax() - user.returnNationalInsurance() * 12))
        except ValueError:
            messagebox.showerror("Error", "Income cannot be calculated")

    # Function Sign_Up creates variables for each input entered when the button is clicked, so that it can be used in other areas of the program

if __name__ == "__main__":
    root = Tk()
    app = TakeHomeGUI(root)
    root.mainloop()