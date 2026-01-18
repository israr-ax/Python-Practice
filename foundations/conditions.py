# 1. Check Whether a Number Is Positive, Negative, or Zero
print("1. Check Whether a Number Is Positive, Negative, or Zero")

# num=int(input("Enter any number:"))
num=5
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")


# 2. Check Whether a Year Is a Leap Year    
print("2. Check Whether a Year Is a Leap Year")
# year=2024
year=int(input("Enter year:"))
if(year % 4 == 0 and year % 100!=0) or (year % 400==0):
    print("Leap Year")
else:
    print("Not a leap Year")