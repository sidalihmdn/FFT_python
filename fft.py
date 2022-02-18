#this is an implementation of the FFT (fast fourier transform) in python from scratch
from cmath import exp, pi, sin
import matplotlib.pyplot as plt

def fft(input):



    #seperate the input vector into even and odd indexes
    input_odd = input[1::2]
    input_even = input[0::2]
    
    #length of the input vector
    N = len(input)
    #print(N)
    if N == 1 :
        return input
    output = [0 for i in range(N)]

    #recursive implementation 
    output_odd = fft(input_odd)
    output_even = fft(input_even)


    w = W_coef(N) #calculate the omega coeffecient 
    for i in range(N//2):
        output[i] = output_even[i] + (w**i)*output_odd[i]
        output[i + N//2] = output_even[i] - (w**i)*output_odd[i]
    
    return output


def W_coef(N):
    return exp(-1j*(2*pi)/N)


#the number of element must be a power of to in order for the algorithm to work
x = [ i*0.01 for i in range(1024)]
y = [sin(i) for i in x]

Y = fft(y)

plt.plot(Y) 
plt.show()