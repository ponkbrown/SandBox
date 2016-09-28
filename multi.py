import os
from multiprocessing import Process

def doubler(number):
    '''
    Una funcion de dobles que puede usar por un proceso
    '''
    result = number * 2
    proc = os.getpid()
    print('{0} doblado a {1} por el proceso [id: {2}]'.format(
        number, result, proc))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(numbers,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
