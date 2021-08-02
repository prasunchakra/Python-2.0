# Condition with Logical Operators
num = 12
if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    print("The number is a multiple of 2, 3, and 4")

# Nested If
num = 63
if num >= 0 and num <= 100:
    if 50 <= num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")

# If Else If
light = "Red"
if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Caution")
elif light == "Red":
    print("Stop")
else:
    print("Incorrect light signal")

