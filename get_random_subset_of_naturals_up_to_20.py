import numpy as np

def get_random_subset_of_naturals_up_to_20():
    """
    Write a function: get_random_subset_of_naturals_up_to_20() that: outputs
    a random subset of the set of integers between 
    1 and 20 in the format of a numpy array. The draw of the subset should be uniform, i.e.,
    any subset should in principle have the same chance to be outputted by your function. T
    his problem will be graded manually. For 2 out of the 5
    points allotted to this problem, you can write your function however you wish. To get 5
    points, your function is allowed to make a single call to the numpy.random.randint() 
    method but it cannot make use of any other random methods.

    """
    N = 20
    S = np.arange(1, N + 1) 
   
    mask = np.random.choice([True, False], size=N, p=[0.5, 0.5])
    
    random_subset = S[mask]
    
    return random_subset

