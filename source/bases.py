#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number
    # return int(str_num, base)
    sum = 0
    for index, digit in enumerate(str_num):
        try:
            sum += int(digit) * base ** (len(str_num) - 1)
        except:
            sum += (ord(digit.lower()) - 87) * base ** (len(str_num) - 1)
    return int(str_num, base)

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number

    largest_value = 0
    count = 0
    while largest_value <= num:
        count += 1
        largest_value = base ** count

    largest_power = count - 1
    result = ""
    digit = 0
    for count2 in range(largest_power + 1):
        digit = num / (base ** (largest_power - count2))
        if digit > 9:
            digit = chr(digit + 87)
            print(digit)
        result += str(digit)
        num = num % (base ** (largest_power - count2))
    print("result:", result)
    return result

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number
    base_ten = decode(str_num, base1)
    result = encode(base_ten, base2)
    return result
    
def main():
    import sys
    print(decode('02021',3))
    # args = sys.argv[1:]  # Ignore script file name
    # if len(args) == 3:
    #     str_num = args[0]
    #     base1 = int(args[1])
    #     base2 = int(args[2])
    #     result = convert(str_num, base1, base2)
    #     print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    # else:
    #     print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
