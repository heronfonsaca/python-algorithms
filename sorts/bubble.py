"""Bubble Sort Algorithm"""

from copy import copy
from typing import List


def bubble_sort(
    items: List[int],
    ascending: bool = True,
    inplace: bool = False,
) -> List[List[int]]:
    """Sorts list of integers using Bubble Sort algorithm.

    Args:
        items (List[int]): list of integers to sort.
        ascending (bool): sort ascending vs. descending.
        inplace (bool): if true, perform operation in-place.

    Returns:
        (List[List[int]]): list of lists containing each
        step (swap) of the sort process.

    Examples:
        >>> bubble_sort([1, 2])
        [[1, 2]]
        >>> bubble_sort([2, 1], ascending=False)
        [[2, 1]]
        >>> bubble_sort([3, 2, 1])
        [[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 2, 3]]
        >>> bubble_sort([1, 2, 3], ascending=False)
        [[1, 2, 3], [2, 1, 3], [2, 3, 1], [3, 2, 1]]
    """
    length = len(items)
    comparison = "__gt__" if ascending else "__lt__"

    if not inplace:
        items = items.copy()

    iterations = [copy(items)]
    for i in range(length):
        has_swapped = False
        for j in range(length - i - 1):
            if getattr(items[j], comparison)(items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                iterations.append(copy(items))
                has_swapped = True
        if not has_swapped:
            break
    return iterations
