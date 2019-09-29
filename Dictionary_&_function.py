# -------------------dictionary----------------
"""   is_key_value_pair     """

d1={"fish":"water","loin":"jungle"}
d1["moon"]="sky" #adding new value
d1.update({"love":"hurts"}) #same as above

print(d1.keys()) #printing keys
print(d1.values()) #printing values
print(d1.items(),"\n") #printing_values
# d2=d1.copy() for copy dictionary in new variable

# --------------Converting_dictionary_into_list------------
print("method for converting dictionary into list :" )


""" method 1 using list comprehension """
lis=[(k,v) for k,v in d1.items()]
print(lis)

"""  method 2 using items """
lis2=list(d1.items())
print(lis3)

"""  method 3 using zip """
lis3=zip(d1.keys(),d1.values())
lis3=list(lis3)
print(lis3)

""" method 4  iteration """
lis4=[]
for i in d1:
    k=(i,d1[i])
    lis4.append(k)
print(lis4)





