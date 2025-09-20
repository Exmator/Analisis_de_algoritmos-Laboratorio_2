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

## -------------------------------------------------------------------------
if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "input_file")
    sys.exit(1)
# end if

Af = open(sys.argv[1], 'r').readlines()
A = [int(a) for a in Af][0:]

print(A)
print(mat_mult(A))

