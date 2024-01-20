grade  = ""  
remarks = ""
marks = float(input("Enter Marks"))

if marks<40:
    grade="F"
    remarks = "You are failed n cannot be in next class"
elif marks <50:
    grade ="E"
    remarks="You have low performance need much hardwork"
elif marks <60:
    grade ="D"
    remarks="You have average performance need more attension"
elif marks <70:
    grade ="C"
    remarks="You have average performance need more attension"
elif marks <80:
    grade ="B"
    remarks="you have good performer"
elif marks <90:
    grade ="A"
    remarks="you have excellent performer"
else:
    grade ="A*"
    remarks="you have exceptional performer"
print(f"Your grade is {grade}")