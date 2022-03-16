## Functions That Converts ##

def decToBin(n):
    '''
    converts decimal to binary
    '''
    rem = []
    while True:
        res = int(n/2)
        xtra = int(n%2)
        if xtra == 0:
            rem.append(0)
            
        if xtra == 1:
            rem.append(1)
            
        if n == 0:
            break

        n = res
    str1 = ''
    for i in rem[::-1]:
        i = str(i)
        str1 = str1 + i

    return int(str1)

def binToDec(num):
    '''
    converts binary to decimal
    '''
    binList = []
    n = 0
    total = 0

    intStr = str(num)
    for i in intStr:
        if i == '1' or i == '0':
            i = int(i)
            binList.append(i)
        else:
            print('Enter Binary Values only (0, 1)!')
            quit()
    
    binList = binList[::-1]

    for x in binList:
        dcml = x * (2**n)
        n = n + 1
        total = total + dcml


    return int(total)

## main ##

print('\nWhat would you like to convert? \n')
print('1: Binary to Decimal')
print('2: Decimal to Binary')

ans = (input())

try:
    ans = int(ans)
    if ans in range(1,3):
        if ans == 1:
            print('Enter Binary Value (1,0): ')
            bn = input()
            print('Binary: ', bn)
            print('Decimal: ', binToDec(bn))
            quit()
        if ans == 2:
            print('Enter Decimal Value : ')
            try:
                dc = int(input())
                print('Decimal: ', dc)
                print('Binary: ', decToBin(dc))
                quit()
            except ValueError:
                print('Entered value not valid.')
                quit()
except ValueError:
    print('Entered operation not valid. Quitting...')
    quit()