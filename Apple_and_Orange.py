#!/bin/python3
def countApplesAndOranges(apples,oranges, s= 7, t= 11, a= 5, b=15):
    app= 0
    oran=0 
    for apple in apples:
        dis= apple+ a
        if dis in range(s, t+1):
            app+= 1

    for orange in oranges:
        dis= orange+ b
        if dis in range(s, t+1):
            oran+= 1
    print(app)
    print(oran)

if __name__ == '__main__':
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(apples, oranges)
