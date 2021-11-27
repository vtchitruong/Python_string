'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------



'''




import string

def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    l = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        l.append((s[::-1] + s[1:]).center(4*size - 3, '-'))
    print('\n'.join(l[:0:-1]+l))    




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
