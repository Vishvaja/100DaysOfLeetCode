from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        """
        :type digits: str
        :rtype: List[str]
        """
        inputs=[]
        dig_map = {"2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        for i in digits:
            inputs.append(dig_map[i])
        
        result = ["".join(p) for p in product(*inputs)]
        return result
        