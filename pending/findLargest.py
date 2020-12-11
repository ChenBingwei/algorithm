def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums_length = len(nums)
    for i in range(nums_length):
        for j in range(0, nums_length - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums[k - 1]


if __name__ == '__main__':
    print(findKthLargest([1, 2, 6, 7, 23, 5, 3, 9], 3))
