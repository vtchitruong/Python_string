'''
Sample Input:
hello
l

Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
'''

text = input()
letter = input()

times = text.count(letter);
frequency = int(times  / len(text) * 100)
print(frequency)