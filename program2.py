s = input("Enter string: ")

seen = {}
left = 0
ans = 0

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1

    seen[s[right]] = right
    ans = max(ans, right - left + 1)

print("Length:", ans)