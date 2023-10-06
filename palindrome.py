def isPalindrome(s: str) -> bool:
  
  s = s.lower()
  string = ''
  
  for i in range(len(s)):
      if s[i].isalnum() == True:
          string += s[i]
  begin = 0
  end = len(string) - 1
  
  while (begin < end):
      if string[begin] != string[end]:
          return False
      begin += 1
      end -= 1
  return True
