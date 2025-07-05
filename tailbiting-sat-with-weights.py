import random
import numpy as np
from pysat.solvers import Glucose3

L = 200
n = 40
w = 7

def generate_tailbiting_2sat_biased(L, n, r, w, bias_strength=1, biased_prob=0.7):
    N = L * n
    M = int(r * N)
    clauses = []

    exp_weights = [np.exp(-bias_strength * i) for i in range(w)]
    norm_weights = [w / sum(exp_weights) for w in exp_weights]

    for _ in range(M):
        i = random.randint(0, L - 1)
        if random.random() < biased_prob:
            window = [(i + offset) % L for offset in range(w)]
            b1 = random.choices(window, weights=norm_weights)[0]
            b2 = random.choices(window, weights=norm_weights)[0]
        else:
            b1 = random.randint(0, L - 1)
            b2 = random.randint(0, L - 1)

        v1 = random.randint(b1 * n, (b1 + 1) * n - 1)
        v2 = random.randint(b2 * n, (b2 + 1) * n - 1)
        while v1 == v2:
            v2 = random.randint(b2 * n, (b2 + 1) * n - 1)

        lit1 = (v1 + 1) * random.choice([-1, 1])
        lit2 = (v2 + 1) * random.choice([-1, 1])
        clauses.append([lit1, lit2])

    return clauses

def solve_instance(r):
    clauses = generate_tailbiting_2sat_biased(L=L, n=n, r=r, w=w)
    solver = Glucose3()
    solver.append_formula(clauses)
    result = solver.solve()
    solver.delete()
    return result

