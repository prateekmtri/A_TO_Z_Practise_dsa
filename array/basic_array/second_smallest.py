# meta_seq: 1102:1 | 1104:0 | 1108:0 | 1122:0

arr = list(map(int, input().split()))

smallest = float('inf')
second_smallest = float('inf')

for i in arr:
    if i < smallest:
        second_smallest = smallest
        smallest = i

    elif i < second_smallest and i != smallest:
        second_smallest = i

if second_smallest == float('inf'):
    print("Second smallest does not exist")
else:
    print(second_smallest)