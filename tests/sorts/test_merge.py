from sorts.merge import _merge, merge_sort


def test_merge_internal_1_digit_lists_asc_sorted() -> None:
    assert _merge(left=[1], right=[2], ascending=True) == [1, 2]


def test_merge_internal_1_digit_lists_desc_sorted() -> None:
    assert _merge(left=[2], right=[1], ascending=False) == [2, 1]


def test_merge_internal_2_digits_lists_asc() -> None:
    assert _merge(left=[1, 7], right=[3, 5], ascending=True) == [1, 3, 5, 7]


def test_merge_internal_3_1_digits_lists_asc() -> None:
    assert _merge(left=[2, 8], right=[4, 6], ascending=True) == [2, 4, 6, 8]


def test_merge_sort_3_digits_asc() -> None:
    assert merge_sort([7, 4, 1]) == [
        ([4, 1], [1, 4]),
        ([7, 4, 1], [1, 4, 7]),
    ]


def test_merge_sort_3_digits_desc() -> None:
    assert merge_sort([1, 5, 3], ascending=False) == [
        ([5, 3], [5, 3]),
        ([1, 5, 3], [5, 3, 1]),
    ]


def test_merge_sort_5_digits_asc() -> None:
    assert merge_sort([1, 5, 9, 4, 2]) == [
        ([1, 5], [1, 5]),
        ([4, 2], [2, 4]),
        ([9, 4, 2], [2, 4, 9]),
        ([1, 5, 9, 4, 2], [1, 2, 4, 5, 9]),
    ]
