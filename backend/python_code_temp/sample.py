start = 13
end = 25


for i in range (start, end):
    if i > 1:
        for j in range(2, i):
            if (j%2 == 0):
                # print("Not prime")
                break
            else:
                print(j, "prime")








