# meta_seq: 1102:1 | 1104:0 | 1108:0 | 1122:0

arr = list(map(int,input("Enter the value : ").split()))
n = len(arr)

smallest_number = arr[0]
for i in range(1 , n):
    if smallest_number > arr[i]:
        smallest_number = arr[i]
        
print(smallest_number)        
        
        