class Solution:
    def minOperations(self,s):
        a,b = '0', '1'
        count1, count2 = 0, 0
        for i in s:
            if i!=a:
                count1+=1
            if i!=b:
                count2+=1
            a, b = b, a
        return min(count1, count2)
