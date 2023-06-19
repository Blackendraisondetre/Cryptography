from sympy.logic.boolalg import ANFform, anf_coeffs
from sympy import symbols
from sympy import Matrix

x, y, z, j = symbols('x_1 x_2 x_3 x_4')
seq = [0,0,1,1,1,1,0,1]
#seq = [1,0,0,1,0,0,1,1]
#seq = [0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1]
#seq = [0,1,1,1,0,1,1,1]

def def_1(n):
    [print(f'Обсяги булевих функцій при x = {x}, буде = {2**(2**x)}') for x in range (n)]

def def_2(seq):
    ans = (str(ANFform([x,y,z], seq)))
    print(f'Представлення у вигляді поліному: {ans}')
    print(f'Таблиця коефіцієнтів: {anf_coeffs(seq)}')

def def_3(seq):
    M = Matrix([[1,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[1,1,1,1,0,0,0,0],[1,0,0,0,1,0,0,0],[1,1,0,0,1,1,0,0],[1,0,1,0,1,0,1,0],[1,1,1,1,1,1,1,1]])
    N = Matrix(seq)
    amogus = [0 if not(x%2) else 1 for x in list(M*N)]
    print(f'Таблиця коефіцієнтів: {amogus}')

def_2(seq)
#def_3(seq)

#def_1(8)