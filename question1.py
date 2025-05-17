class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(1,(n//2)+1):
            if (n%i==0):
                count += 1
                if count == k:
                    return i
        if count+1 == k:
            return n
        return -1