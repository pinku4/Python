from random import randint

def main():
    n=raw_input('enter a lengthof the random numberto be generated')
    m=random_with_N_digits(n)
    print m

def random_with_N_digits(n):
    range_start=10**(n-1)
    range_end=(10**n)-1
    o =randint(range_start,range_end)
    return o
main()
