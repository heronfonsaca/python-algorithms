from typing import List

from sorts.insertion import insertion_sort


def test_insertion_sort_inplace() -> None:
    items: List[int] = []
    insertion_sort(items=items, ascending=False, inplace=True)
    assert items == []


def test_insertion_sort_2_digits_asc_sorted() -> None:
    assert insertion_sort([1, 2]) == [[1, 2]]


def test_insertion_sort_2_digits_desc_sorted() -> None:
    assert insertion_sort([2, 1], ascending=False) == [[2, 1]]


def test_insertion_sort_3_digits_asc() -> None:
    assert insertion_sort([7, 1, 4]) == [
        [7, 1, 4],
        [1, 7, 4],
        [1, 4, 7],
    ]


def test_insertion_sort_3_digits_desc() -> None:
    assert insertion_sort([4, 1, 7], ascending=False) == [
        [4, 1, 7],
        [4, 7, 1],
        [7, 4, 1],
    ]


def test_insertion_sort_4_digits_asc() -> None:
    assert insertion_sort(items=[5, 9, 3, 7]) == [
        [5, 9, 3, 7],
        [5, 3, 9, 7],
        [3, 5, 9, 7],
        [3, 5, 7, 9],
    ]


def test_insertion_sort_4_digits_desc() -> None:
    assert insertion_sort(items=[7, 3, 9, 5], ascending=False) == [
        [7, 3, 9, 5],
        [7, 9, 3, 5],
        [9, 7, 3, 5],
        [9, 7, 5, 3],
    ]
