import numpy as np
import copy


'''# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)

#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]'''

## Problem 1

def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

## Problem 2
def get_lead_ind(row):

    for i in range (len(row)):
        if row[i] != 0:
            return i

    return len(row)

## Problem 3
def get_row_to_swap(M, start_i):
    # out[0] is index of leading non-zero coeff that wasf ound, out[1] is index of that row
    out = [len(M[0]),0]

    for i in range (start_i, len(M)):
        for j in range (start_i, len(M[0])):
            if M[i][j] != 0:
                if j < out[0]:
                    out[0] = j
                    out [1] = i
                    break

    return out [1]

## Problem 4
def add_rows_coefs(r1, c1, r2, c2) :
    out =  [0]*len(r1)

    for i in range (len(out)):
        out[i] = c1*r1[i]+c2*r2[i]

    return out

## Problem 5
def eliminate(M, row_to_sub, best_lead_ind, b):


    for i in range (row_to_sub+1, len(M)):
        if M[row_to_sub][best_lead_ind] != 0:
            c1 = -(M[i][best_lead_ind]/M[row_to_sub][best_lead_ind])

            for j in range (len(M[0])):
                M[i][j] = add_rows_coefs (M[row_to_sub], c1, M[i], 1)[j]

            b [i] = c1*b[row_to_sub]+b[i]

## Problem 6
def forward_step(M, b):
    print ("Performing forward step")
    for i in range (len(M)):

        print ("The matrix is currently: ")
        print_matrix(M)

        print ("Now looking at row", i)
        print ("Swapping rows", i, "and", get_row_to_swap(M, i))

        ind = get_row_to_swap(M, i)
        for j in range (len(M[0])):
            M[i][j], M[ind][j] = M[ind][j], M[i][j]
            b[i], b[ind] = b[ind], b[i]



        print ("The matrix is currently: ")
        print_matrix(M)

        ind2 = get_lead_ind(M[i])
        eliminate(M, i, ind2, b)
        print ("Adding row", i, "to rows below it to eliminate coefficients in column", i)

## Problem 7
def eliminate_backwards(M, row_to_sub, best_lead_ind, b):


    for i in range (row_to_sub-1, -1, -1):
        if M[row_to_sub][best_lead_ind] != 0:
            c1 = -(M[i][best_lead_ind]/M[row_to_sub][best_lead_ind])

            for j in range (len(M[0])):
                M[i][j] = add_rows_coefs (M[row_to_sub], c1, M[i], 1)[j]

            b[i]=c1*b[row_to_sub]+b[i]

def backward_step(M, b):
    forward_step(M, b)
    print ("Performing backward step-----------------------------------------------")

    for i in range (len(M)-1,-1, -1):

        print ("The matrix is currently: ")
        print_matrix(M)
        print (b)

        ind2 = get_lead_ind(M[i])
        eliminate_backwards(M, i, ind2, b)
        print ("Adding row", i, "to rows above it to eliminate coefficients in column", i)

    print ("Now dividing each row by the leading coefficient")
    for i in range (len(M)):
        ind3 = get_lead_ind(M[i])
        divisor = M[i][ind3]
        print (divisor)

        for j in range (ind3, len(M[0])):
            M[i][j] = M[i][j]/divisor

        b[i] = b[i]/divisor

    print ("The matrix is currently: ")
    print_matrix(M)
    print(b)


## Problem 8
def solve(M, b):
    backward_step(M,b)
    # just doing this gives solution if the matrix RNF is identity matrix

    M = np.array(M)
    B = np.array(b)

    X = np.linalg.solve(M,B) # using numpy to solve it properly

    print (X)


if __name__ == "__main__":
    M = [[0,-2,4],[3,4,1],[1,7,3]]
    x = [5,6,5]

    b = (np.matmul(M,x)).tolist()

    solve(M,b)