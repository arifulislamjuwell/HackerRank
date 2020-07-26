def a(alice , bob):
    score=[0,0]
    for a, b in zip(alice, bob):
        score[0] += a > b
        score[1] += a < b
    return score
print(a([3,1,78], [6,2,100]))
