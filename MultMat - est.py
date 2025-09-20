import sys
import numpy as np
import time

def mat_mult(A):
    init = time.perf_counter_ns()
    n = len(A)
    
    end = time.perf_counter_ns()
    print(f' Total time is: {(end - init)}')
    return 0
# end def

# Complejidad O(2^n)
def mult_chain(d, i, j):
    print(f'Calling {i},{j}')
    if i == j:
        return 0
    else:
        cost = float('inf')
        for k in range(i, j):
            cost_act = (mult_chain(d, i, k) +
                        mult_chain(d, k + 1, j) +
                        d[i - 1] * d[k] * d[j])
            if cost_act < cost:
                cost = cost_act
            # end if
        return cost
        # end for
    # end if
# end def

def memoizacion():
    # TODO: Implementar memoización
    pass
# end def

def bottom_up():
    # TODO: Implementar enfoque de abajo hacia arriba
    pass
# end def

def analisis_de_memoria():
    # TODO: Implementar análisis de memoria
    pass
# end def
## -------------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)
# end if

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][0:]

print(A)
print(mat_mult(A))

