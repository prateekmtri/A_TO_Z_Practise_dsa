arr = list(map(int , input("Enter the value : ").split()))
n = len(arr)

initial_value = arr[0]

for i in range(n):
    if arr[i]!= initial_value:
        print(initial_value)
        
    initial_value = initial_value + 1    