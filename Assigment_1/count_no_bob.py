s = 'azcbobobegghakl'
count = 0
length = len(s)
n = 0
while n < length:
    sub_str = s[n:n+3]
    if sub_str == 'bob':
        count += 1
    n += 1
print('Number of times bob occurs is:' + str(count))