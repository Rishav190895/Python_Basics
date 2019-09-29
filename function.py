# ------------------------function-------------------------------------------
""" block of organised, reusable code that is used to
           perform a single related action """


def add(a,b):
    """this  multiline comment is doc_string of the function """
    return a+b

print(add(3,4))
print(add.__doc__) # printing the doc string of the function



# it can be user define and built in function
a=12
b=12
c=sum((a,b)) #Here sum is a built in function
print(c)
