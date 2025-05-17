class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        extras = []
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        count = 1
        for i in s:
            if i in extras:
                count += 1
                extras = []
            extras.append(i)

            print(count)
        return count