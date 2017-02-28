def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for i in L:
        if isinstance(i,list):
            deep_reverse(i)
    return L
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print(L)