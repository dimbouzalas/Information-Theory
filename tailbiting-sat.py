import random
from pysat.solvers import Glucose3


L = 100           
n = 100           
w = 3             

def generate_tailbiting_2sat(L, n, r, w):
   
    N = L * n
    M = int(r * N)
    clauses = []

    for _ in range(M):
        
        i = random.randint(0, L - 1)
        window_start = i
        window_end = i + w

       
        b1 = random.randint(window_start, window_end - 1) % L
        b2 = random.randint(window_start, window_end - 1) % L

        
        v1 = random.randint(b1 * n, (b1 + 1) * n - 1)
        v2 = random.randint(b2 * n, (b2 + 1) * n - 1)
        while v1 == v2:
            v2 = random.randint(b2 * n, (b2 + 1) * n - 1)

        
        lit1 = (v1 + 1) * random.choice([-1, 1])
        lit2 = (v2 + 1) * random.choice([-1, 1])

        clauses.append([lit1, lit2])

    return clauses

def solve_instance(r):
    
    clauses = generate_tailbiting_2sat(L=L, n=n, r=r, w=w)
    clauses = [list(map(int, clause)) for clause in clauses]
    solver = Glucose3()
    solver.append_formula(clauses)
    result = solver.solve()
    solver.delete()
    return result
