'''
Input
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Output
AB
CA
AD

t = AAB -> u = AB
t = CAA -> u = CA
t = ADA -> u = AD

'''

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        u = ''
        for c in string[i : i+k]:
            if c not in u:
                u += c
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
