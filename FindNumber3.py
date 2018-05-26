import math

lis = [2, 34, 46, 57, 68, 69, 70, 89, 500, 5000]

temporaryList = lis[:3]
temporaryList2 = lis[4:]
high = len(lis) - 1
low = 0

print(lis)

 
num = int(input('Please enter a number '))
middle = math.floor((low+high) / 2)

not_found = True

    
while not_found:
    middle = math.floor((low+high) / 2)
    if num == lis[middle]:
        print(lis.index(num))
        not_found = False
    elif num > lis[middle]:
        low = middle + 1
        num_in_list = True
        continue
    elif num < lis[middle]:
        high = middle - 1
        num_in_list = True
        continue
    else:
        print('Number is not in the list')
        not_found = False

        
    


