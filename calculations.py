#class to define income
#parameters will probably change when we add student loans
#Hannan - Income tax calculator made on 5/12/24, National Insurance 10/12/24
class Income:
    def __init__(self, name, income, monthly):
        self.name = name
        self.income = income

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income):
        self.validateIncome(income)
        self.__income = income

    def validateIncome(self, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                print("Not an integer")
        if value < 0:
            raise ValueError("Income must be greater than or equal to zero")



    #def validateIncome(self, value):

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

    def returnNationalInsurance(self, plan):
        #for now have done it for plan A
        #I am using nested dict to allow us to store all the brackets and plans in one place
        #the code below it takes the inputted plan that the user gives, finds it in the dictionary and uses its associated
        #percentages
        planList = {
            "a": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "b": {
            "contribution1": 0,
            "contribution2": 0.0185,
            "contribution3": 0.02
            },
            "c": {
            "contribution1": 0,
            "contribution2": 0,
            "contribution3": 0
            },
            "d": {
            "contribution1": 0,
            "contribution2": 0.02,
            "contribution3": 0.02
            },
            "e": {
            "contribution1": 0,
            "contribution2": 0.0185,
            "contribution3": 0.02
            },
            "f": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "h": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "i": {
            "contribution1": 0,
            "contribution2": 0.0185,
            "contribution3": 0.02
            },
            "j": {
            "contribution1": 0,
            "contribution2": 0.02,
            "contribution3": 0.02
            },
            "k": {
            "contribution1": 0,
            "contribution2": 0,
            "contribution3": 0
            },
            "l": {
            "contribution1": 0,
            "contribution2": 0.02,
            "contribution3": 0.02
            },
            "m": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "n": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "s": {
            "contribution1": 0,
            "contribution2": 0,
            "contribution3": 0
            },
            "v": {
            "contribution1": 0,
            "contribution2": 0.08,
            "contribution3": 0.02
            },
            "z": {
            "contribution1": 0,
            "contribution2": 0.02,
            "contribution3": 0.02
            }
        }

        #only the percentage contribution per threshold changes not the threshold itself
        #so we can use the threshold as the conditions and have the tax amount be taken from the dict
        if self.monthly <= 1048:
            contribution = planList[plan]["contribution1"] * 1048
            return contribution
        elif self.monthly > 1048 and self.monthly <= 4189:
            bracket1 = planList[plan]["contribution1"] * 1048
            bracket2 = planList[plan]["contribution2"] * (self.monthly - 1048)
            return bracket1 + bracket2
        elif self.monthly > 4189:
            bracket1 = planList[plan]["contribution1"] * 1048
            bracket2 = planList[plan]["contribution2"] * (4189 - 1048)
            bracket3 = planList[plan]["contribution3"] * (self.monthly - 4189)
            return bracket1 + bracket2 + bracket3

    #def returnStudentLoans(self):

John = Income('John', 36790)
print(John.returnIncomeAfterTax())
print(John.returnIncomeAfterTax() - John.returnNationalInsurance("a") * 12)
#getting take home pay of 30,008 from MSE calculator and 30008.88 from this so must be right.