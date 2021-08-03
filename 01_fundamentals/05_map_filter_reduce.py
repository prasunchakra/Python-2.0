from functools import reduce
num_list = [0, 1, 2, 3, 4, 5]

# Built in Functions:- Map
def triple(n):
    return n*3
double_list = map(lambda n:n*2, num_list)
triple_list = map(triple,num_list)
print(list(double_list))
print(list(triple_list))

# Built in Functions:- Filter
def moreThan2(elem):
    return elem>2
gt3 = filter(lambda n:n>3,num_list)
gt2 = filter(moreThan2, num_list)
print(list(gt3))
print(list(gt2))

# Built in Functions:- Reduce
avg = reduce(lambda a,b:(a+b), num_list)/len(num_list)
print(avg)