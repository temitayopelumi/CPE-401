import matplotlib.pyplot as plt


def main():
    A = [0] * 4
    B = [0] * 4
    Q = [0] * 4
    nB = [0] * 4

    print('Enter Dividend: ')
    for i in range(4):
        Q[i] = int(input('Enter bit'))
    print('Enter Divisor: ')
    for j in range(4):
        B[j] = int(input('Enter bit'))
    print('Dividend ', Q)
    print('Divisor ', B)
    # code of 2's complement of Divisor
    c = 1
    for i in range(3, -1, -1):
        nB[i], c = adds(xors(B[i], 1), 0, c)

    # main code start
    for cnt in range(4):
        # shift operation (left shift A, Q)
        A, Q = shifts(A, Q)
        C = 0
        # subtraction operation (A=A-B)
        for i in range(3, -1, -1):
            A[i], C = adds(A[i], nB[i], C)
        # check MSB of A
        if A[0] == 0:
            Q[3] = 1  # set LSB of Q
        else:
            Q[3] = 0  # set LSB of Q
            c = 0
            # addition operation (A = A + B)
            for i in range(3, -1, -1):
                A[i], C = adds(A[i], B[i], C)
    # Result Display
    print('Quotient: ', Q)
    print('Remainder: ', A)

    # Plotting Result
    plt.subplot(2, 2, 1)
    plt.plot(Q, 'y')
    plt.xlabel('Dividend')

    plt.subplot(2, 2, 2)
    plt.plot(B, 'b')
    plt.xlabel('Divisor')

    plt.subplot(2, 2, 3)
    plt.plot(Q, 'r')
    plt.xlabel('Quotient')

    plt.subplot(2, 2, 4)
    plt.plot(A, 'g')
    plt.xlabel('Remainder')

    # giving padding to subplots preventing the labels from being hidden
    plt.tight_layout()
    plt.show()


def ands(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def xors(a, b):
    if a != b:
        return 1
    else:
        return 0


def ors(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1


def adds(a, b, c):
    res = xors(xors(a, b), c)
    car = ors(ands(a, b), ands(xors(a, b), c))
    return res, car


def shifts(remainder, dividend):
    msb = dividend[0]
    for i in range(1, len(remainder)):
        temp = remainder[i]
        remainder[i - 1] = temp
    remainder[-1] = msb
    for i in range(1, len(dividend)):
        temp = dividend[i]
        dividend[i - 1] = temp
    dividend[-1] = 0
    return remainder, dividend


if __name__ == '__main__':
    main()
