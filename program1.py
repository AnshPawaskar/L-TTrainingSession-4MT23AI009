nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

arr = sorted(freq.items(), key=lambda x: x[1], reverse=True)

result = []

for i in range(k):
    result.append(arr[i][0])

print(result)