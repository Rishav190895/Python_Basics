# ---------------------Global_variable-----------------------

x=34   # Global variable
def akhil():
    print("the way you make me feel")

    """if you delete the line (global x) output will be 34, 23"""
    global x # (global keyword) assigning the value to the x outside the function
    x=23 #local variable
    print(x)

akhil()
print(x)