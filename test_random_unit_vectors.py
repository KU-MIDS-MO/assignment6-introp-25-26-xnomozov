import numpy as np
from random_unit_vectors import random_unit_vectors

def test_random_unit_vectors_shape_and_norms():
    ## fix the seed so the random numbers are reproducible
    np.random.seed(123)

    num_vectors = 5
    dim = 3

    U = random_unit_vectors(num_vectors, dim)

    ## check shape
    assert isinstance(U, np.ndarray)
    assert U.shape == (num_vectors, dim)

    ## check that each row has L2 norm very close to 1
    norms = np.linalg.norm(U, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-12), \
        f"Row norms are not all 1: {norms}"

def test_random_unit_vectors_first_row_values():
    ## with seed 123 and a corect implementation using np.random.randn(num_vectors, dim)
    ## and row-wise normalization, the first row should look like this:
    np.random.seed(123)

    U = random_unit_vectors(5, 3)

    expected_first_row = np.array([
        -0.72321256,
         0.66439980,
         0.18851127
    ])

    assert np.allclose(U[0], expected_first_row, atol=1e-8), \
        f"First row does not match expected values.\nExpected: {expected_first_row}\nGot: {U[0]}"
