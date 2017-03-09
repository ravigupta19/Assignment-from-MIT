s = 'azcbobobegghakl'
import string
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print('Number of vowels:' + str(count))


def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    shift_dict = {}
    alphabets = string.ascii_lowercase

    for letter in alphabets:
        indexAlphabet = (alphabets.index(letter) + shift) % 26
        shift_dict[letter] = alphabets[indexAlphabet]
        shift_dict[letter.upper()] = alphabets[indexAlphabet].upper()
    print(shift_dict)
build_shift_dict(1)