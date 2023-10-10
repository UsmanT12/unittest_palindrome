'''
Function to check if the input string is a palindrome 
It is a palindrome if it is the same string when written backwards 
All spaces, non alphanumeric characters, and character cases are ignored.
'''

def isPalindrome(s: str) -> bool:
    s = s.lower()
    string = ''

    for i in range(len(s)):
        if s[i].isalnum() == True:
            string += s[i]
    begin = 0
    end = len(string) - 1

    while begin < end:
        if string[begin] != string[end]:
            return False
        begin += 1
        end -= 1
    return True
