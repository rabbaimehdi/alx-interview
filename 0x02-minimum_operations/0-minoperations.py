def minOperations(n):
    """ """
    number_of_op = 0
    if (n % 2 == 1):
        number_of_op = n
    else:
        a=0
        while(n%2 ==0):
            n = n//2
            if (n == 1):
                n = 0
                a+=1
                break
            else:
                a += 1
        number_of_op = n + 2 * a
    return number_of_op