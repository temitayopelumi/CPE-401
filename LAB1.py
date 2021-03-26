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

def Adder():
    a = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    c = [0, 0, 0, 0]
    for i in range (0, 4):
        a_bit = int (input ('Enter First Binary Sequence'))
        a[i] = a_bit
    for i in range (0, 4):
        b_bit = int (input ('Enter Second Binary Sequence '))
        b[i] = b_bit
    carry = 0
    for i in range (3, -1, -1):
        c[i] = L_xor (L_xor (a[i], b[i], ), carry)
        carry = L_or (L_and (a[i], b[i]), L_and (L_xor (a[i], b[i]), carry))
    return carry, c


if __name__ == '__main__':
    k = Adder ()
    print ('_________________________')
    print (k)
