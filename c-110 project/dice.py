import random
response="y"
while response=="y":
    no = random.randint(1,6)
    if no==1:
        print("0")
    if no==2:
        print("0 0")
    if no==3:
        print("0 0 0")
    if no==4:
        print("0 0 0 0")
    if no==5:
        print("0 0 0 0 0")
    if no==6:
        print("0 0 0 0 0 0")
    response=input("press y to roll and n to exit")
    print("\n")

