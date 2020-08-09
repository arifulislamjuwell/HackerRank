def a(ar= [1,3,2,6,1,2]):
    print(enumerate(ar))
    res= 0
    count=0
    for i in ar:
        for j in range(count+1, 6):
            res+= 1 if ((i + ar[j]) % 3) == 0 else 0
        count+=1
    return res

print(a())