#!/usr/bin/python

import datetime
import string

def sum(x,y) :
   return x + y

def sub(x,y) :
   return x - y

def nextNum(x) :
   return x+1

def convert(x) :
   return x * 60

def tri_area(base,height) :
   return .5*base*height

def remainder(x,y) :
   return x % y

def calculate_exponent(x,y) :
   return x**y

def howmanyseconds(x) :
   return x*60*60

def next_edge(x,y) :
   return x+y-1

def find_perimeter(x,y) :
    return (x*2)+(y*2)

def getfirstvalue(x) :
   return x[0]

def land(x,y) :
  return x & y

def animals(chickens,cows,pigs) :
  return (chickens*2 + (cows + pigs)*4)

def issamenum(x,y) :
  return x == y

def lessthanorequalto_zero(x) :
  return x<=0

def to_int(x) :
  return int(x)

def to_str(x) :
  return str(x)

def squared(b) :
  return b*b

def findLargestNum(x) :
  largestThusFar = x[0]
  for a in x:
    if a > largestThusFar:
      largestThusFar = a
  return largestThusFar

def count_ones(x) :

  # Initialize number of Ones to Zero
  numOnes=0

  # If value of X is greater than Zero then work to do
  if x>0:
    n = 0   # n is power of 2
    numOnes=1 # atleast 1 '''1''' found as most significant bit '''msb'''

    # Determine most significant bit
    while x > 2**n: 
      n+=1

    # Equality implies value is a power of 2 and n has been determined 
    # Inequality implies value is not a power of 2 and n-1 represents msb    
    if (x!=2**n):
      n-=1

    # Calculate remaining value as msb accounted for
    remainingValue = x - (2**n)

    # Determine value of next msb incrementially
    while ((remainingValue > 0) and (n>0)):
      n-=1
      if remainingValue >= 2**n:
        numOnes+=1
        remainingValue-=2**n
  return numOnes

        
def factorial(x) :
  return x if x == 1 else x * factorial(x-1) if x > 0 else 0

def sum_numbers(x) :
  return x if x == 1 else x + sum_numbers(x-1) if x > 0 else 0

def double_char(x) :
  length = len(x)
  return x[0] + x[0] + double_char(x[1:length]) if length > 0 else ""   

def alphabet_soup(x) :
  currentIndex = 0
  minIndex = 0
  strLength = len(x)
  minChar = chr(ord("z")+1)

  if strLength > 1 :  
    for currentCharacter in x :
      if minChar > currentCharacter :
         minChar = currentCharacter
         minIndex = currentIndex
      currentIndex += 1
  elif strLength == 1 :
    minChar = x[0]
    return minChar
  else :
    return "" 

  retList = minChar
  return retList + (alphabet_soup(x[1:strLength]) if minIndex == 0 else alphabet_soup(x[0:minIndex] + x[minIndex+1:strLength]) if minIndex !=0 and minIndex != (strLength-1) else alphabet_soup(x[0:minIndex]))

def timeformilkandcookies(day) :
 return (day.month == 12) and (day.day==24)

def hamming_distance(str1,str2) :
 difference = 0

 str1Length = len(str1)
 str2Length = len(str2)

 index = 0

 primaryString = ""
 comparisonString = ""

 if str1Length > str2Length :
   primaryString = str2
   comparisonString = str1
   difference = str1Length - str2Length
 else :
   primaryString = str1
   comparisonString = str2
   difference = str2Length - str1Length

 while index < len(primaryString)  :
   difference += 1 if primaryString[index] != comparisonString[index] else 0
   index += 1
 return difference

#findevennums method uses LIST COMPREHENSION 
def findevennums(x) :
  returnList  = [val for val in range(2,x+1,2)]
  returnList

def nth_smallest(pList,n) :

   minVal = None

   if (n > 0) and (n < len(pList)) :
    for currentVal in pList :
       if minVal != None and currentVal < minVal :
          minVal = int(currentVal)
       elif minVal == None :
          minVal = int(currentVal)

    if (n == 1) :
       return minVal
    else :
       pList.remove(minVal)
       return nth_smallest(pList,n-1)
   elif minVal == None :
     print("None")
         
def unique_sort(xList) :
  # Purge : remove duplicates thru set conversion
  remainder = list(set(xList))

  #order
  orderedList = []

  for x in xList :
    minValue = None
    for y in remainder :
      if minValue == None :
        minValue = y
      elif y < minValue :
        minValue = y
    
    if minValue != None :
      remainder.remove(minValue)
      orderedList.append(minValue)

  return orderedList

def XO(pStr) :
  xCount = 0
  oCount = 0

  index = 0
  normalizedStr = string.lower(pStr)

  while index >= 0 :
   index = string.find(normalizedStr,"x",index)
   if index >= 0 :
     xCount += 1
     index += 1

  index = 0
  while index >= 0 :
   index = string.find(normalizedStr,"o",index)
   if index >= 0 :
     oCount += 1
     index += 1

  return xCount == oCount

def name_shuffle(name) :
  shuffledStr = ""
  wsIndex = string.find(name," ")
  if wsIndex >= 0 :
    shuffledStr = name[wsIndex+1:len(name)] + " " + name[0:wsIndex]
  else :
    print("Index Error : " + name + " : " + str(wsIndex))

  return shuffledStr

def reverse(boolVal) :
 booleanDetected = type(boolVal) is bool

# returnVal = ""
# if booleanDetected :
#   returnVal = not(boolVal)
# else : 
#   returnVal = "boolean expected"
# return returnVal

 return not(boolVal) if booleanDetected else "boolean expected"

def count_vowels(strVal) :
  nStrVal = string.lower(strVal) 
  vCount = string.count(nStrVal,"a")
  vCount += string.count(nStrVal,"e")
  vCount += string.count(nStrVal,"i")
  vCount += string.count(nStrVal,"o")
  vCount += string.count(nStrVal,"y")

  return vCount

def counterpartCharCode(charVal) :
  return ord(string.swapcase(charVal))

def can_alternate(bStrVal) :
  oneCount = 0
  zeroCount = 0
  index = 0

  while index >= 0 :
     index = string.find(bStrVal,"1",index)
     if index >= 0 :
        index += 1
        oneCount += 1

  index = 0

  while index >= 0 :
     index = string.find(bStrVal,"0",index)
     if index >= 0 :
        index += 1
        zeroCount += 1
 
  return True if (zeroCount == oneCount) or (abs(zeroCount - oneCount) == 1) else False

def amplify(intVal) :
   rList = [x  if x % 4 != 0 else x* 10 for x in range(intVal + 1)]
   return rList


def society_name(lVal) :
  interVal = ""
  for x in lVal :
    interVal += x[0]
  retVal = sorted(interVal.upper())

  return "".join(retVal)

def missing_num(lVal) :
  missingVal = None
  for x in range(10) :
    try :
      lVal.index(x+1)
    except :
      missingVal = x+1
  return missingVal

def correct_stream(userList,correctList) :
  retList = [1 if userList[x] == correctList[x] else -1 for x in range(len(userList))]
  return retList

def is_symmetrical(intVal) :
  rearIndex = -1
  retVal = True
  strVal = str(intVal)

  for x in range(len(str(strVal)) / 2) :
    if strVal[x] != strVal[rearIndex] :
      retVal = False
      break 
    rearIndex += -1

  return retVal   
