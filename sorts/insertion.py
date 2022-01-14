"""Insertion Sort Algorithm"""

from copy import copy
from typing import List


def insertion_sort(
    items: List[int],
    ascending: bool = True,
    inplace: bool = False,
) -> List[List[int]]:
    """Sorts list of integers using Insertion Sort algorithm.

    Args:
        items (List[int]): list of integers to sort.
        ascending (bool): sort ascending vs. descending.
        inplace (bool): if true, perform operation in-place.

    Returns:
        (List[List[int]]): list of lists containing each
        step (swap) of the sort process.

    Examples:
        >>> insertion_sort([1, 2])
        [[1, 2]]
        >>> insertion_sort([2, 1], ascending=False)
        [[2, 1]]
        >>> insertion_sort([3, 1, 2])
        [[3, 1, 2], [1, 3, 2], [1, 2, 3]]
        >>> insertion_sort([2, 1, 3], ascending=False)
        [[2, 1, 3], [2, 3, 1], [3, 2, 1]]
    """
    length = len(items)
    comparison = "__lt__" if ascending else "__gt__"

    if not inplace:
        items = items.copy()

    iterations = [copy(items)]
    for i in range(1, length):
        for j in range(i, 0, -1):
            if getattr(items[j], comparison)(items[j - 1]):
                items[j - 1], items[j] = items[j], items[j - 1]
                iterations.append(copy(items))
    return iterations
