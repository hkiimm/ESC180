import math
pi = math.pi

"""
# Problem 1
def count_evens(L):
    evens = 0
    for num in L:
        evens += (num + 1)%2

    return evens

if __name__ == '__main__':
    L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print(count_evens(L))



# Problem 2
def list_to_str(lis):
    word = ""
    for num in lis:
        word += str(num) + " "
    return word

if __name__ == '__main__':
    lis = [1, 2, 3, 4, 5]
    print(list_to_str(lis))



# Problem 3
def lists_are_the_same(list1, list2):
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                pass
            else:
                return False
                #break
        return True
    else:
        return False

if __name__ == '__main__':
    lis1 = [1, 2, 3, 4, 5]
    lis2 = [1, 2, 3, 4, 5]
    print(lists_are_the_same(lis1, lis2))



# Problem 4

def simplify_fraction(n, m):
    for i in range(n):
        if n % (n-i) == 0 and m % (n-i) == 0:
            n1 = n/(n-i)
            m1 = m/(n-i)
            break
    print(int(n1), "/", int(m1))

if __name__ == '__main__':
    simplify_fraction(16, 8)



# Problem 5

done = [0]

def leibniz(n):
    if len(done) < n+1:
        done.append(done[n-1] + ((-1)**(n-1))/(2*(n-1) + 1))
    return done[n] * 4

def num_sigdig(sd):
    n = 0
    right = (10 ** (sd-1))
    compare = int(pi * right)
    while int(leibniz(n)*right) != compare:
        #print(int(leibniz(n)*right), compare)
        n += 1
    return n-1

if __name__ == '__main__':
    print(num_sigdig(3))

"""

# Problem 6

def euclids_algorithm(a,b):
    while a != 0:
        c = a
        a = b%a
        b = c
    return b

if __name__ == '__main__':
    a = 219
    b = 360
    c = euclids_algorithm(a, b)
    a /= c
    b /= c
    print (int(a), "/", int(b))












