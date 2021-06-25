def can_make_sum(target,elements):
    if(target==0):
        return True
    elif(target<0):
        return False
    else:
        for i in elements:
            rem=target-i
            if(can_make_sum(rem,elements)):
                return True
    return False
def can_make_sum_dynamic(target,elements,memo={}):
    if target in memo:
        return memo[target]
    if(target==0):
        return True
    elif(target<0):
        return False
    else:
        for i in elements:
            rem=can_make_sum_dynamic(target-i,elements,memo)
            if rem:
                memo[rem]=rem
                return True
    memo[target]=False
    return False               
        

print(can_make_sum(200,[1,1]))
