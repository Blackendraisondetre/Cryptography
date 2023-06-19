import numpy
from sympy.logic.boolalg import anf_coeffs
import math
import sys, os
from Lab_4 import SAC,adamar
from Lab_3 import Hemming
from sympy import Matrix
from scipy.linalg import hadamard

def blockPrint():
    sys.stdout = open(os.devnull, 'w')
# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
def print_list_data(lst:list,shift:int)->list:
    dec_ans = []
    print("{:<10s}{:<40s}{:<15s}{:<15s}".format("θ", "polynom", "bin", "decimal"))
    print("-" * 75)
    for i, sublist in enumerate(lst):
        theta = '\u03B8'
        polynom = ' + '.join([f'{sublist[j]}*x^{len(sublist)-j-1}' for j in range(len(sublist)) if sublist[j] != 0])
        bin_str = ''.join(map(str, sublist))
        decimal = sum([sublist[j] * (2**(len(sublist)-j-1)) for j in range(len(sublist))])
        dec_ans.append(decimal)
        print("{:<10d}{:<40s}{:<15s}{:<15d}".format(i + shift, polynom, bin_str, decimal))
    print("-" * 75)
    return dec_ans
def zeroes(length: int) -> list:
    return [0 for x in range (length)]
def fill_me_senpai(poly:list,length:int) -> list:
    if (len(poly) != length):
        [poly.append(0) for x in range(length-len(poly))]
    reversed_poly = poly[::-1]
    return reversed_poly
def clean(poly:list,length:int)->list:
    pivo = zeroes(length)
    poly = fill_me_senpai(poly,length)
    for x in range (length):
        pivo[x] = int(abs(poly[x]%2))
    return pivo
def gen_field(poly:list, theta:int,order:int) -> list:
    amogus = []
    for x in range(theta,order+theta):
        pivo = zeroes(x)
        pivo.append(1)
        qx, rx = numpy.polynomial.polynomial.polydiv(pivo, poly)
        ans = clean(list(rx),4)
        amogus.append(ans)

    seq = print_list_data(amogus,theta)
    seq.insert(0,0)
    print(f'Q-sequence = {seq}')
    print("-" * 75)
    return seq
def decompose_s_block(s_block:list)->list:
    sub_functions = []
    num_subfunctions = len(bin(max(s_block))) - 2

    for i in range(num_subfunctions):
        sub_func = [(s >> (num_subfunctions - i - 1)) & 1 for s in s_block]
        sub_functions.append(sub_func)

    for i, sub_func in enumerate(sub_functions, 1):
        print(f'F_{i}: {sub_func}')
    print("-" * 75)


    return sub_functions
def det_trans_type(s_block):
    print("-" * 75)
    n = len(s_block)
    for x in range(n):
        for y in range(n):
            fx = s_block[x]
            fy = s_block[y]
            fxy = s_block[x ^ y]  # XOR operation
            fx_xor_fy = fx ^ fy

            if fxy != fx_xor_fy:
                print(f"The S-block represents a Nonlinear transformation.")
                print("-" * 75)
                return 0

    print(f"The S-block represents a Linear transformation.")
    print("-" * 75)
    return 0
def deg(seq:list) -> int:
    odds_table = anf_coeffs(seq)

    ans = 0
    coef = []
    numbers = []

    for x in range(len(odds_table)):
        strings = ''.join([i for i in '{0:0{again}b}'.format(x, again=round(math.log(len(seq), 2)))])
        coef.append(strings)
        numbers.append(strings.count('1'))

    for x in range(1, round(math.log(len(seq), 2)) + 1):
        indices = [i for i, j in enumerate(numbers) if j == x]
        for y in indices:
            if odds_table[y] != 0:
                ans = x
    return ans
def first_list_of_checks(seq:list)->None:
    deg_ans = []
    dist_ans = []
    sac_ans = []
    imm_ans = []

    blockPrint()
    for x in seq:
        #1 Deg
        deg_ans.append(deg(x))
        #2 Non linear
        dist_ans.append(Hemming(x))
        #3 Strict avalanche
        sac_ans.append(SAC(x,1))
        #4 Immunity
        imm_ans.append(adamar(x))
    enablePrint()

    print(f'The deg of an S block is = {min(deg_ans)}')
    print(f'The nonlinear distance of an S block is = {min(dist_ans)}')
    print(f'Meeting a strict avalanche criterion of an S block is = {any(sac_ans)}')
    print(f'The correlational immunity of an S block is = {min(imm_ans)}')

def vibe_check(lists):
    first_list = lists[0]
    return all(lst == first_list for lst in lists[1:])

def lin_red(seq:list):
    N = Matrix([-1 if x == 1 else 1 for x in seq])
    M = Matrix(hadamard(len(seq)))
    amogus = list(M * N)
    print(amogus)
    return amogus



def second_list_of_checks(seq:list):
    #TODO
    lin_red_ans = []
    for x in seq:
        lin_red_ans.append(lin_red(x))


    #print(f'The high criterion of the absence of linear redundancy is {not vibe_check(lin_red_ans)}')

seq = gen_field([1,1,0,0,1],5,15)
F = decompose_s_block(seq)
det_trans_type(seq)
first_list_of_checks(F)
second_list_of_checks(F)
