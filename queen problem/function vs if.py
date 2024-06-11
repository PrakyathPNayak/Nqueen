import time

s1 = time.time()
def function(a, b):
    return a*(a>b) + b * (b>a)
print(function(10, 20), time.time()-s1)
s2 = time.time()

