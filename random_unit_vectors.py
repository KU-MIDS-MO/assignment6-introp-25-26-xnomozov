import numpy as np

def random_unit_vectors(num_vectors, dim):
    """
    Write a function: random_unit_vectors(num_vectors, dim) that: 
    a)creates a matrix M of shape (num_vectors, dim)using;

    M = np.random.randn(num_vectors, dim)

    b)normalizes each row so it has Euclidean norm 1,

    and c)returns the resulting matrix as a NumPy array.
    """
   
    M = np.random.randn(num_vectors, dim)        
    norms = np.sqrt(np.sum(M**2, axis=1, keepdims=True))  
    return M / norms    