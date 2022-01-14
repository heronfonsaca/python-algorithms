"""Merge Sort Algorithm"""

from typing import List, Tuple


def _merge(left: List[int], right: List[int], ascending: bool = True) -> List[int]:
    """Merges two lists of integers in one sorted list.

    Args:
        left (List[int]): list left part to merge.
        right (List[int]): list right part to merge.
        ascending (bool): sort ascending vs. descending.

    Returns:
        (List[int]): list of merged parts containing
            sorted integers.
    """
    comparison = "__lt__" if ascending else "__gt__"
    result = []

    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if getattr(left[left_index], comparison)(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:] or right[right_index:])
    return result


def _merge_sort(
    items: List[int],
    iterations: List[Tuple[List[int], List[int]]],
    ascending: bool = True,
) -> List[int]:
    """Sorts list of integers, writing down every
    merge done and its respective result into "iterations"
    parameter.

    Args:
        items (List[int]): list of integers to sort.
        iterations (List[Tuple[List[int], List[int]]]):
            list of tuples containing the input integer list and
            its respective output integer list from _merge() call.
        ascending (bool): sort ascending vs. descending.

    Returns:
        (List[int]): list of merged parts containing
            sorted integers.
    """
    length = len(items)
    if length < 2:
        return items

    middle = length // 2
    left = _merge_sort(items[:middle], iterations, ascending)
    right = _merge_sort(items[middle:], iterations, ascending)

    result = _merge(left, right, ascending)
    iterations.append((items, result.copy()))
    return result


def merge_sort(
    items: List[int],
    ascending: bool = True,
) -> List[Tuple[List[int], List[int]]]:
    """Sorts list of integers using Merge Sort algorithm.

    Args:
        items (List[int]): list of integers to sort.
        ascending (bool): sort ascending vs. descending.

    Returns:
        (List[Tuple[List[int], List[int]]]):
            list of tuples containing the input integer list and
            its respective output integer list.

    Examples:
        >>> merge_sort([2, 3, 1])
        [([3, 1], [1, 3]), ([2, 3, 1], [1, 2, 3])]
        >>> merge_sort([2, 1, 3], ascending=False)
        [([1, 3], [3, 1]), ([2, 1, 3], [3, 2, 1])]
    """
    iterations: List[Tuple[List[int], List[int]]] = []
    _merge_sort(items=items, ascending=ascending, iterations=iterations)
    return iterations
