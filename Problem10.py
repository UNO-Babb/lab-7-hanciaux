#Problem2.py
#Project Euler problem 2

from NumberTests import isPrime
from NumberTests import addNum

def main():
  total = 0
  primes = []
  for num in range(0, 2000001):
    if isPrime(num):
      primes.append(num)
  #print(primes)
  total = sum(primes)
  print(total)  


      
  
  

if __name__ == '__main__':
  main()
