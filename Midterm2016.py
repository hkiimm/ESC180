# Midterm 2016 - ESC180 Midterm Prep

# Q1 - A
'''
Complete the following function. The function takes in a string thing, and returns the string "NOO!"
if thing is "ghost", "monster", or "midterm", and the string "YAY!" otherwise. For example, the call
halloween_reaction("ghost") should return the string "NOO!", and the call halloween_reaction("candy")
should return the string "YAY!".
'''
'''
def halloween_reaction(thing):
    if thing == "ghost" or thing == "monster" or thing == "midterm":
        return "NOO!"
    else:
        return "YAY!"

if __name__ == '__main__':
    print(halloween_reaction("ghost"))
'''
#Q1 - B
'''
Complete the following function. The function takes in a list L, and prints all the elements of the list L,
in order, except for the first element and the last element. One element should be printed per line. For
example,
    print_mid_part(["pumpkins", "candy", "costumes", "autumn", "zombies"])
should print

candy
costumes
autumn
'''
'''
def print_mid_part(L):
    for i in range (1, len(L)-1):
        print(L[i])

if __name__ == '__main__':
    print_mid_part(["pumpkins", "candy", "costumes", "autumn", "zombies"])
'''
#Q1 - C
'''
Complete the function h() so that the effect of running the code below is to print
    ["fall", "colours"]
(and nothing else).
'''
'''
def h(L):
    L[0] = "fall"
    L[1] = "colours"
    return L

if __name__ == "__main__":
    L = ["tricks", "treats"]
    h(L)
    print(L) #should print ["fall", "colours"]
'''
#Q1 - D
'''
What is the output of the following piece of code?
    x = "Spice"
    y = "Pumpkin"
    x += x
    print(y+x, "Latte")
'''
'''
# Output of the following piece of code should be 'PumpkinSpiceSpiceLatte'
def output():
    x = "Spice"
    y = "Pumpkin"
    x += x
    print(y+x, "Latte")

if __name__ == "__main__":
    output()
'''
#Q2 - A
'''
Complete the following function, which computes the sum of all the elements in the list L that are odd (i.e.,
not divisible by 2.) For example, if L is [1, 3, 4, 5], the function should return 9 since 9 = 1 + 3 + 5.
Assume L is a list of integers.
'''
'''
def odds_sum(L):
    """Return the sum of the odd elements of L"""
    sum = 0
    for i in range (len(L)):
        if L[i] % 2 != 0:
             sum += L[i]
    return sum

if __name__ == "__main__":
    L = [1, 3, 4, 5]
    print(odds_sum(L))
'''
#Q2 - B
'''
The following code is written using a for-loop. Write it using a while-loop instead.
    for i in range(5, 500, 3):
    print(i)
A version of the code above written using a while-loop:
'''
'''
def for_while():
    n = 0
    while n < 500:
        if 5 + n < 500:
            print(5+n)
        n += 3

if __name__ == "__main__":
    for_while()
'''
#Q3 - A
'''
Complete the following function. The function takes in a list of strings faves, and a list of string, of the
same length, kids. The favourite thing about Halloween of the kid whose name is kids[i] is faves[i].
The function returns the list of the names of the kids whose favourite thing about Halloween is "candy"
("candy" is in lowercase). The names in the list that the function returns should appear in the same order
that the names appear in the list kids. For example, if
    faves == ["candy", "costumes", "weather", "candy"] and
    kids == ["Bob", "Dorothy", "Mike", "Alice"],
then kids_who_like_candy(faves, kids) should return the list ["Bob", "Alice"].
'''
'''
def kids_who_like_candy(faves, kids):
    new_kids = []
    for i in range (len(faves)):
        if faves[i] == "candy":
            new_kids.append(kids[i])
    return new_kids

if __name__ == "__main__":
    faves = ["candy", "costumes", "weather", "candy"]
    kids = ["Bob", "Dorothy", "Mike", "Alice"]
    print(kids_who_like_candy(faves,kids))
'''
#Q3 - B
'''
Complete the following function. The function returns the cube root of n (i.e., √3 n.) Assume that √3 n
is an integer. You may not import any modules or use the ** operator.
'''
'''
def cube_root(n):
    for i in range (n):
        if i*i*i == n:
            return i
    return None

if __name__ == "__main__":
    print(cube_root(27))
    '''
#Q4
'''
Complete the following code in such a way that the output is as stated in the comments.
'''
'''
counter = 0

def halloween_surprise():
    global counter
    counter += 1
    if counter == 2:
        return 2
    elif counter == 3:
        return 1
    elif counter == 4:
        return "SURPRISE!"
    else:
        return 3

if __name__ == "__main__":
    print(halloween_surprise()) #Output: 3
    print(halloween_surprise()) #Output: 2
    print(halloween_surprise()) #Output: 1
    print(halloween_surprise()) #Output: SURPRISE!
'''
#Q5
'''
Each of these subquestions contains a piece of code. Treat each piece of code independently (i.e., code
in one question is not related to code in another), and write the expected output for each piece
of code. If the code produces an error, write down the output that the code prints before the error is
encountered, and then write “ERROR.” You do not have to specify what kind of error it is.
'''
#Q5 - A
'''
L1 = [1, 2]
L2 = L1[:]
L2 = [3, 4]
print(L1)

# Output: [1, 2]
# Reason --> The last thing that is assigned to L1 is [1, 2]
'''
#Q5 - B
'''
def f():
    n = 5

n = 4
n = f()
print(n)

# Output: None
# Reason --> The function doesn't return anything, which means it returns None
'''
#Q5 - C
'''
def f(L):
    L2 = L
    L = [1, 2]
    L[0] = 5
    print(L)

L = [2, 3]
f(L)
print(L[0])
print(L2)

# Output:
    [5, 2]
    5
    ERROR
# Reasoning: L is printed inside the function and modified to be [5, 2]. L[0] is 5. L2 gives an ERROR because it is a local variable.
'''
#Q5 - D
'''
L1 = [[[1, 2], 3], 4]
L2 = L1[:] # L2 = [L1[0], L1[1]]
L1[1] = 5
L1[0][1] = 5
L1[0][0][1] = 5
print(L2)

# Output: [[[1, 5], 5], 4]
# Reasoning: L2 is a shallow copy of L1 --> only one new list is created.
             L1 and L2 are not aliases, but L1[0] and L2[0] are, as are L1[0][0] and L1[0][0].
'''
#Q6
'''
Write a function that determines if a list has only a single “peak.” A list has a single peak if the list
is non-decreasing up to a certain point, and is non-increasing after that point. For example, the list
[1, 2, 2, 3, 4, 5, 0, -1] has a single “peak,” since it is non-decreasing up to 5, and non-increasing
after 5. On the other hand, the list [1, 2, 1, 2] has more than one “peak,” so we say that it is not
true that it has only a single “peak.” Non-decreasing lists like [1, 2, 3] and non-increasing lists like
[3, 2, 1] are considered to have a single “peak.”
'''
'''
def has_single_peak(L):
    """Return True iff the list of integers L has only a single peak"""
    peak = False
    for i in range (0, len(L)):
        if peak == False:
            if L[i] < L[i-1]:
                peak = True
        else:
            if L[i] > L[i-1]:
                return False
    return True

if __name__ == "__main__":
    print(has_single_peak([1, 2, 1, 2]))
'''
#Q7
'''
Write a function with the signature def max_arrivals_2hrs(arrivals) that returns the maximum number of arrivals of trick-or-treating kids that happened within the span of two hours, as recorded in the
list arrivals. The list arrivals is a list of times (in minutes) after 5PM on Oct. 31 that kids arrived
trick-or-treating. For example, if arrivals is [0, 30, 40, 150, 160, 170, 370], then kids arrived at
5:00PM, 5:30PM, 5:40PM, 7:30PM, 7:40PM, etc.; and the maximum number of arrivals within the span
of two hours was 3 (the arrivals at 5:00PM, 5:30PM, and 5:40PM.) You can assume that the list arrivals
contains only integers and is non-decreasing.
'''
'''
def max_arrivals_2hrs(arrivals):
    sum = 0
    for i in range (len(arrivals)):
        for j in range(len(arrivals)):
            if arrivals[j] - arrivals[i] < 120:
                sum = max(sum, j-i+1)
    return sum

if __name__ == "__main__":
    print(max_arrivals_2hrs([0, 30, 40, 150, 160, 170, 370]))
'''