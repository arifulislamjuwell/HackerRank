def a(ar= [1,3,2,6,1,2]):
    a=[[c,d] for a,c in enumerate(ar) for b,d in enumerate(ar) if a<b and (c+d)%3 ==0 ]
    return a
print(a())