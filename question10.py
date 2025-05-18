from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        char_map = Counter(nums)
        print(char_map)
        x,y = char_map.most_common(1)[0]
        print(x,y)
        if y>=(len(nums)//2):
            return x

        return 0