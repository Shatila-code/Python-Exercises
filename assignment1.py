#Exercise 1

age =int(input("Welcome to our program enter your age to calculate the price of the movie ticket"))

ticketPrice=0
if age<10:
    ticketPrice=8

elif age >= 10 and age<=13:
    ticketPrice=12

elif age>=14 and age <=45:
    ticketPrice=25

elif age>=46 and age<=60:
    ticketPrice=20


print("the ticketprice is $",ticketPrice)




#Exercise 2

num=int(input("Enter a number :"))

if num>0:
    print("The number is even")

elif num<0:
    print("The number is odd")  


#Exercise 3

userName = input("Enter username: ")
password= int(input("Enter password: "))

if userName=="admin" and password==1234:
    print("Access granted")

else:
    print("Access denied")    

