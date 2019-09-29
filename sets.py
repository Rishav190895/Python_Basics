
# ----------------------Sets-----------------------

s1=set([1,4,5,6])
s2=set([2,4,5,7])
s1.add(9) #adding 9 in set 1
s1.remove(4) #removing 4 from set 1
print(s1)
print(s1.intersection(s2))    #checking intersection between two sets
print(s1.union(s2))          #checking union
print(s1.isdisjoint(s2))    #checkig set is disjoint

# -----------------program-----------------------
"""----program to make a set from user input--------
         uncomment the following for run the program  """
# s=set()
# count=0
# while count<5:
#     user_input = int(input("enter the number that you wants to add : "))
#     count+=1
#     # user_input = int(input("enter the number that you wants to add : "))
#     s.add(user_input)
# print(s)