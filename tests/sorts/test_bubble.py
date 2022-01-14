from typing import List

from sorts.bubble import bubble_sort


def test_bubble_sort_inplace() -> None:
    items: List[int] = []
    bubble_sort(items=items, ascending=False, inplace=True)
    assert items == []


def test_bubble_sort_2_digits_asc_sorted() -> None:
    assert bubble_sort(items=[1, 2], ascending=True) == [[1, 2]]


def test_bubble_sort_2_digits_desc_sorted() -> None:
    assert bubble_sort([2, 1], ascending=False) == [[2, 1]]


def test_bubble_sort_3_digits_asc() -> None:
    assert bubble_sort([7, 4, 1]) == [
        [7, 4, 1],
        [4, 7, 1],
        [4, 1, 7],
        [1, 4, 7],
    ]


def test_bubble_sort_3_digits_desc() -> None:
    assert bubble_sort([1, 4, 7], ascending=False) == [
        [1, 4, 7],
        [4, 1, 7],
        [4, 7, 1],
        [7, 4, 1],
    ]


def test_bubble_sort_4_digits_asc() -> None:
    assert bubble_sort(items=[9, 5, 7, 3]) == [
        [9, 5, 7, 3],
        [5, 9, 7, 3],
        [5, 7, 9, 3],
        [5, 7, 3, 9],
        [5, 3, 7, 9],
        [3, 5, 7, 9],
    ]


def test_bubble_sort_4_digits_desc() -> None:
    assert bubble_sort(items=[3, 7, 5, 9], ascending=False) == [
        [3, 7, 5, 9],
        [7, 3, 5, 9],
        [7, 5, 3, 9],
        [7, 5, 9, 3],
        [7, 9, 5, 3],
        [9, 7, 5, 3],
    ]
