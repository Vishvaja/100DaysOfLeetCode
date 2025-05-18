class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        x=[]
        for j in emails:
            
            new_word = ""
            word1, word2 = j.split("@")
            for i in word1:
                if i == ".":
                    continue
                elif i =="+":
                    break
                else:
                    new_word = new_word + i
            new_word = new_word + "@" + word2
            if new_word not in x:
                x.append(new_word)
        print(x)
        return len(x)