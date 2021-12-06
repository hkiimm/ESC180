## Problem 1
def power (x, n):
    n = n-1
    if n == 0:
        return x
    return x*power (x,n)

## Problem 2
def interleave (L1, L2):

    if len(L1) == 1:
        return [L1[0],L2[0]]

    return [L1[0],L2[0]]+interleave (L1[1:],L2[1:])


## Problem 3
def reverse_rec(L):

    if len(L) == 1:
        return [L[0]]

    return [L[len(L)-1]] + reverse_rec(L[:len(L)-1])

## Problem 4
def zigzag1(L):
    if len(L) == 0:
        return []
    elif len(L) == 1:
        return [L[0]]
    else:
        return [L[len(L)//2], L[len(L)//2-1]] + zigzag1(L[:len(L)//2-1]+L[len(L)//2+1:])

## Problem 5
def is_balanced(s):
    if "(" not in s and ")" not in s:
        return True
    elif "(" not in s or ")" not in s or s.find("(") > s.rfind (")"):
        return False

    return is_balanced(s[: s.find("(")]+s[s.find("(")+1:s.find(")")]+s[s.find(")")+1:])


if __name__ == "__main__":
    #print (power(2,5))
    #print (interleave([1,2],[3,4]))
    #print (reverse_rec([1,2,3,4,5]))
    #print (zigzag1([3,6,9,12,15]))
    print (is_balanced("(()(()))"))
