#Problem21.py
#Project Euler problem 21

from NumberTests import getFactors
from NumberTests import addNum
from NumberTests import isAmicable

def main():
  ami = []
  totList = []
  for num1 in range(0, 10001):
    for num2 in range((num1+1), 10001):
      if isAmicable(num1, num2):
        ami.append((num1, num2))
        totList.append(num1)
        totList.append(num2)
  print(ami)
  total = sum(totList)
  print(total)




if __name__ == '__main__':
  main()
