import turingarena as ta
import random

def my_assert(cond, name_assert):
    if not cond:
        print(f"My Assert {name_assert} failed !!!")

def test_case(n,B0,x):             

    def incoming_x_at_the_end_of_current_period(num_periods_after_current_one):
        my_assert(num_periods_after_current_one < n, "num_periods_after_current_one < n")
        my_assert(num_periods_after_current_one >= 0, "num_periods_after_current_one >= 0")
        return x[n-1-num_periods_after_current_one]

    def call_num_traces_starting_from(starting_budget_for_current_period,num_periods_after_current_one):
        risp = None
        with ta.run_algorithm(ta.submission.source) as process:
            try:
                risp = process.functions.num_traces_starting_from(starting_budget_for_current_period,num_periods_after_current_one, callbacks = [incoming_x_at_the_end_of_current_period, call_num_traces_starting_from])
            except ta.AlgorithmError as e:
                print(e)
        return risp


    with ta.run_algorithm(ta.submission.source) as process:
        try:
            risp = process.functions.num_traces_starting_from(B0,n-1, callbacks = [incoming_x_at_the_end_of_current_period, call_num_traces_starting_from])
        except ta.AlgorithmError as e:
            ta.goals["n_times_max_B"] = False
            ta.goals["enumerate_one_by_one"] = False
            ta.goals["enumerate_one_by_one"] = False
            print(e)
    print(f"Your risp = {risp} on instance (n={n}, B0={B0}, x={x}")

    
for n in [1,2,3]:
    for B0 in [0,1,2]:
        for MAX_y in [0, 1, 2]:
            y = [random.randint(0, MAX_y) for _ in range(n)]
            test_case(n,B0,y)
        
