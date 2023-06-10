'''
Sample Input
chris alan

Sample Output
Chris Alan
'''

def capitalize_first_letter(input_string):
    mystring_list = []
    mystring_list[:0] = input_string
    mystring_list_len = len(mystring_list)

    if mystring_list[0].isspace() is False:
        mystring_list[0] = mystring_list[0].upper()

    for i in range(1, mystring_list_len):
        if mystring_list[i - 1].isspace():
            mystring_list[i] = mystring_list[i].upper()

    n = "".join(mystring_list)
    return n

if __name__ == '__main__':
    MY_STRING = "hello  world lol"
    NEW_STRING = capitalize_first_letter(MY_STRING)
    print(NEW_STRING)