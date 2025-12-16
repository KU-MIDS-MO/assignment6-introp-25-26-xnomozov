import  numpy as np


def estimate_pi(num_samples):
    
    """
    
    Write a function: estimate_pi(num_samples) that: returns an estimate 
    of π using num_samples random points generated with np.random.rand().
    
    """

    points = np.random.rand(2, num_samples)

    distance = points[0, :] ** 2 + points[1, :] ** 2

    hits = np.sum(distance <= 1)

    estimate = 4 * (hits / num_samples)

    return estimate
    



    
    
   
