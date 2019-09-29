
# ---------------------if_else_&_elif----------------------------
var1=87
var2=int(input("Enter the number "))

if var1<var2:
    print("Greater")
elif var1==var2:
    print("equal")
else:
    print("Lesser")

#-------------------Program-------------------------------
""" progarm to check person is under 18 or over 18 for drive """
user_input=int(input("Please Enter your age : "))

if  user_input<7 or user_input>100 :
    print("please enter valid age")
elif user_input>18 or user_input==18 :
    print("congratulation you are eligible for drive")
else:
    print("sorry ! you are not eligible for drive")