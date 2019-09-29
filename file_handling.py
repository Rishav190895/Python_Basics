# ------------------file_handling-----------------------------


f=open("akhil.txt","r+")
f.write("love the way you lie\n")

# f.write "w" - clear the recent text and add new content in the file
# f.read "r"  - predefined mode use to read the text
# f.write "r+"- read the content and and add new content in it
# f.append "a"- add new content in the file



# print(f.readlines()) #printing text in the list
# content=f.read() printing text
# print(content)

for line in f:      #same as above
    print(line, end="")


f.close() #for closing the file