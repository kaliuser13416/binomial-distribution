import math;

print("This is a simple program for calculating the binomial distribution.");
print("calculate Sum(binomial distribution) (Y/n)?");

once = input(": " )
keep = {};
index = 0;
total = 0;

print("number of trials");
n = int(input(": " ));
print("probability of a success");
p = float(input(": " ));

if once == "n":

    print("number of “successes”");
    i = int(input(": " ));
    total = math.comb(n, i) * pow(p,i) * pow((1 - p), n-i);


elif once == "Y":

    print("lower bound of “successes”");
    i = int(input(": " ));
    print("upper bound of “successes”");
    x = int(input(": " ));
    while (i < x):
        keep[index] = math.comb(n, i) * pow(p,i) * pow((1 - p), n-i);
        total=total+keep[index];
        i = i + 1;
        index = index + 1;
    
else:
    print("invalid input");

print("probability is:");
print(total);
