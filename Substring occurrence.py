'''
You have to print the number of times that the substring occurs
in the given string.

Input:
ABCDCDC
CDC

Output:
2

'''


def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string) - len(sub_string):
        find_position = string.find(sub_string, start)
        if find_position != -1:
            count += 1
            start = find_position + 1
        else:
            break
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
