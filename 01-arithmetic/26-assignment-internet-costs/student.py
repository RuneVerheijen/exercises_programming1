from math import ceil
def internet_costs(duration_in_seconds, cost_per_block):
    in_minutes = ceil(duration_in_seconds / 60)
    cost = ceil(in_minutes / 6)
    return cost * cost_per_block
