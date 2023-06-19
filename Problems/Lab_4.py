import math
from sympy import Matrix
from itertools import product
import matplotlib.pyplot as plt
from scipy.linalg import hadamard

def zeroes(length: int) -> list:
    return [0 for x in range (length)]
def combinator3000(order:int, length: int) -> list:
    nanomachines = []
    for x in range (2**length):
        son = [i for i in '{0:0{again}b}'.format(x,again = length)]
        if son.count('1') == order:
            nanomachines.append(''.join(son))
    #print(nanomachines)
    return nanomachines
def SAC(seq:list, order:int) -> bool:

    print(seq)
    amogus = []

    # Forming dictionaries of truth table
    pool = combinator3000(order, round(math.log(len(seq), 2)))
    for x in range (round(math.log(len(seq),2))+1):
        dick = {}
        for y in range(len(seq)):
            help_me = [i for i in '{0:0{again}b}'.format(y,again = round(math.log(len(seq),2)))]
            if x != round(math.log(len(seq),2)):
                help_me = [str(l) for l in [(ord(a) ^ ord(b)) for a, b in zip(help_me, pool[x])]]
            help_me = ''.join(help_me)
            dick[help_me] = seq[int(help_me,2)]
        amogus.append(dick)

    # Evalutating the table to consider SAF
    doppelganger= []
    for z in reversed(amogus):
        print(z)
        doppelganger.append(list(z.values()))
    ans = zeroes(round(math.log(len(seq),2)))
    for j in range(len(seq)):
        for k in range(len(ans)):
            ans[k] += doppelganger[0][j]^doppelganger[k+1][j]
    print(ans)
    for x in range(round(math.log(len(seq),2))):
        if ans[x] == len(seq)/2:
            print(f'The bool function №{x+1} passed the vibe check')
            pass
        else:
            print(f'The bool function №{x + 1} failed the vibe check')
            return False
    return True
def hist_sac():
    results = []
    # Iterate through all possible Boolean functions of length 16
    # Build a histogram
    histogram = {1: 0, 2: 0, 3: 0}
    for bool_func in product([0, 1], repeat=16):
        print(bool_func)

        for abobus in range(1,4):
            res = SAC(list(bool_func),abobus)
            if res:
                histogram[abobus] += 1
        # Collecting the results

    print(histogram)

    # Plot the histogram
    x = histogram.keys()
    y = histogram.values()
    plt.bar(x, y)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.show()
def adamar(seq:list) -> int:
    # Forming matrices
    N = Matrix([-1 if x==1 else 1 for x in seq])
    M = Matrix(hadamard(len(seq)))
    #M = Matrix([[1, 1, 1, 1, 1, 1, 1, 1], [1, -1, 1, -1, 1, -1, 1, -1], [1, 1, -1, -1, 1, 1, -1, -1],[1, -1, -1, 1, 1, -1, -1, 1], [1, 1, 1, 1, -1, -1, -1, -1], [1, -1, 1, -1, -1, 1, -1, 1],[1, 1, -1, -1, -1, -1, 1, 1], [1, -1, -1, 1, -1, 1, 1, -1]])
    amogus = list(M*N)
    print(f'Таблиця коефіцієнтів: {amogus}')
    ans = 0

    coef = []
    numbers = []

    # Lexicographic format
    for x in range(len(amogus)):
         strings = ''.join([i for i in '{0:0{again}b}'.format(x, again=round(math.log(len(seq),2)))])
         coef.append(strings)
         numbers.append(strings.count('1'))

    print(coef)
    print(numbers)

    # Evaluating level of m
    for x in range(1,round(math.log(len(seq),2))+1):
        indices = [i for i, j in enumerate(numbers) if j == x]
        print(indices)
        for y in indices:
            if amogus[y] != 0:
                print(f'm = {x-1} ')
                return x-1
def hist_adam():
    results = []

    # Iterate through all possible Boolean functions of length 16
    for bool_func in product([0, 1], repeat=16):
        print(bool_func)
        # Performing the evaluation
        res = adamar(list(bool_func))
        print(res)
        if res is None:
            res = 4
        # Collecting the results
        results.append(res)

    # Build a histogram
    histogram = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0}

    for result in results:
        histogram[result] += 1

    print(histogram)

    # Plot the histogram
    x = histogram.keys()
    y = histogram.values()
    plt.bar(x, y)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.show()

#adamar([0, 0, 1, 0, 0, 1, 1, 1])
#adamar([0, 1, 1, 1, 1, 0, 1, 1,0,1,0,0,1,1,1,0])
#combinator3000(3,4)
#SAC([0,0,1,0,0,1,1,1],1)
#SAC([0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0],1)
#hist_sac()
#hist_adam()