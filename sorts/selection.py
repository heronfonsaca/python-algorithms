"""Selection Sort Algorithm"""

from copy import copy
from typing import List


def selection_sort(
    items: List[int],
    ascending: bool = True,
    inplace: bool = False,
) -> List[List[int]]:
    """Sorts list of integers using Selection Sort algorithm.

    Args:
        items (List[int]): list of integers to sort.
        ascending (bool): sort ascending vs. descending.
        inplace (bool): if true, perform operation in-place.

    Returns:
        (List[List[int]]): list of lists containing each
        step (swap) of the sort process.

    Examples:
        >>> selection_sort([1, 2])
        [[1, 2]]
        >>> selection_sort([2, 1], ascending=False)
        [[2, 1]]
        >>> selection_sort([3, 1, 2])
        [[3, 1, 2], [1, 3, 2], [1, 2, 3]]
        >>> selection_sort([2, 1, 3], ascending=False)
        [[2, 1, 3], [3, 1, 2], [3, 2, 1]]
    """
    length = len(items)
    comparison = "__lt__" if ascending else "__gt__"

    if not inplace:
        items = items.copy()

    iterations = [copy(items)]
    for i in range(length - 1):
        edge = i
        for j in range(i + 1, length):
            if getattr(items[j], comparison)(items[edge]):
                edge = j
        if edge != i:
            items[i], items[edge] = items[edge], items[i]
            iterations.append(copy(items))
    return iterations
