from math import floor, ceil
def buses_needed(people_count, bus_capacity):
   return ceil(people_count / bus_capacity)