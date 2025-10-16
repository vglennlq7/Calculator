#This is my first calculator
print("************************************")
print("********WELCOME TO THE MOST*********")
print("*****SIMPLE CALCULATOR ON EARTH*****")
print("************************************")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Now choose the operation: +, -, *, /")
result = input("Your operation: ")

if result == '+' : 
    print("The result is: " , number1 + number2)
    print("That is all 👋😊. ")
elif result == '-' : 
    print("The result is: ", number1 - number2)
    print("That is all 👋😊.")
elif result == '*' :
    print("The result is :", number1 * number2)
    print("That is all 👋😊.")
elif result == '/':
    if number2 !=0 :
        print("The result is:", number1 / number2)
        print("Tha is all 👋😊.")
    else :
        print("Error ⚠️ , cannot divide by zero")
else :
    print("Error not found 🤖")

