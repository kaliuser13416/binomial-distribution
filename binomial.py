import math;
import numpy as np;

print("This is a simple program for calculating the binomial distribution.");
print("calculate Sum(binomial distribution) (Y/n)?");

once = input(":/$ " )
keep = {};
index = 0;
total = 0;

def some():
    Num = math.comb(n, i) * pow(p,i) * pow((1 - p), n-i);
    return Num;

if once == "n":
    print("number of trials");
    n = int(input(":/$ " ));
    print("number of “successes”");
    x = int(input(":/$ " ));
    print("probability of a success");
    p = float(input(":/$ " ));
    Num = math.comb(n, x) * pow(p,x) * pow((1 - p), n-x);
    print("probability is:");
    print(Num);

elif once == "Y":
    
    print("number of trials");
    n = int(input(":/$ " ));
    print("probability of a success");
    p = float(input(":/$ " ));
    print("lower bound of “successes”");
    i = int(input(":/$ " ));
    print("upper bound of “successes”");
    x = int(input(":/$ " ));
    while (i < x):
        keep[index] = some();
        total=total+keep[index];
        i = i + 1;
        index = index + 1;
    
    print("probability is:");
    print(total);
    
else:
    print("invalid input");