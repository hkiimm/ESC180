'''
# Problem 1

def list1_starts_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range (0, len(list2)):
            if not list1[i] == list2[i]:
                return False

        return True
    else:
        return False

if __name__ == '__main__':
    L1 = [1,2,33,5,7,9]
    L2 = [1,2,33]

    print(list1_starts_with_list2(L1,L2))
'''

'''
# Problem 2

def match_pattern(list1, list2):
    for i in range (0,len(list1)):
        if list1[i] == list2[0]:
            for j in range (0, len(list2)):
                if list1[i+j]==list2[j] and j == len(list2)-1:
                    return True

    return False

if __name__ == '__main__':
    L1 = [3,1,2,33,6,3]
    L2 = [1,2,33]

    print(match_pattern(L1, L2))
'''

'''
# Problem 3

def repeats(list0):
    for i in range (0, len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False


if __name__ == '__main__':
    L1 = [3,1,2,3,3,6,3]

    print(repeats(L1))
'''

'''
# Problem 4A

def print_matrix_dim(M):
    print (str(len(M))+"x"+str(len(M[0])))


if __name__ == '__main__':
    print_matrix_dim([[1,2],[3,4],[5,6]])
'''

'''
# Problem 4B
def mult_M_v(M, v):

    out=[]
    n = 0

    for i in range (len(M)):
        n = 0
        for j in range (len(M[i])):
            n += M[i][j]*v[j]
        out.append (n)

    return out


if __name__ == '__main__':
    matrix = [[1,4],[2,5],[3,6]]
    vect = [1,2]

    print (mult_M_v(matrix,vect))
'''

'''
# Problem 4C
def matrix_mult(M1,M2):
    u = [0]*len(M1) #rows of m1
    v = [u]*len(M2[0]) #column of m2; creates a 2d list with the proper dimensions
    for i in range(len(M1)): #goes through rows of m1
        for j in range(len(M2[0])): #goes through columns of m2
            n = 0
            for k in range(len(M1[0])): #goes through column of m1
                n += M1[i][k]*M2[k][j]
            v[i][j] = n
    return(v)


if __name__ == '__main__':
    matrix1 = [[1,0],[0,1]]
    matrix2 = [[1,0],[0,1]]

    print (matrix_mult(matrix1,matrix2))
'''