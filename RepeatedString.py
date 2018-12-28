from collections import Counter

def repeatedString(s, n):
    # print('Inside Repeated String function')
    i = 1
    l, newL = len(s), len(s)
    count, newCount = Counter(s)['a'], Counter(s)['a']
    # print('Frequency of a: ', count)

    if(l!=1 and count != 1):
        while(newL+l<n):
            newL = i*l
            newCount = i*count 
            i+=1

        rem = n - newL
        # print('remo: ', rem)
        # print('s[:rem]: ', s[:rem])
        newCount += Counter(s[:rem])['a']
        # print('Additional number of a is ', newCount)    
        return newCount
    else:
        return n


if __name__ == '__main__':
    s = 'bab'
    n = 725261545450
    print(repeatedString(s,n))