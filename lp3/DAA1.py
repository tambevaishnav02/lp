def fibo_itrative(n:int):
    if n==1:
        return 0
    elif n==2:
        return 1
    else :
        dp=[0]*n
        dp[0]=0
        dp[1]=1
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]
def fibo_rec(n):
    cache={1:0,2:1}
    return helper(n,cache)
def helper(n:int,cache):
    if n in cache:
        return cache[n]
    else:
        cache[n]=helper(n-1,cache)+helper(n-2,cache)
        return cache[n]
n=int(input("enter nTH fibonaci number "))
print(f"fibonaci number by non recursive ittrative{fibo_itrative(n)}")

print(f"fibonaci number by recursive {fibo_rec(n)}")