def a(ar= [1,4,4,4,5,3]):
    a=[0,0,0,0,0]
    for i in ar:
        a[i-1]+= 1
    return a.index(max(a))+ 1
