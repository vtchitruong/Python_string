'''
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be n x m. (n is an odd natural number, and m is 3 times n.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Input:
9 27

Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''


n, m = [int(x) for x in input().split()]

pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
print("\n".join(pattern))

welcome = "WELCOME".center(m, "-")
print(welcome)

print("\n".join(pattern[::-1]))
