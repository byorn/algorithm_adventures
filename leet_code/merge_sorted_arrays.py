class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while k >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                if i > 0:
                    i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                if j > 0:
                    j -= 1

        print(nums1)


s = Solution()
nums1 = [2, 3, 4, 0, 0, 0]
s.merge([2, 3, 4, 0, 0, 0], 3, [1, 3, 5], 3)

print(nums1)
