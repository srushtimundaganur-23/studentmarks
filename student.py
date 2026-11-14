name = input("enter student name:")
marks = input("enter student marks:")
m1 = int(input("enter the marks in subject 1:"))
m2 = int(input("enter the marks in subject 2:"))
m3 = int(input("enter the marks in subject 3:"))

total = m1+m2+m3
average = total/3
print("\n --- Student Mark DDetails ---")
print("Student Name:",name)
print("Total Marks:",total)
print("Average Marks:",average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
    
