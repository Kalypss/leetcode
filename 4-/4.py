"""4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


def MedTwoSortedArrays(tab1:list, tab2:list):
    # Merging tabs: 
    tab_merged = sorted(tab1 + tab2)
    n = len(tab_merged)
    if n % 2 == 0:
        median_tab = (tab_merged[n // 2 - 1] + tab_merged[n // 2]) / 2.0
    else:
        median_tab = tab_merged[n // 2]
    return median_tab


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tab_merged = sorted(nums1 + nums2)
        n = len(tab_merged)
        if n % 2 == 0:
            median_tab = (tab_merged[n // 2 - 1] + tab_merged[n // 2]) / 2.0
        else:
            median_tab = tab_merged[n // 2]
        return median_tab

if __name__ == "__main__" :
    print(MedTwoSortedArrays([1,3], [2]))
    print(MedTwoSortedArrays([1,2], [3,4]))
    
    
    