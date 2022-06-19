# a=input("Enter your pin: ")
content= True
i=1
with open("acc.txt") as f:
    while content:
        content=f.readline
        if 1234 in content:
            print(content)
            print("yes")
        i+=1