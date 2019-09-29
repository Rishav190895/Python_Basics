#-------------------------Exception_handling------------------
""""for printing error we use Try: except error """

num1=input("Enter the number: ")
num2=input("Enter the number: ")

#if you will enter string value in input then it will show error

try:
    print(f"sum of the two number is {int(num1)+int(num2)}")
except:
    print("please Enter the Integer value in input")

print("this line is going to print after error")

func1()
