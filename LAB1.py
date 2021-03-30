# Program to add two unsigned binary number [4 bit binary adder]

# Helper Functions

# And function
def L_and(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


# Or function
def L_or(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1


# xor function
def L_xor(a, b):
    if a != b:
        return 1
    else:
        return 0


# Adder

def Adder(a, b):
    c = [0, 0, 0, 0]
    if (len(a) and len(b)) <= 4:
        carry = 0
        for i in range (3, -1, -1):
            c[i] = L_xor (L_xor (int(a[i]), int(b[i]), ), carry)
            carry = L_or (L_and (int(a[i]), int(b[i])), L_and (L_xor (int(a[i]), int(b[i])), carry))
        return carry, c
    else:
        return 'Bits greater than 4'

#main code
if __name__ == '__main__':
    f=str(input('Enter First Binary Sequence '))
    s=str(input('Enter Second Binary Seuence '))
    a=list(str(f))
    b=list(str(s))
    k = Adder (a, b)
    print('The sum is of')
    print(f)
    print('+')
    print(s)
    print ('===========================')
    print (k)
