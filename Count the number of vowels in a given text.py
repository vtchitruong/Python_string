# Counts the number of vowels in a given text

vowels = ['a', 'e', 'i', 'o', 'u']
s = input()
count = 0
for c in s:
    if c in vowels:
        count += 1
print(count)
