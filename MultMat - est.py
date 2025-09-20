import sys
import numpy as np
import time

def mat_mult(A):
    n = len(A)
    # Tiempos del algoritmo recursivo 
    init_rec = time.perf_counter_ns()
    cost_rec = mult_chain(A, 1, n - 1)
    end_rec = time.perf_counter_ns()

    # Tiempos del algoritmo memoizado
    init_memo = time.perf_counter_ns()
    cost_memo = memoizacion(A, 1, n - 1)
    end_memo = time.perf_counter_ns()

    # Tiempos del algoritmo bottom-up
    init_bottom = time.perf_counter_ns()
    cost_bottom = bottom_up(A, 1, n - 1)
    end_bottom = time.perf_counter_ns()

    # Secuencia de multiplicacion de minimo coste
    secuencia = analisis_de_memoria(A)

    print('Tiempo de ejecución (nanosegundos):')
    print('Recursivo: ', (end_rec - init_rec))
    print('Memoizado: ', (end_memo - init_memo))
    print('Bottom-Up: ', (end_bottom - init_bottom))

    print ('Coste mínimo (número de multiplicaciones):')
    print('Recursivo: ', cost_rec)
    print('Memoizado: ', cost_memo)
    print('Bottom-Up: ', cost_bottom)

    print('Análisis de memoria :')
    print('Secuencia: ', secuencia)
# end def

# ---------------------------------Algoritmo recursivo----------------------------------------
# Complejidad O(2^n)
def mult_chain(d, i, j):
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

# ---------------------------------Algoritmo memoizado----------------------------------------
def memoizacion(d, i, j):
    M = {}
    return aux_memoizacion(d, i, j, M)
# end def

def aux_memoizacion(d, i, j, M):
    if (i, j) in M:
        return M[(i, j)]
    # end if
    if i == j:
        return 0
    #end if
    cost = float('inf')
    for k in range(i, j):
        cost_act = (aux_memoizacion(d, i, k, M) +
                    aux_memoizacion(d, k + 1, j, M) +
                    d[i - 1] * d[k] * d[j])
        if cost_act < cost:
            cost = cost_act
        # end if
    # end for
    M[(i, j)] = cost
    return cost
# end def

# ---------------------------------Algoritmo bottom-up-----------------------------------------
def bottom_up(d, i, j):
    n = j - i + 1 # Numero de matrices a multiplicar.
    m = [[0] * n for _ in range(n)] # Se llena de ceros la matriz en los casos base
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                # end if
            # end for
        # end for
    # end for
    return m[0][n - 1]
# end def

# --------------------------Algoritmo de análisis de memoria-----------------------------------
def analisis_de_memoria(d):
    n = len(d) - 1  # número de matrices
    m = [[0] * n for _ in range(n)]  # costos
    s = [[0] * n for _ in range(n)]  # particiones

    # Llena la tabla m
    for l in range(2, n + 1): 
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
                # end if
            # end for
        # end for
    # end for

    pasos = []
    construir_secuencia(s, 0, n - 1, pasos)
    return pasos
# end def

def construir_secuencia(s, i, j, pasos):
    if i == j:
        return (i + 1, j + 1)  
    else:
        k = s[i][j]
        izquierda = construir_secuencia(s, i, k, pasos)
        derecha = construir_secuencia(s, k + 1, j, pasos)
        pasos.append((izquierda, derecha))
        return (i + 1, j + 1)  # rango completo 
# end def


## -------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3", sys.argv[0], "input_file")
        sys.exit(1)
    # end if

    Af = open(sys.argv[1], 'r').readlines()
    A = [int(a) for a in Af][0:]

    print(A)
    mat_mult(A)