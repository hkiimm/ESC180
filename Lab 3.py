# Problem 2: Sums of Cubes
def checksum(num):
    global output

    for i in range (1,num+1):
        output += i**3

def check_sums_up_to_n (num2):
    formula = ((num2**2)*((num2+1)**2))/4

    if formula==output:
        return True
    else:
        return False


if __name__ == "__main__":
    n = 2
    output = 0
    checksum(2)
    checksum(3)
    print (check_sums_up_to_n(n))

# Problem 3: pi
approx=0

for i in range (0, 1001):
    approx += ((-1)**i )/ (2*i+1)

print (approx)