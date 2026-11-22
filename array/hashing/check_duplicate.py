arr = list(map(int , input("Enter the value ").split()))
n = len(arr)

hash_list = {}

duplicate = False
for i in arr:
    if i in hash_list:
        duplicate = True
        break  
    else:
        hash_list[i] = 1 
print(duplicate)        