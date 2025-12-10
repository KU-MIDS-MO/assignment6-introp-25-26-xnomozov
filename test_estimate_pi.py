import numpy as np
from estimate_pi import estimate_pi

def test_estimate_pi_value_with_seed_0():
    ## fix the random seed so the result is reproducible
    np.random.seed(0)

    ## use a reasonably large sample size for a decent approximation
    num_samples = 100_000
    pi_hat = estimate_pi(num_samples)

    ## expected value computed using the same setup:
    ## np.random.seed(0); np.random.rand(100000,2) etc.
    expected = 3.13304

    ## allow a small numerical error
    assert np.isclose(pi_hat, expected, atol=1e-2), \
        f"Expected about {expected}, got {pi_hat}"

def test_estimate_pi_type_and_range():
    np.random.seed(1)
    num_samples = 10_000

    pi_hat = estimate_pi(num_samples)

    ## should be a float
    assert isinstance(pi_hat, float)

    ## should be somewhere "resonable" for pi
    assert 3.0 < pi_hat < 3.3, \
        f"Estimate seems unreasonable: {pi_hat}"

