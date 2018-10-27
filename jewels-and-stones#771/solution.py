class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_set = set(J)
        count = 0
        for stone in S:
            if stone in j_set:
                count = count + 1
        return count