
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
    low = 1
    high = num
    mid = int((low + high) / 2)
    lowestDiff = num
    counter = 0
    tempEx = 0
    while True:
        exponential = mid
        res = base ** exponential
        diff = abs(res - num)
        if diff == 0:
            break
        elif counter == 0 or (counter > 0 and diff < lowestDiff):
            lowestDiff = diff
            if res > num:
                high = mid
            else:
                low = mid
            mid = int((low + high) / 2)
            tempEx = exponential
        elif counter > 0 and diff >= lowestDiff:
            exponential = tempEx
            break
        counter += 1
    return exponential

print(closest_power(20, 210.0))



