import random

import turingarena as ta

NUM_MACHINES = 100

def test_case(n,B0_,x_):             
        with ta.run_algorithm(ta.submission.source) as process:
            def B0():
                return B0_
            def x():
                return x_(i)
            try:
                process.functions.conta_storie(n, callbacks = [B0, x]))
            except ta.AlgorithmError as e:
                ta.goals["n_times_max_B"] = False
                ta.goals["enumerate_one_by_one"] = False
                ta.goals["enumerate_one_by_one"] = False
                print(e)
        print(f"Your P({n}) = {memoP[n]}")

    P_is_new = True
    first_n_diff = None
    for i in range(0,NUM_MACHINES):
        P_and_Pi_differ = False
        for j in range(0,i+1):
            if memoM[i][j] != memoP[j]:
                P_and_Pi_differ = True
                first_n_diff = j
                break
        if P_and_Pi_differ:
            print(f"The first diff with machine P_{i} is on the natural {first_n_diff}. Here, P({first_n_diff}) = {memoP[first_n_diff]} whereas P({i}) = {memoM[i][first_n_diff]}")
        else:
            ta.goals.setdefault("correct", False)
            print(f"NO: your property P coincides with our property P_{i} for all n <= {i}. Indeed, P[0..{i}] = {memoP[:i+1]} and P_{i}[0..{i}] = {memoM[i][:i+1]}")


    
for n in [1,2,3,5,10,20,50]:
    for B0 in [0,1,5,10,100,1000,10000]:
        for MAX_y in [0, 2, 10]:
            y = [random.randint(0, MAX_y) for _ in range(n)]
                test_case(n,B0,y)
        
ta.goals.setdefault("correct", True)
print(ta.goals)

