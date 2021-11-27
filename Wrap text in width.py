'''
Wrap the string into a paragraph of width w.

Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''


import textwrap

def wrap(string, max_width):
    res = "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
