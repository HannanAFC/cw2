#Pie chart for visualisation of tax breakdown - Joel

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from calculations import Income
#assigning variables to put into pie chart
"""John = Income('John', 36790, 36790 / 12, "a", 29877, "2", 0.036)"""
take_home = John.returnIncomeAfterTax() - (John.returnNationalInsurance() * 12)
national_insurance = John.returnNationalInsurance() * 12
income_tax = John.income - John.returnIncomeAfterTax()
student_loan = 2 #placeholder
#creating pie chart
def pie_chart():
    #assigning variables to pie chart labels
    y = ([take_home, national_insurance, income_tax, student_loan])
    labels = [("Take Home pay" , take_home), ("National Insurance", national_insurance) , ("Income Tax", income_tax) , "Student loan repayments"]
    #creating pie chart
    fig, ax = plt.subplots()
    ax.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Your Tax Breakdown")
    #allowing pie chart to show in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
#placeholder tkinter window for testing
"""window = tk.Tk()
window.title("Your Tax Breakdown")
button=tk.Button(window, text="Pie", command=pie_chart)
button.pack()
window.mainloop()"""