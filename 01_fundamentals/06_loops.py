# For Loop for specfic range
for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
    print(i, end=" ")
print()

# For loop over an array with Break, Continue and Pass
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            print(n1, n2)  # Print the pair
            found = True  # Set found to True
            break  # Break inner loop if a pair is found
    if found:
        break  # Break outer loop if a pair is found


num_list = list(range(0, 10))
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num, end=" ")
print()
num_list = list(range(20))
for num in num_list:
    pass # You can write code here later on

print(len(num_list))

# While Loop
n = 2  # Could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print(power)
