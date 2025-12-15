[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/o9Hgs2pM)
## Introduction to Programming
## Winter Semester 2025/26 -- Assignment 6
## All concepts required for these tasks have been covered in the lectures and examples.


---
##task1

Write a function:
`estimate_pi(num_samples)`
that:
returns an estimate of π using num_samples random points generated with np.random.rand().

---
##task2

Write a function:
`get_random_subset_of_naturals_up_to_20()`
that:
outputs a random subset of the set of integers between $1$ and $20$ in the format of a `numpy` array.
The draw of the subset should be uniform, i.e., any subset should in principle have the same chance to be outputted by your function. This problem will be graded manually.
For $2$ out of the $5$ points allotted to this problem, you can write your function however you wish. To get $5$ points, your function is allowed to make a single call to the `numpy.random.randint()` method
but it cannot make use of any other random methods.

---
##task3

Write a function:
`random_unit_vectors(num_vectors, dim)`
that:
a)creates a matrix M of shape (num_vectors, dim)using;

M = np.random.randn(num_vectors, dim)

b)normalizes each row so it has Euclidean norm 1,

and c)returns the resulting matrix as a NumPy array.

