import math

def isPrime(x):
    #Determines if a number is prime (divisible only by itself and 1)
    prime = 1
    for y in range(2,x):
        if x%y == 0:
            prime = 0
    if prime == 0:
        return bool(0)
    elif prime == 1:
        return bool(1)

def isPerfect(x):
    #Determines if a number is perfect (equal to the sum of its divisors)
    factors=0
    for y in range (1,x-1):
        if x%y == 0:
            factors += y
    if factors == x:
        return bool(1)
    else:
        return bool(0)

def isAbundant(x):
    #Determines if a number is abundant(sum of its divisors is greater than itself)
    factors=0
    for y in range (1,x-1):
        if x%y == 0:
            factors += y
    if factors > x:
        return bool(1)
    else:
        return bool(0)

def isNarcissistic(x):
    #Determines if a number is narcisssistic (sum of the nth powers of its digits sums up to the number itself.)
    length =len(str(x))
    total = 0
    for y in range (1, length+1):
        total += (x/(10**(y-1))%10)**length
    if x == total:
        return bool(1)
    else:
        return bool(0)

def isHarshad(x):
    #Determines if a number is harshad (divisible by the sum of its digits)
    length =len(str(x))
    total = 0
    for y in range (1, length+1):
        total += (x/(10**(y-1))%10)

    if (x % total == 0):
        return bool(1)
    else:
        return bool(0)

def isHexagonal(x):
    #Determines if a number is hexagonal (can be expressed in the form 2n^2 − n.)
    num = ((1+math.sqrt(1+8*x))/4)
    if num == int(num):
        return bool(1)
    else:
       return bool(0)

def main():
    #Asks user for an input number and then displays properties
    num = input ("Please enter a number between 1 and 1000: ")
    print str(num),
    if isPrime(num):
        print "is prime,",
    else:
        print "is not prime,",
    if isPerfect(num):
        print "is perfect,",
    else:
        print "is not perfect,",
    if isAbundant(num):
        print "is abunadnt,",
    else:
        print "is not abundant,",
    if isNarcissistic(num):
        print "is Narcissistic,",
    else:
        print "is not Narcissistic,",
    if isHarshad(num):
        print "is Harshad,",
    else:
        print "is not Harshad,",
    if isHexagonal(num):
        print "is hexagonal"
    else:
        print "is not hexagonal"

if __name__ == "__main__":
    main()
