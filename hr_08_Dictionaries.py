# Given N Names and phone numbers
# map names to phone numbers

# N = int(input().strip()) # number of entries in phonebook


N = int(input())
name = []
phoneBook = {}

for i in range(N):
    name, phone = input().strip().split(' ')
    phoneBook[name] = phone

for i in range(N):
    name = input()
    if name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print("Not found")

'''
#takes one input per line, name then phone
N = int(input())
name = []
phone = {}

for i in range(N):
    #name.append(input().strip())
    name = input().strip()
    phone[name] = input().strip()

phoneBook = phone

# for k,v in phoneBook.items():
#     print(k,v)
# else:
#     print("Not Found")

for i in range(N):
    if name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print("Not found")
'''