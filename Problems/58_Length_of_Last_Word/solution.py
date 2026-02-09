class Solution(object):
    def lengthOfLastWord(self, s):
        s_len = len(s)
        last = s_len - 1
        while s[last] == ' ':
            last -= 1
            
        last_len = 0
        while last >= 0 and s[last] != ' ':
            last_len += 1
            last -= 1
            
        return last_len
        
