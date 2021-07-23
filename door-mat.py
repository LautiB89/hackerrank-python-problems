inp = list(map(int, input().split()))
n,m = inp[0],inp[1]
p = ".|."
for i in range(1,n+1):
    q = n-abs(2*i-n-1)
    if q==n:print("WELCOME".center(m,"-"))
    else: print((q*p).center(m,"-"))
