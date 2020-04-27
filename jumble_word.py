import random
print("welcome to jumble word")

print("1. easy")
print("2. medium")
print("3. hard")

n=int(input("select level number: "))

l1=["any","day","die","dig","all","age","dry"]
l2=["calm", "care", "cool", "coal", "dope", "duty", "mark"]
l3=["able","also","away","baby","bath","base","ball"]
for i in range(1,6):
    count=0
    if n==1:
        x1=random.choice(l1)
        val=list(x1)
        random.shuffle(val)
        res="".join(val)
        print("your jumble is: ",res)
        z=input("your guess: ")
        if z==x1:
            print("correct")
            count=count+1
        else:
            print("wrong")
    print(count)
    
    if n==2:
        x1=random.choice(l2)
        val=list(x1)
        random.shuffle(val)
        res="".join(val)
        print("your jumble is: ",res)
        z=input("your guess: ")
        if z==x1:
            print("correct")
        else:
            print("wrong")


    if n==3:
        x1=random.choice(l3)
        val=list(x1)
        random.shuffle(val)
        res="".join(val)
        print("your jumble is: ",res)
        z=input("your guess: ")
        if z==x1:
            print("correct")
        else:
            print("wrong")










            



        
    
