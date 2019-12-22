# Sorting Algorithms
Compiled by [jedfras](https://github.com/jedfras).

## Counting Sort
Implementation(s): [Python](https://github.com/jedfras/sorting-algorithms/blob/master/countingsort.py)

### Description
Counting Sort sorts an array of integers on a certain range.
* `input`: input array (to be sorted)
* `count`: array that holds number of instances of each value

### Pseudocode
* Update `count` with number of instances of each value
* Update `count` such that each element stores the sum of the previous value
* Decrease each elements' count by 1
* Each element in `count` now indicates the sorted position of its corresponding `input` value