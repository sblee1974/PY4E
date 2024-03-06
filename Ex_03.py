# Program to calculate gross pay with overtime work
# Rewrite the code with try/exception statement
try:
    Hours = float(input("Enter Hours: "))
except:
    print("Error, please enter numeric input")
    exit()

try:
    Rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    exit()

Overtime = Hours - 40
if Overtime > 0:
    GrossPay = ((Hours - Overtime) * Rate) + (Overtime * Rate * 1.5)
else:
    GrossPay = Hours * Rate

print("Pay:", GrossPay)