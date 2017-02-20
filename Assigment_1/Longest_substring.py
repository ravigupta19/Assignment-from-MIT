s = 'azcbobobegghakl'

current_acsii_val = 0
previous_acsii_val = 0
length = len(s)
cur_res_str = ''
pre_res_str = ''
current_count = 0
previous_count = 0
n = 0
res = ''
while n < length:
    if n == 0:
        previous_acsii_val = ord(s[n])
    current_acsii_val = ord(s[n])

    if current_acsii_val >= previous_acsii_val:
        cur_res_str += s[n]
        current_count += 1
    else:
        if current_count > previous_count:
            pre_res_str = cur_res_str
            previous_count = current_count
            cur_res_str = s[n]
            current_count = 1
        else:
            cur_res_str = s[n]
            current_count = 1
    previous_acsii_val = current_acsii_val
    n += 1
if pre_res_str == '' or len(cur_res_str) > len(pre_res_str):
    res = cur_res_str
else:
    res = pre_res_str

print('Longest substring in alphabetical order is: ' + res)