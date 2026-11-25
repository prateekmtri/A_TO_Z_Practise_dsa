arr = list(map(int, input("Enter the value : ").split()))
n = len(arr)

list_dict = {}
for i in arr:
    if i in list_dict:
        list_dict[i] +=1
    else:
        list_dict[i] = 1 
for key , value in list_dict.items():
    if value > n/2:
        print(key)          