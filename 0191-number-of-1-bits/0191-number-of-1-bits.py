class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_binary=bin(n)[2:]
        res=str(number_binary)
        return res.count("1")