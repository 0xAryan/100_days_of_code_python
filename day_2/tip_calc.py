print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input('How many people to split the bill? '))

tip = (percent / 100) * bill
total_bill = bill + tip
each_pay = total_bill / no_of_people
final_pay = round(each_pay, 2)
print(f'Each person should pay: $ {each_pay}')