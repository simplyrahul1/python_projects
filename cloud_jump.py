'''
0 0 1 0 0 1 0
'''

def jump_cloud(input_num, input_string):
    my_list = []
    num_list = []
    my_list[:0] = input_string
    num_of_zero = 0
    last_cloud = "culmulus"
    next_cloud = ""
    jump_counter = 0
    next_move = [int(input_string[0])]
    my_list_len = len(my_list)
    num_list_index = 0

    print(f"my list length : {my_list_len} and my list : {my_list}")
    for n in range(0, my_list_len):
        if my_list[n] != " ":
            if my_list[n].isdigit():
              #print(f"my list element: {my_list[n]}")
              num_list.append(int(my_list[n]))

    print(f"my num list length : len(num_list) and my list : {num_list}")
    num_list_len = len(num_list)
    i = 1
    while i < num_list_len:
        #print(f"while {i}")
        #print(f"i: {i} , input_num: {num_list_len}")
        if num_list[i] == 0:
            current_cloud = "culmulus"
            #print("if0 ", num_list[i])
            if my_list[i+1] == 0:
                next_cloud = "culmulus"
                next_move.append(num_list[i+1])
                jump_counter += 1
                i = i + 2
                #print(f"if1 {num_list[i]}")
            else:
                next_cloud = "thunderheads"
                next_move.append(num_list[i])
                jump_counter += 1
                i = i + 1
                #print("if2", num_list[i])
        else:
            current_cloud = "thunderheads"
            i = i + 1
            #print("if3", num_list[i])

    #print(f"Moves : {next_move}")
    return jump_counter

if __name__ == '__main__':
    input_number_count = 7
    input_numbers = "0 0 1 0 0 1 0"
    counter = jump_cloud(input_number_count, input_numbers)
    print(f"Counter : {counter}")