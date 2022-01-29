mark=int(input("Enter Your Marks:\n"))

if(mark>=90):
    Grade="EX"
elif(mark>=80):
    Grade="A"
elif(mark>=70):
    Grade="B"
elif(mark>=60):
    Grade="C"
elif(mark>=50):
    Grade="D"
else:
    Grade="F"

print("Your Grade is " + Grade)
