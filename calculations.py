#class to define income
#parameters will probably change when we add student loans
#Hannan - Income tax calculator made on 5/12/24, National Insurance 10/12/24
class Income:
    def __init__(self, name, income, monthly, plan, studentLoanDebt, studentLoanPlan, interestRate):
        #constructor method
        self.name = name
        self.income = income
        self.monthly = monthly
        self.plan = plan
        self.studentLoanDebt = studentLoanDebt
        self.studentLoanPlan = studentLoanPlan
        self.interestRate = interestRate

    #just a bunch of setters that store everything as private variables
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def income(self):
        return self.__income

    #passes the income to the float validator before setting it
    @income.setter
    def income(self, income):
        self.validateIncome(income)
        self.__income = income

    @property
    def monthly(self):
        return self.__monthly

    #same validation here
    @monthly.setter
    def monthly(self, monthly):
        self.validateIncome(monthly)
        self.__monthly = monthly

    @property
    def plan(self):
        return self.__plan

    #passes the plan to the NI plan validator to make sure its a valid plan
    @plan.setter
    def plan(self, plan):
        self.validatePlan(plan)
        self.__plan = plan

    @property
    def studentLoanDebt(self):
        return self.__studentLoanDebt

    #checks it is a float before setting like earlier
    @studentLoanDebt.setter
    def studentLoanDebt(self, studentLoanDebt):
        self.validateIncome(studentLoanDebt)
        self.__studentLoanDebt = studentLoanDebt

    @property
    def studentLoanPlan(self):
        return self.__studentLoanPlan

    # same here, plan is validated
    @studentLoanPlan.setter
    def studentLoanPlan(self, studentLoanPlan):
        self.validateStudentLoanPlan(studentLoanPlan)
        self.__studentLoanPlan = studentLoanPlan

    @property
    def interestRate(self):
        return self.__interestRate

    #also checks interest rate is a float
    @interestRate.setter
    def interestRate(self, interestRate):
        self.validateIncome(interestRate)
        self.__interestRate = interestRate

    #just a list of plans which are iterated through to check if the passed through plan is valid
    def validatePlan(self, plan):
        if plan not in ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 's', 'v', 'z']:
            raise ValueError("Invalid plan")

    #same thing here
    def validateStudentLoanPlan(self, studentLoanPlan):
        if studentLoanPlan not in ['1', '2', '3', '4', '5']:
            raise ValueError("Invalid plan")

    #checks that the passed though variable is a float and more than zero
    def validateIncome(self, value):
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                print("Not an integer")
        if value < 0:
            raise ValueError("Income must be greater than or equal to zero")

    #method calculates income after tax and returns
    def returnIncomeAfterTax(self):
        #depending on the bracket you are taxed differently, brackets are checked with if statements
        if self.income <= 12570:
            return self.income
        elif self.income <= 50270:
            return 12570 + ((self.income - 12570)*0.8)
        elif self.income <= 125140:
            #you have to take different amounts from each bracket of your income
            #so if the amount you earn under £50279 is taxed differently to that which is earned under £125140
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

    def returnNationalInsurance(self):
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
            contribution = planList[self.plan]["contribution1"] * 1048
            return contribution
        elif self.monthly > 1048 and self.monthly <= 4189:
            bracket1 = planList[self.plan]["contribution1"] * 1048
            bracket2 = planList[self.plan]["contribution2"] * (self.monthly - 1048)
            return bracket1 + bracket2
        elif self.__monthly > 4189:
            bracket1 = planList[self.plan]["contribution1"] * 1048
            bracket2 = planList[self.plan]["contribution2"] * (4189 - 1048)
            bracket3 = planList[self.plan]["contribution3"] * (self.monthly - 4189)
            return bracket1 + bracket2 + bracket3

    #again I made a nested dictionary that contains the threshold amount that you start paying contributions over,
    #the actual contribution percentage and the extra interest on top of RPI that the debt is increased by
    #the extra interest is redundant here but I got confused while making this so it's here
    def returnStudentRepayments(self):
        planList = {
            "1": {
                "threshold": 24990,
                "contribution": 0.09,
                "extraInterest": 0
            },
            "2": {
                "threshold": 27295,
                "contribution": 0.09
            },
            "3": {
                "threshold": 21000,
                "contribution": 0.06,
                "extraInterest": 0.03
            },
            "4": {
                "threshold": 31395,
                "contribution": 0.09,
                "extraInterest": 0.03
            },
            "5": {
                "threshold": 25000,
                "contribution": 0.09,
                "extraInterest": 0.03
            }
        }
        #calculation for yearly student loan contribution
        contribution = (self.income - planList[self.studentLoanPlan]["threshold"]) * planList[self.studentLoanPlan]["contribution"]
        return contribution

John = Income('John', 36790, 36790/12, "a", 29877, "2", 0.036)
print(John.returnIncomeAfterTax())
print(John.returnIncomeAfterTax() - John.returnNationalInsurance() * 12)
print(John.returnStudentRepayments())
#all of these calculations seem right based of online calculators used
#MSE used for the income tax
#www.student-loan-calculator.co.uk used for student finance validation