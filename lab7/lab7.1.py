from time import time
def summation(n):
    t1 = 0
    for i in range(0, n):
        t1 += i
    return t1

def summation2(n):
    t1 = (n/2)*(n+1)
    return t1

def analyze_algo(n=1):
    stime = time()
    summation(n)
    etime = time()
    elapsed = etime - stime
    print("excution time: ", elapsed)

analyze_algo(100)
analyze_algo(10000)
analyze_algo(1000000)
analyze_algo(100000000)
analyze_algo(1_000_000_000)
