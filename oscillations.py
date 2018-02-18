import numpy as np
import matplotlib.pyplot as plt
import random
from time import sleep

class Oscillators:
    def __init__(self):
        self.N = 20
        self.state = np.zeros(20)
        self.T = 100
        self.c = np.zeros(20)
        for x in range(20):
            self.c[x] = random.randint(0,self.T)

        self.k = 0.9
        print 'For values of c = ', self.c
        print 'and k = ',self.k
        #fig = plt.figure()
        #ax = plt.axes(xlim=(0, 20), ylim=(-1, 1))
        #plt.scatter(0,self.state[0])
        #plt.show()

    # def neighbour(self, n):
    #     temp = np.zeros(2)
    #     if n == 0:
    #         temp[0] = self.N - 1
    #         temp[1] = n + 1
    #         return temp
    #     elif n == (self.N - 1):
    #         temp[0] = n-1
    #         temp[1] = 0
    #         return temp
    #     else:
    #         temp[0] = n-1
    #         temp[1] = n+1
    #         return temp

    def fireflies(self):
        for i in range(20):
            #n = self.neighbour(i)
            if i == 0:
                l = self.N - 1
                r = i + 1
            elif i == (self.N - 1):
                l = i-1
                r = 0
            else:
                l = i-1
                r = i+1
            if self.state[l] == 1 or self.state[r] == 1:
                self.c[i] = self.c[i] * (1 + self.k)
            else:
                self.c[i] = self.c[i] + 1

            if self.c[i] >= self.T:
                self.state[i] = 1
                self.c[i] = 0
            else:
                self.state[i] = 0
            #plt.scatter(i,self.state[i])
        print(self.state)
        sleep(0.2)

def main():
    o = Oscillators()
    while True:
        o.fireflies()

if __name__ == "__main__":
        main()
