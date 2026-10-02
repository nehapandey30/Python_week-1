a=float(input("enter marks in english:"))
b=float(input("enter marks in maths:"))
c=float(input("enter marks in science:"))
avg=(a+b+c)/3
if avg>=90:
    grade="A"
    print("Grade: A")
elif avg>80 and avg<90:
    grade="B"
    print("Grade: B")
elif avg>70 and avg<80:
    grade="C"
    print("Grade: C")
else:
    grade="D"
    print("Grade: D")