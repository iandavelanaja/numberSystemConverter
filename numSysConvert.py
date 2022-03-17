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

    return str1

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

def hexToOct(n):
    """
    FUNCTION NOT YET FINISHED!
    """
    str1 = ''
    decList = []
    oct = 0
    for numbr in n:
        if numbr == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'A' or 'B' or 'C' or 'D' or 'E' or 'F':
            if numbr == 'a' or 'A':
                decList.append(11)
                continue
            if numbr == 'b' or 'B':
                decList.append(12)
                continue
            if numbr == 'c' or 'C':
                decList.append(13)
                continue
            if numbr == 'd' or 'D':
                decList.append(14)
                continue
            if numbr == 'e' or 'E':
                decList.append(15)
                continue
            if numbr == 'f' or 'F':
                decList.append(16)
                continue
        if numbr.isdigit():
            numbr = int(numbr)
            decList.append(numbr)
            continue
        else:
            print('Please input valid value. Quitting...')
            quit()
    for i in decList:
        str1 = decToBin(i) + str1
    return oct


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
    print('Please try again...')
    quit()