__author__ = 'w0285677'

#1. Prompt the user to enter three numbers.
print("We're gonna need ya to enter three numbers...")
numberOne = float(input("First number: "))
numberTwo = float(input("Second number: "))
numberThree = float(input("Third number: "))

#2. Display a message confirming the numbers the user entered.
print("You did it! They're all numbers!")

#3. Calculate the average of the three numbers.
average = (numberOne + numberTwo + numberThree) / 3.0

#4. Display the average, rounded to two decimal places.
print("The average of your numbers is: " + str(round(average, 2)))
