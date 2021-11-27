'''
Average Word Length

To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5
'''

text = input()
words = text.split()
text_length_without_space = len(text) - text.count(' ')
average_word_length = text_length_without_space / len(words)
print(average_word_length)