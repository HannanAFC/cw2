# cw2
Repository for Coursework 2 for Tax Calculator

<h1>CW2 Tax Breakdowns</h1>
<h2>References</h2>
Source for Income Tax: https://www.gov.uk/income-tax-rates<br>
Source for student finance: https://www.thecompleteuniversityguide.co.uk/student-advice/finance/student-loan-repayment-calculator<br>
Source for National Insurance Contributions: https://www.gov.uk/national-insurance-rates-letters<br>
Source for NI Categories Breakdown: https://www.gov.uk/national-insurance-rates-letters/category-letters<br>
Used this to validate income tax calculations: https://www.moneysavingexpert.com/tax-calculator/<br>
Used this to validate student loan repayments: https://www.thecompleteuniversityguide.co.uk/student-advice/finance/student-loan-repayment-calculator<br>

<h2>Tax Brackets</h2>
- Income below and at £12,570 not taxed
- Income above £12,570 to £50,270 taxed at 20%
- Income above £50,270 to £125,140 taxed at 40%
- Income above £125,140 taxed at 45%

<h2>Student Loan Repayments</h2>
Student loans repayments are taken once per pay period, so that depends on whether you earn weekly, monthly, yearly etc.

Plan 1, if you earn over:
* £24,990 a year
* £2,082 a month
* £480 a week
You will pay 9% of the amount you earn over the threshold. Threshold income and interest rates increase every year. Interest rates based on RPI.

Plan 2, if you earn over:
* £27,295 a year
* £2,274 a month
* £524 a week
You only start repaying this plan if you earn over £28,470. This makes it more complicated for anybody who would have changing monthly incomes but we can exclude these examples if needed as they make it a bit too complex. We could clarify this tool is for people who have predefined incomes for the year. Threshold income and interest rates increase every year. Might be too complex to implement the sliding scale RPI scale but included screenshot below.
![Plan 2 PRI Breakdown](readmeImages/plan2_breakdown.jpg?raw=true)

Plan 3 (Postgrad Loan), if you earn over:
* £21,000 a year
* £1,750 a month
* £403 a week
No annual increase for this threshold as of now and for the foreseeable future. You pay 6% of the amount earned over the threshold. Interest rate is RPI + 3%.

Plan 4 (only applies to Scottish students, worth including?). Repayment threshold is:
* £31,395 per year
* £2,616 per month
* £603 per week
Threshold increases every year, you repay 9% of income above the threshold, interest rate are based on RPI.

Plan 5 “for students from England taking out undergraduate student finance after 1 August 2023”. So we’ll have to ask what year the user took out their student loans. If you earn over:
* £25,000 per year
* £2,083 per month
* £480 per week
Threshold Increases every year. You repay 9% of your income over this amount interest rates based on RPI.

<h2>National Insurance Contributions</h2>
Most employees are category A, category can be found on pay slip.<br>

![Categories Breakdown 2](readmeImages/category1.jpg?raw=true)
![Categories Breakdown 2](readmeImages/category2.jpg?raw=true)
![Categories Breakdown 3](readmeImages/category3.jpg?raw=true)
Category X is for people who don’t have to pay national insurance, for example, under 16’s.
