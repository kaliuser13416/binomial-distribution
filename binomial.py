import math

binomial = lambda n, r, p: math.comb(n, r) * pow(p, r) * pow((1-p),(n-r))
def binomial_sum(L, U, n, p):
    aws = []
    while L <= U:
        aws.append((binomial(n,L,p)))
        L = L + 1
    return sum(aws)

cal_sum = input("calculate Sum(binomial distribution) (Y/n)? ")
n = int(input("number of trials: " ))
p = float(input("probability of a success: " ));

if cal_sum == "Y":
    low = int(input("lower bound of successes: "))
    up = int(input("upper bound of successes: "))
    print(binomial_sum(low, up, n, p))
else:
    r = int(input("number of successes: "))
    print(binomial(n,r,p))
