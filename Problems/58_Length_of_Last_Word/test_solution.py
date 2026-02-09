from solution import Solution

def test_lengthOfLastWord():
    solution = Solution()
    
    #test 1: no space at the end
    s = "Hello World"
    assert solution.lengthOfLastWord(s) == 5
    
    #test 2: spaces at the end
    s = "   fly me   to   the moon  "
    assert solution.lengthOfLastWord(s) == 4
    
    #test 3: no space at the end
    s = "luffy is still joyboy"
    assert solution.lengthOfLastWord(s) == 6
    
    #test 4: only one multi-letter word
    s = "Apple"
    assert solution.lengthOfLastWord(s) == 5
    
    #test 5: only one letter
    s = "A"
    assert solution.lengthOfLastWord(s) == 1
    
    #test 6: multiple spaces between words
    s = "a   b"
    assert solution.lengthOfLastWord(s) == 1