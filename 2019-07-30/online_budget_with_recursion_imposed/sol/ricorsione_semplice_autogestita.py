def num_traces_starting_from(starting_budget_for_current_period, num_periods_after_current_one, incoming_x_at_the_end_of_current_period, call_num_traces_starting_from):
    if num_periods_after_current_one == 0:
        return starting_budget_for_current_period + 1
    risp = 0
    for spesa_at_current_period in range(starting_budget_for_current_period + 1):
        risp = risp + num_traces_starting_from(starting_budget_for_current_period -spesa_at_current_period +incoming_x_at_the_end_of_current_period(num_periods_after_current_one), num_periods_after_current_one -1 )
    return risp


