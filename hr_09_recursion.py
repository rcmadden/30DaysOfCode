# Write a factorial function that takes a positive integer N,  as a parameter and prints the result of N! (N factorial).
# N = int(input().strip())
# if 2 <= N <= 12:
#     N == N
# else:
#     print("N not in range")
#
# #iterative
# def factorial(N):
#     product = 1
#     for i in range(N):
#         product = product * (i+1)
#     return product
#
# print(factorial(N))

#recursive
N = int(input().strip())
if 2<= N <= 12:
    N == N
else:
    print("N not in range")

def factorial(N):
    if N <= 1:
        return(1)
    else:
        return(N * factorial(N-1))
print(factorial(N))