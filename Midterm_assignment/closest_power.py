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
    if num == 1:
        return 0
    low = 1
    high = num
    mid =  int((low + high) / 2)
    lowestDiff = num
    while True:
        exponential = mid
        res = base ** exponential
        diff = abs(res - num)
        if res == num:
            break
        elif res > num:
            if diff > lowestDiff:
                high = mid
            else:
                break
        elif res < num:
            if diff > lowestDiff:
                low = mid
            else:
                break
        mid = int((low + high)/2)
    return exponential

print(closest_power(3,12))

