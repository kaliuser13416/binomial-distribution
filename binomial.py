from math import comb
cal_sum = str(input("calculate Sum(binomial distribution) (Y/n)? "))
n = int(input("number of trials: " ))
p = float(input("probability of a success: " ));
binomial = lambda n, r, p: comb(n, r) * (p ** r) * ((1 - p) ** (n - r))
binomial_sum = lambda L, U, n, p: sum(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(L, U + 1))
if cal_sum == "Y":
    L = int(input("lower bound of successes: "))
    U = int(input("upper bound of successes: "))
    print(binomial_sum(L,U,n,p))
else:
    r = int(input("number of successes: "))
    print(binomial(n,r,p))
