def Brecord(a):
    h_sc= l_sc= 0
    highest_score= lowest_score= a[0]
    for i in a:
        if i > highest_score:
            highest_score= i
            h_sc+= 1
        if i < lowest_score:
            lowest_score= i
            l_sc+= 1
    return h_sc, l_sc


print(Brecord([10,5, 20, 20, 4, 5, 2, 25, 1]))