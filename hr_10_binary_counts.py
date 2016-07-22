# A solution to refactor

n = int(input().strip())
binary_str = (bin(n))[2:]
print(binary_str)
ones = binary_str.split("0")
print(len(max(ones)))