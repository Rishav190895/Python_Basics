#------------------------map_and_lambda_-----------------
print("Map and lambda function")
number=["3","4","5","8"]
c=[int(i) for i in number]
print(c)
add=list(map(lambda x:x+2,c))
print(add,"\n")

# -----------------------filter()------------------------

print("filter function")
ls=[1,4,5,6,9,11]

def gr_5(num):
    return num>5
gr_is=list(filter(gr_5,ls))
print(gr_is,"\n")

# --------------reduce()-----------------
print("reduce function")
from functools import reduce
ls1=[1,2,3,4,5]
num_l=reduce(lambda x,y:x+y,ls1)
print(num_l)