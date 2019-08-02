int count_traces_starting_from(int starting_budget_for_current_period, int num_periods_after_current_one, int incoming_x_at_the_end_of_current_period(int num_periods_after_current_one), int call_count_traces_starting_from(int starting_budget_for_current_period, int num_periods_after_current_one)) {
  if(num_periods_after_current_one == 0)
    return starting_budget_for_current_period + 1;
  int risp = 0;
  for(int spesa_at_current_period = 0; spesa_at_current_period <= B; spesa_at_current_period++)
    risp = risp + call_num_traces_starting_from(starting_budget_for_current_period -spesa_at_current_period +incoming_x_at_the_end_of_current_period(num_periods_after_current_one), num_periods_after_current_one -1 );
  return risp;
}

