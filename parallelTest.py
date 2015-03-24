from multiprocessing import Process, Value, Array

__author__ = 'adriana'
'''
Toying around with parallelization.
'''
from multiprocessing import Process, Value, Array

'''
def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]
'''
def addTen(n, a):
    for i in range(len(a)):
        a[i] += 10

def timesTwo(n, a):
    for i in range(len(a)):
        a[i] *= 2

def main():
    num = Value('d', 0.0)
    arr = Array('i', range(10), lock=False)

    p1 = Process(target=addTen, args=(num, arr))
    p1.start()
    p2 = Process(target=timesTwo, args=(num, arr))
    p2.start()
    p1.join()
    p2.join()

    print arr[:]
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1] - 2:
            print "HURRAY"

main()
