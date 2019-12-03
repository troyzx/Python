import time

time.perf_counter()
start = time.time()
n=0
sum=0
for n in range(100000000):
    sum=sum+n
end = time.time()
elapse = end - start
print(elapse)