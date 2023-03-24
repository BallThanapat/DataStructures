from time import time
import random
def isIntersect(a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i==j and i==k:
                    return True
    return False
    # for i in a:
    #     if i in b and i in c:
    #         return True
    # return False

def isIntersect2(a, b, c):
    for i in a:
        for j in b:
            if i == j in i in c:
                return True
    return False

def randomList(n):
    a = [i for i in range(n)]
    b = [i for i in range(n, 2*n)]
    c = [i for i in range(2*n, 3*n)]
    return a, b, c

def analyze_algo(n=1):
    a, b, c = randomList(n)
    stime = time()
    print(isIntersect2(a,b,c))
    etime = time()
    elapsed = etime - stime
    print("excution time: ", float(elapsed))
  
# analyze_algo(100)
# analyze_algo(1000)
analyze_algo(10000)
# analyze_algo(1000000)

