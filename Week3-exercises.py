
salary=float(input('Welcome nabhia enter your salary: '))
monthName=input('enter the name of the month: ')

print("input the following percentages for: a) Savings b) Rent c) Electricity :")


listOfExpenses=dict()
for i in range(3):
    choice= input("choose :")
    percentage=int(input('now enter the percentage '))

    result= salary*(percentage/100)

    if choice == 'a':
        listOfExpenses["Savings"]=result
    elif choice == 'b':
        listOfExpenses["Rent"]=result

    elif choice == 'c':
        listOfExpenses["Electricity"]=result    

totalExpenses=sum(listOfExpenses.values())
print(f'the total expenses is {totalExpenses}')
print(f"the remaining of your salary is: {salary-totalExpenses}")

for K,V in listOfExpenses.items():
    print(f"the yearly expenses for {K} is {V*12}$")

print(f'for fun your salary in the power of 2 {pow(salary,2)}')


randAmount=float(input('enter an additional amount:'))
print(f'{randAmount}$ represents {randAmount / listOfExpenses["Savings"]*100}% of your savings')

