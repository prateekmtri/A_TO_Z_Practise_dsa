arr = list(map(int , input("Enter the value : ").split()))
n = len(arr)

sum = 0
for i in range(n):
    sum = sum + arr[i]
print(sum)    