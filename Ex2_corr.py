n= int(input('primefactors.py '))
print(n, ' = ' , end='')

for i in range(3,n+1):
    if(n%i) == 0:
        while(n%i ==0 ):
            n = n/i
            print(i , end='')
            if(n!=1):
                print(' * ',end='')
# slower than the suggested algorithm
