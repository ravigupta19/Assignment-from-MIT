d1 = {1:30, 2:20, 3:30, 5:80,7:20}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90,7:90}

def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    dict_intersect = {}
    dict_diff = {}
    return_tuple = (dict_intersect, dict_diff)
    diff_keys = (d1.keys() - d2.keys() | d2.keys() - d1.keys())
    if len(d1) > len(d2):
        iterate = d1
    else:
        iterate = d2
    for keys in iterate:
        if keys not in diff_keys:
            a = d1[keys]
            b = d2[keys]
            res = f(a, b)
            dict_intersect[keys] = res

    for key in diff_keys:
        if key in d1:
            dict_diff[key] = d1[key]
        else:
            dict_diff[key] = d2[key]
    return return_tuple
print(dict_interdiff(d1,d2))
