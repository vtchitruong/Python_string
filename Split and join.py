'''
Input:
this is a string

Output:
this-is-a-string
'''

def split_and_join(line):
    # write your code here
    string_list = line.split()
    res = "-".join(string_list)
    return res


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
