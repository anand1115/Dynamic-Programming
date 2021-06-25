def get_ways(m,n):
    if(m==1 and n==1):
        return 1
    if(m==0 or n==0):
        return 0
    return get_ways(m-1,n)+get_ways(m,n-1)
def get_ways_dynamic(m,n,memo={}):
    key=str(m)+","+str(n)
    if key in memo:
        return memo[key]
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    memo[key]=get_ways_dynamic(m-1,n)+get_ways_dynamic(m,n-1)
    return memo[key]
m,n=list(map(int,input().split()))
print(get_ways_dynamic(m,n))
