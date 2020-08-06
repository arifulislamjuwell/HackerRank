def Brecord(s, d, m):
    tp = (len(s)-m) + 1 #total number of pieces possible
    pr
    return len([1 for i in range(tp) if sum(s[i:i+m])==d])


print(Brecord([1, 2, 1, 3, 2], 3, 2))