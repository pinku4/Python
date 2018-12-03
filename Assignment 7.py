n=100
list=[]
count =0
def main():
     n=input('enter the number of prime to be listed:')
     primes(n)
     for l in range(count):
         print list[1]
def primes(n):
    i=1
    for k in range(1,(n+1),1):
        c=0
        for j in range(1,(n+1),1):
            a=i%j
            if(a==0):
                c=c+1
            if(c==2):
                list.append(i)
                count+1

            else:
                k=k-1
                return list
            main()
