
def a(a):
    res=[]
    for i in a:
        if i < 38 or i % 5 == 0 or i % 5 <= 2:
            res.append(i)
        else:
            res.append(((i//5)+1)* 5)
    return res

print(a([73,68,38,33,99]))