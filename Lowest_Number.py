# Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number
# Steps

# Add scenario
def showScene():
    print("Diane, Daniel, and Dayne have their own money savings. At the end of November, they are about to open their piggy banks. They wanted to know who has the lowest savings among them.")

# Ask for 3 numbers.
def savingAmount():
    Savings1 =  float(input("How much money does Diane saved?: "))
    Savings2 = float(input("How much money does Daniel saved?: "))
    Savings3 = float(input("How much money does Dayne saved?: "))
    return Savings1, Savings2, Savings3

# Use if-else statement to find the lowest number.
def lowestNumber(Savings1, Savings2, Savings3):
    if Savings1 < Savings2 and Savings1 < Savings3:
        print("The lowest number among the three savings amount is",Savings1)
    else:
        if Savings2 < Savings1 and Savings2 < Savings3:
            print("The lowest number among the three savings amount is",Savings2)
        else:
            if Savings3 < Savings1 and Savings3 < Savings2:
                print("The lowest number among the three savings amount is",Savings3)

# Closing program
def showEndScene():
    print("Now they know who has the lowest number of savings.")

Set1 = showScene()
savings1, savings2, savings3 = savingAmount()
lowestNumber(savings1, savings2, savings3)
displayTotal = showEndScene()