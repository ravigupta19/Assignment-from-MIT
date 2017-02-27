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

    guessed = False
    low = 1
    high = num
    mid =  int((low + high) / 2)
    while not guessed:
        guessedExpotential


closest_power(3,12)