def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    List = []
    for i in aList:
        if isinstance(i,list):
            List.extend(flatten(i))
        else:
            List.append(i)
    return List

#List = []
aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

print(flatten(aList))

