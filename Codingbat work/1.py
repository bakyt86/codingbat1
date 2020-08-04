1-##Given a string and a non-negative int n, return a larger string that is n copies of the original string.
##
##
##string_times('Hi', 2) → 'HiHi'
##string_times('Hi', 3) → 'HiHiHi'
##string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  result = ""
  for i in range(n):
    result = result + str
  return result

2-##Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
##
##
##front_times('Chocolate', 2) → 'ChoCho'
##front_times('Chocolate', 3) → 'ChoChoCho'
##front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  if len(str)<=3:
    return str*n
  return str[0:3]*n

3-##Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
##
##
##string_bits('Hello') → 'Hlo'
##string_bits('Hi') → 'H'
##string_bits('Heeololeo') → 'Hello'

def string_bits(str):
  if len(str)==1:
    return str
  k = ''
  for i in range(0,len(str),2):
    k = k + str[i]
  return k

4-#Given a non-empty string like "Code" return a string like "CCoCodCode".
##
##
##string_splosion('Code') → 'CCoCodCode'
##string_splosion('abc') → 'aababc'
##string_splosion('ab') → 'aab'

def string_splosion(str):
  k = ''
  for i in range(1,len(str)+1):
    k = k + str[0:i]
  return k

5-##Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
##
##
##last2('hixxhi') → 1
##last2('xaxxaxaxx') → 1
##last2('axxxaaxx') → 2

def last2(str):
  count = 0
  x = str[-2:]
  for i in range(len(str)-2):
    if str[i:i+2]==x:
      count = count +1
  return count    

  
6-##Given an array of ints, return the number of 9's in the array.
##
##
##array_count9([1, 2, 9]) → 1
##array_count9([1, 9, 9]) → 2
##array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  acount = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      acount = acount + 1
  return acount


7-##Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
##
##
##array_front9([1, 2, 9, 3, 4]) → True
##array_front9([1, 2, 3, 4, 9]) → False
##array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  x = len(nums)
  if x > 4:
     x = 4
    
  for i in range(x):
    if nums[i]==9:
       return True
  else:
      return False

8-##    
##Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
##
##
##array123([1, 1, 2, 3, 1]) → True
##array123([1, 1, 2, 4, 1]) → False
##array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

9-##
##Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
##
##
##string_match('xxcaazz', 'xxbaaz') → 3
##string_match('abc', 'abc') → 2
##string_match('abc', 'axc') → 0

def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2]==b[i:i+2]:
      count = count + 1
  return count

#list -2

##Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
##
##
##count_evens([2, 1, 2, 3, 4]) → 3
##count_evens([2, 2, 0]) → 3
##count_evens([1, 3, 5]) → 0

def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count = count + 1
  return count

2-##Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
##
##
##big_diff([10, 3, 5, 6]) → 7
##big_diff([7, 2, 10, 9]) → 8
##big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
  x = min(nums)
  y = max(nums)
  return y - x


3-##Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
##
##
##centered_average([1, 2, 3, 4, 100]) → 3
##centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
##centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  x = min(nums)
  y = max(nums)
  nums.remove(x)
  nums.remove(y)
  return sum(nums)//len(nums)


4-##Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
##
##
##sum13([1, 2, 2, 1]) → 6
##sum13([1, 1]) → 2
##sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  if len(nums)==0:
    return 0
  if nums[-1]==13:
    nums[-1]=0
  for i in range(len(nums)):
    if nums[i]==13:
     nums[i]=0
     nums[i+1]=0
  return sum(nums)


5-##Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
##
##
##sum67([1, 2, 2]) → 5
##sum67([1, 2, 2, 6, 99, 99, 7]) → 5
##sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  total = 0
  found6 = False
  for i in range(len(nums)):
    if nums[i]==6:
      found6=True
    if not found6: # True
      total+=nums[i]
    if nums[i]==7 and found6:
      found6=False
  return total    


6-##Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
##
##
##has22([1, 2, 2]) → True
##has22([1, 2, 1, 2]) → False
##has22([2, 1, 2]) → False

def has22(nums):
  nums.append(1)
  for i in range(len(nums)):
    if nums[i]==2 and nums[i+1]==2:
      return True
  return False

S
