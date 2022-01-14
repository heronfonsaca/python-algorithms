# 🐍 Algorithms
<a href="https://github.com/heronfonsaca/python-algorithms/actions"><img alt="Actions status" src="https://github.com/heronfonsaca/python-algorithms/actions/workflows/main.yml/badge.svg"></a>
<a href="https://codecov.io/gh/heronfonsaca/python-algorithms"><img src="https://codecov.io/gh/heronfonsaca/python-algorithms/branch/main/graph/badge.svg?token=9CIF8E79QO"/></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Well-known computer science algorithms published for practice and educational purposes.

## Sorting
Bubble, selection and insertion sort algorithms were implemented to retrieve all iterations of their respective processes, instead of the sorted items.

### Bubble
```python
>>> bubble_sort([3, 2, 1])
[[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 2, 3]]
>>> bubble_sort([1, 2, 3], ascending=False)
[[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 2, 1]]
```

### Selection
```python
>>> selection_sort([3, 1, 2])
[[3, 1, 2], [1, 3, 2], [1, 2, 3]]
>>> selection_sort([2, 1, 3], ascending=False)
[[2, 1, 3], [3, 1, 2], [3, 2, 1]]
```

### Insertion
```python
>>> insertion_sort([3, 1, 2])
[[3, 1, 2], [1, 3, 2], [1, 2, 3]]
>>> insertion_sort([2, 1, 3], ascending=False)
[[2, 1, 3], [2, 3, 1], [3, 2, 1]]
```

### Merge
Returns a list of tuples containing all merges performed.
```python
>>> merge_sort([2, 3, 1])
[([3, 1], [1, 3]), ([2, 3, 1], [1, 2, 3])]
>>> merge_sort([2, 1, 3], ascending=False)
[([1, 3], [3, 1]), ([2, 1, 3], [3, 2, 1])]
```