## Functions That Converts ##

def decToBin(n):
    rem = []
    while True:
        res = int(n/2)
        xtra = int(n%2)
        if xtra == 0:
            rem.append(0)
            print('append 0')
            
        if xtra == 1:
            rem.append(1)
            print('append 1')
            
        if n == 0:
            break

        n = res
    str1 = ''
    for i in rem[::-1]:
        i = str(i)
        str1 = str1 + i

    return int(str1)

## main ##

str1 = int(input('Enter a number- '))
conBin = decToBin(str1)   

print('\nYour number- ', str1)
print('Binary equivalent: ', conBin)