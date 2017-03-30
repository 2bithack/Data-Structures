def find(string, pattern):
    count = 0
    for char in string:
        if char == pattern[count]:
            count += 1
        else:
            count = 0
        if count == len(pattern):
            return True
    return False

def find_index(string, pattern):
    count = 0
    for index, char in enumerate(string):
        if char == pattern[count]:
            count += 1
        else:
            count = 0
        if count == len(pattern):
            return index - (count - 1)
    return None


def main():
    import sys
    args = sys.argv[1:]


if __name__ == '__main__':
    main()
