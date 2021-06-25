def fib_recursive(n):
    if(n<=2):
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)

def fib_dynamic(n,memo={}):
    if n in memo:
        return memo[n]
    elif(n<=2):
        return 1
    else:
        memo[n]=fib_dynamic(n-1,memo)+fib_dynamic(n-2,memo)
        return memo[n]

n=int(input("Enter Number : "))
print(fib_dynamic(n))
