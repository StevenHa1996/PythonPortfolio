###Financial Statement Analysis###


#Data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#Profit for each month
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
profit = []
for i in range(0, len(revenue)):
    profit.append(revenue[i] - expenses[i])

#TAX

##THE CODE BELOW IS MY NORMAL WAY OF CODING. RESEARCH LIST COMPREHENSION
#tax = []
#for i in range(0, len(revenue)):
    #tax.append(profit[i] * 0.3)

tax = [round(0.3 * profit[i],2) for i in range(0, len(profit))] # multiply 0.3(30%) to every profit iterate, rounded to 2 decimal places
                                                                # in a new for loop for tax.


#PROFIT AFTER TAX
profit_tax = []

for i in range(0, len(profit)):
    profit_tax.append(profit[i] - tax[i])
profit_tax

#PROFIT MARGIN
profit_margin = []

for i in range(0, len(revenue)):
    profit_margin.append(profit_tax[i] / revenue[i])

profit_margin = [round(100 * profit_margin[i]) for i in range(0, len(profit_margin))]



#AVERAGE PROFIT THROUGHOUT 12 MONTH
meanprofit = sum(profit_tax) / len(revenue)


#GOOD MONTHS ABOVE MEAN PROFIT
good_months = []

for i in range(0, len(revenue)):
    good_months.append(profit_tax[i] > meanprofit)



#BAD MONTHS BELOW MEAN PROFITS
bad_months = []

for i in range(12):
    bad_months.append(profit_tax[i] < meanprofit)


#BEST MONTH
bestmonth = []

for i in range(12):
    bestmonth.append(profit_tax[i] == max(profit_tax))

#WORST MONTH
worstmonth = []

for i in range(12):
    worstmonth.append(profit_tax[i] == min(profit_tax))



#CONVERTING CALCULATIONS IN UNITS OF 1000 i.e 1k

revenue_1000 = [int(round(i/1000, 2)) for i in revenue]
expenses_1000 = [int(round(i/1000, 2)) for i in expenses]
profit_1000 = [int(round(i/1000, 2)) for i in profit]
profit_tax1000 =  [int(round(i/1000, 2)) for i in profit_tax]


print("Revenue:")
print(revenue_1000)
print("Expenses:")
print(expenses_1000)
print("Profit:")
print(profit_1000)
print("Tax:")
print(tax)
print("Profit after tax:")
print(profit_tax1000)
print("Profit margin:")
for i in profit_margin:
    print('{:.0f}%'.format(i))
print("Average profit throughout 12 months:")
print(meanprofit)
print("Good months:")
print(good_months)
print("Bad months:")
print(bad_months)
print("Best month:")
print(bestmonth)
print("Worst months:")
print(worstmonth)

#counter = 0
#for i in range(20):
#    print(i)
 #   counter = counter + 1


import calendar
month = []
for i in range(1,13):
    month.append(calendar.month_abbr[i])
month_profit = []
for i in range(0, len(profit)):
    month_profit.append (month[i] + ' -- ' + str(profit[i]))
print("\n")
print(month_profit)
