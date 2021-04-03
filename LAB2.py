from  LAB1 import L_xor, Adder
import matplotlib.pyplot as plt

a=[0,0,0,0]
b=[1,0,0,0]
print('Enter First number sequence')
for i in range(4):
    a[i]=int(input())
print('Enter Second number sequence')
for i in range(4):
    b[i] = int(input())
for i in range(4):
    b[i]=L_xor(1,b[i])

k= Adder(a,b,carry=1)
c=k[0]
s=k[1]

if  c == 0:
    for i in range(4):
        s[i] = L_xor(1, s[i])
    car = 1
    ans = Adder(s, [0,0,0,0], car)
    c=ans[0]
    s=ans[1]
    print('-')
    print(s)
else:
    #   display('Positive')
    print('+')
    print(s)


plt.subplot(311)
plt.plot(a, 'r')
plt.xlabel('First Sequence')
plt.subplot(312)
plt.plot(b, 'g')
plt.xlabel('Second Sequence')
plt.subplot(313)
plt.plot(s, 'b')
plt.xlabel('Result(a-b)')
plt.show()

