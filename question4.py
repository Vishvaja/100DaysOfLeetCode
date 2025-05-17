class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        new_list = []
        maximum_val = max(candies)
        for i in candies:
            if i + extraCandies < maximum_val:
                new_list.append(False)
            else:
                new_list.append(True)
        return new_list