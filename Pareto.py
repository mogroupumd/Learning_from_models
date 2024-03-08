import numpy as np

"""
    To construct pareto fronts

    All algorithm codes are contributed by the answers in the following site:
    https://stackoverflow.com/questions/32791911/fast-calculation-of-pareto-front-in-python
    
    Note:
        is_pareto: finds the maximum pareto front (upper right)
        is_pareto_efficient_dumb: finds the minimum pareto front (lower left)
        is_pareto_efficient_simple: finds the minimum pareto front (lower left)
        is_pareto_efficient: finds the minimum pareto front (lower left)
"""
def is_pareto(data):
    output = np.ones(len(data), dtype=bool) # all points are pareto initially
    for i, values_i in enumerate(data):
        for j, values_j in enumerate(data):
            if j==i or output[j] == 0:
                continue # check non-self and all the other pareto points
            all_true = 1
            one_true = 0
            for vj, vi in zip(values_j, values_i):
                if all_true:
                    if vj < vi:
                        all_true = 0
                if not one_true:
                    if vj > vi:
                        one_true = 1
            if all_true and one_true: # j dominates i
                output[i] = 0
                break
    return output

# Very slow for many datapoints.  Fastest for many costs, most readable
def is_pareto_efficient_dumb(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i]>c, axis=1)) and np.all(np.any(costs[i+1:]>c, axis=1))
    return is_efficient


# Fairly fast for many datapoints, less fast for many costs, somewhat readable
def is_pareto_efficient_simple(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        if is_efficient[i]:
            is_efficient[is_efficient] = np.any(costs[is_efficient]<c, axis=1)  # Keep any point with a lower cost
            is_efficient[i] = True  # And keep self
    return is_efficient


# Faster than is_pareto_efficient_simple, but less readable.
def is_pareto_efficient(costs, return_mask = True):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :param return_mask: True to return a mask
    :return: An array of indices of pareto-efficient points.
        If return_mask is True, this will be an (n_points, ) boolean array
        Otherwise it will be a (n_efficient_points, ) integer array of indices.
    """
    is_efficient = np.arange(costs.shape[0])
    n_points = costs.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index<len(costs):
        nondominated_point_mask = np.any(costs<costs[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        costs = costs[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index])+1
    if return_mask:
        is_efficient_mask = np.zeros(n_points, dtype = bool)
        is_efficient_mask[is_efficient] = True
        return is_efficient_mask
    else:
        return is_efficient

def above_benchmarks(data, benchmarks):
    """
        To return a list of elements that are above benchmarks (errors below benchmark values)
    """
    return [m<=n for m, n in zip(data, benchmarks)]

def optimal_pareto_points(data, negative=True):
    """
        Find optimal points on Pareto fronts
    """
    output = is_pareto_efficient_simple(data)
    pareto_points = []
    negatives = None
    if negative:
        negatives = []
    for i, o in enumerate(output):
        if o:
            pareto_points.append([n for n in data[i]])
            if negative:
                negatives.append([-n for n in data[i]])
    return pareto_points, negatives

"""
    Functions to calculate GD, IGD, GD+, and IGD+ scores.
    Equations and calculation steps originate from:
        https://mlopez-ibanez.github.io/eaf/reference/igd.html
"""
def GD(solutions, references, p=1):
    def eu_d(v1, v2):
        return np.sqrt(sum([(m-n)**2 for m, n in zip(v1, v2)]))
    
    sum1 = 0
    for s in solutions:
        sum1 += min([eu_d(s, r)**p for r in references])
    return (sum1/len(solutions))**(1/p)

def IGD(solutions, references, p=1):
    return GD(references, solutions, p=1)

def GDplus(solutions, references, p=1):
    def eu_dplus(v1, v2):
        return np.sqrt(sum([max((m-n), 0)**2 for m, n in zip(v1, v2)]))
    
    sum1 = 0
    for s in solutions:
        sum1 += min([eu_dplus(s, r)**p for r in references])
    return (sum1/len(solutions))**(1/p)

def IGDplus(solutions, references, p=1):
    return GDplus(references, solutions, p=1)