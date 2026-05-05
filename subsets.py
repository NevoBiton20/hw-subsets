def sorted_subset_sums(numbers: set):
    """
    >>> list(sorted_subset_sums({1, 2, 4}))
    [0, 1, 2, 3, 4, 5, 6, 7]

    >>> list(sorted_subset_sums({1, 2, 3}))
    [0, 1, 2, 3, 3, 4, 5, 6]

    >>> list(sorted_subset_sums({2, 3, 4}))
    [0, 2, 3, 4, 5, 6, 7, 9]

    >>> list(sorted_subset_sums(set()))
    [0]

    >>> list(sorted_subset_sums({5}))
    [0, 5]
    """
    nums = sorted(numbers)

    yield 0

    if not nums:
        return

    heap = [(nums[0], 0)]

    while heap:
        current_sum, i = heappop(heap)
        yield current_sum

        next_i = i + 1

        if next_i < len(nums):
            heappush(heap, (current_sum + nums[next_i], next_i))
            heappush(heap, (current_sum - nums[i] + nums[next_i], next_i))

if __name__ == '__main__':
    from itertools import takewhile, islice
    for i in eval(input()):
        print(i, end=", ")
    pass
