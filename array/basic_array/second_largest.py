# meta_seq: 1102:1 | 1104:0 | 1108:0 | 1122:0

arr = list(map(int , input("Enter the value : ").split()))
n = len(arr)

largest = arr[0]
second_larest = float('-inf')   # changed

for i in range(1, n):
    if largest < arr[i]:
        second_larest = largest 
        largest = arr[i]       
    elif arr[i] > second_larest and arr[i] != largest:
        second_larest = arr[i] 

if second_larest == float('-inf'):
    print("No second largest")
else:
    print(second_larest)        
        