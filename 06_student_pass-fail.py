a=int(input("Enter your 1st subject mark\n"))
b=int(input("Enter your 2nd subject mark\n"))
c=int(input("Enter your 3rd subject mark\n"))

if(a<33 or b<33 or c<33):
    print("You are Fail due to Insuficient mark")
elif(a+b+c)/3 < 40:
    print("You are Fail due to Insuficient Percentage")
else:
    print("You are pass")

