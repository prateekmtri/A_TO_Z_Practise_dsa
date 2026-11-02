# meta_seq: 1102:1 | 1104:0 | 1108:0 | 1122:0

arr = list(map(int, input("Enter the value : ").split()))
n = len(arr)
largest_number = arr[0]

for i in range(1, n):
    if largest_number < arr[i]:
        largest_number = arr[i]
        
        
print(largest_number)