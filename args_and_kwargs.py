#-----------------args and Kwargs----------------------------------

def main(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for a,b in kwargs.items():
        print(f"{a} is a {b} of the class")
ak=["john", "wick","sam", "prince","leo"]
you="oh yeah its normal "
be={"anna":"student","prince":"monitor","fereday":"teacher"}
main(you,*ak,**be)
