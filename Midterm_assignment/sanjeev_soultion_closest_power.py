def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    num = int(num)
    if num == 1:
        return 0
    if base > num:
        if abs(base - num) < abs(num - 1):
            return 1
        else:
            return 0

    copyNum = num
    count = 0
    while True:
        copyNum = int(copyNum/base)
        count += 1
        if copyNum < base:
            if(abs(num - (base ** count)) > abs(num - (base ** (count-1)))):
                return count-1
            else:
                return count
        elif copyNum == base:
            return count+1

print(closest_power(15,8.0))