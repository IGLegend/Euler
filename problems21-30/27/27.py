# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, -79 and 1601, is -126479.
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| <= 1000 
# where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4.
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes 
# for consecutive values of n, starting with n = 0.

def main():
    #? A list of all primes < 88000
    primes = [2]
    for i in range(3, 88000):
        isPrime = True
        for p in primes:
            if i%p == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
    
    #? A list of all primes < 1000
    primes1000 = []
    for p in primes:
        if p < 1000:
            primes1000.append(p)
        else:
            break

    #? Checking how many primes roll out of n²+an+b.
    def checkFormula(a, b):
        n = 0
        amountPrimes = 0
        while True:
            if (n**2 + a*n + b) in primes:
                amountPrimes += 1
            else:
                break

            n += 1
        return (amountPrimes, a*b)

    #? Iterating through all possible a and b values.
    mostPrimes = (0, 0)
    for a in range(-999, 999, 2):
        for b in primes1000:
            if checkFormula(a, b)[0] > mostPrimes[0]:
                mostPrimes = checkFormula(a, b)
    
    print(f"{mostPrimes}")


if __name__ == "__main__":
    main()
