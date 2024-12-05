#class to define income
#parameters will probably change when we add student loans
class Income:
    def __init__(self, name, income):
        self.name = name
        self.income = income

    #method calculates income income after tax and returns
    def returnIncomeAfterTax(self):
        if self.income <= 12570:
            return self.income
        elif self.income <= 50270:
            return 12570 + ((self.income - 12570)*0.8)
        elif self.income <= 125140:
            bracket1 = 12570
            bracket2 = (50270-12570)*0.8
            bracket3 = (self.income - 50270)*0.6
            return bracket1 + bracket2 + bracket3
        elif self.income > 125140:
            bracket1 = 12570
            bracket2 = (50270-12570)*0.8
            bracket3 = (125140 - 50270)*0.6
            bracket4 = (self.income - 125140)*0.55
            return bracket1 + bracket2 + bracket3 + bracket4

John = Income('John', 36790)
print(John.returnIncomeAfterTax())
#seem to be getting the right answers based on the MSE calculator if I exclude the National Insurance