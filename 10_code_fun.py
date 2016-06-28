# infinite loop
count = 0
while True:
    if count > 20:
        for i in ["/","-","|","\\","|"]:
            print("%s\r" % i,)
            count += count
            print(count)
