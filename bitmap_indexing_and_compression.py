import os.path


def create_index(input_file, output_path, sorted=True):
    new_path = output_path + input_file

    file1 = open(input_file, "r")
    if file1.mode == "r":
        # read all contents of the input file
        file_content = file1.readlines()
        file1.close()
        # if sorted is true sort the input file first
        if sorted == True:
            file_content.sort()
            try:  # open the output file, if doesn't exist create it
                file2 = open(new_path + '_sorted', 'w', newline='')
            except IOError:
                file2 = open(new_path + '_sorted', 'w+', newline='')
        else:
            try:
                file2 = open(new_path, 'w', newline='')
            except IOError:
                file2 = open(new_path, 'w+', newline='')


        bitmap_index = None
        # loop through each line of the input file
        for element in file_content:
            element = element.split(',')  # split each element in the line by comma and save them as a list
            element[2] = element[2][:-1]  # get rid of the new line at the end
            bitmap_index = bitmapping(element)
            bitmap_index = bitmap_index + '\n'  # append new line at the end
            bitmap_index.rstrip()
            file2.writelines(bitmap_index)  # write the result of each line to output file
        file2.close()
        #return bitmap_index



def bitmapping(element):

    breed_index = '0000'
    age_index = '0000000000'
    adopted_index = '00'
    final_index = None
    if element[0] == 'bird':  # check each element of the list and return the corresponding bits
        breed_index = '0001'
    if element[0] == 'cat':
        breed_index = '1000'
    if element[0] == 'dog':
        breed_index = '0100'
    if element[0] == 'turtle':
        breed_index = '0010'
    if 1 <= int(element[1]) <= 10:
        age_index = '1000000000'
    if 11 <= int(element[1]) <= 20:
        age_index = '0100000000'
    if 21 <= int(element[1]) <= 30:
        age_index = '0010000000'
    if 31 <= int(element[1]) <= 40:
        age_index = '0001000000'
    if 41 <= int(element[1]) <= 50:
        age_index = '0000100000'
    if 51 <= int(element[1]) <= 60:
        age_index = '0000010000'
    if 61 <= int(element[1]) <= 70:
        age_index = '0000001000'
    if 71 <= int(element[1]) <= 80:
        age_index = '0000000100'
    if 81 <= int(element[1]) <= 90:
        age_index = '0000000010'
    if 91 <= int(element[1]) <= 100:
        age_index = '0000000001'
    if element[2] == 'True' or element[2] == 'Tru':
        adopted_index = '10'
    if element[2] == 'False' or element[2] == 'Fals':
        adopted_index = '01'
    final_index = breed_index + age_index + adopted_index

    return final_index

def compress_index(input_list, output_path, method, word_size):

    # perform compression on each column
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []
    column8 = []
    column9 = []
    column10 = []
    column11 = []
    column12 = []
    column13 = []
    column14 = []
    column15 = []
    column16 = []
    file2 = open(output_path + input_list + '_WAH' + '_' + str(word_size), "w+", newline='')
    file1 = open(input_list, "r")
    for line in file1:
        column1.append(line[0])
        column2.append(line[1])
        column3.append(line[2])
        column4.append(line[3])
        column5.append(line[4])
        column6.append(line[5])
        column7.append(line[6])
        column8.append(line[7])
        column9.append(line[8])
        column10.append(line[9])
        column11.append(line[10])
        column12.append(line[11])
        column13.append(line[12])
        column14.append(line[13])
        column15.append(line[14])
        column16.append(line[15])
        # perform compression on each column list and turn the result to a string
    temp1 = ''.join(map(str, compress_index_inner(column1, word_size)))

    temp2 = ''.join(map(str, compress_index_inner(column2, word_size)))
    temp3 = ''.join(map(str, compress_index_inner(column3, word_size)))
    temp4 = ''.join(map(str, compress_index_inner(column4, word_size)))
    temp5 = ''.join(map(str, compress_index_inner(column5, word_size)))
    temp6 = ''.join(map(str, compress_index_inner(column6, word_size)))
    temp7 = ''.join(map(str, compress_index_inner(column7, word_size)))
    temp8 = ''.join(map(str, compress_index_inner(column8, word_size)))
    temp9 = ''.join(map(str, compress_index_inner(column9, word_size)))
    temp10 = ''.join(map(str, compress_index_inner(column10,word_size)))
    temp11 = ''.join(map(str, compress_index_inner(column11, word_size)))
    temp12 = ''.join(map(str, compress_index_inner(column12, word_size)))
    temp13 = ''.join(map(str, compress_index_inner(column13, word_size)))
    temp14 = ''.join(map(str, compress_index_inner(column14, word_size)))
    temp15 = ''.join(map(str, compress_index_inner(column15, word_size)))
    temp16 = ''.join(map(str, compress_index_inner(column16, word_size)))
    # write the result to the output file and add a new line
    file2.writelines(temp1)
    file2.writelines('\n')
    file2.writelines(temp2)
    file2.writelines('\n')
    file2.writelines(temp3)
    file2.writelines('\n')
    file2.writelines(temp4)
    file2.writelines('\n')
    file2.writelines(temp5)
    file2.writelines('\n')
    file2.writelines(temp6)
    file2.writelines('\n')
    file2.writelines(temp7)
    file2.writelines('\n')
    file2.writelines(temp8)
    file2.writelines('\n')
    file2.writelines(temp9)
    file2.writelines('\n')
    file2.writelines(temp10)
    file2.writelines('\n')
    file2.writelines(temp11)
    file2.writelines('\n')
    file2.writelines(temp12)
    file2.writelines('\n')
    file2.writelines(temp13)
    file2.writelines('\n')
    file2.writelines(temp14)
    file2.writelines('\n')
    file2.writelines(temp15)
    file2.writelines('\n')
    file2.writelines(temp16)
    file2.writelines('\n')

    #final_list = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13\
    #+ temp14 + temp15 + temp16
    #return final_list


def compress_index_inner(input_list, word_size):
    # max_run stands for the max number of runs a given word size can hold
    max_run = 0
    if word_size == 8:
        max_run = 63
    if word_size == 16:
        max_run = 16383
    if word_size == 32:
        max_run = 1073741823
    if word_size == 64:
        max_run = 4611686018427387903

    final_list = []  # result to be returned
    temp_list = []   # word size - 1 bits to be compressed
    right_index = 1
    first_count = 0
    zero_run_prefix = ['1', '0']
    one_run_prefix = ['1', '1']
    num_all_ones_list = []
    left_over_runs_list = []

    zero_run = 0
    one_run = 0
    build_word = []  # word that's currently being built
    first_count = 0
    run_counter = 0
    literal_counter = 0

    right_end = word_size * right_index - 1
    left_end = 0

    while left_end <= len(input_list):  # loop through all elements in the list(column)
        right_index += 1
        # print("right and left:" + str(right_end) + " " + str(left_end))
        for x in range(left_end, right_end):
            # print(x)
            if x >= len(input_list):  # read 7 bits each time
                break
            try:
                temp_list.append(input_list[x])
            except IndexError:
                continue  # this is when the left over bits are less than word size - 1

        if temp_list != build_word and first_count != 0: # if what we read in is different than the currently built word
            # if there is all zeros in the build word, then we are building some runs of zeros
            if any(x == '0' for x in build_word):

                num_zero_run = to_binary(zero_run)  # number of zeros runs in binary representation
                # if the number of runs is greater than the max run
                if zero_run > max_run:
                    # first calculate how many runs we can represent in one word
                    left_over_runs = zero_run % max_run
                    # num_all_ones_list is all ones times the integer part of zero_run // max_run
                    num_all_ones_list = (zero_run_prefix + ['1'] * (word_size - 2)) * (zero_run // max_run)
                    # this list is the binary representation of how many runs we can represent in one word
                    temp_left_over_list = to_binary(left_over_runs)
                    # if we don't have anything left over, then the list is just empty
                    if left_over_runs == 0:
                        left_over_runs_list = []
                    else:
                        # left over list is 10 + how many zeros we need to fill up to the word size + binary representation
                        left_over_runs_list = zero_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                    final_list = final_list + num_all_ones_list + left_over_runs_list
                else:
                    # if number of runs is less than max run, then just do the same thing as above
                    final_list = final_list + zero_run_prefix + ['0'] * (
                            (word_size - 2) - (len(num_zero_run))) + num_zero_run
                # empty out zero runs and the currently building word
                zero_run = 0
                build_word = []
            if any(x == '1' for x in build_word):

                num_one_run = to_binary(one_run)

                if one_run > max_run:
                    left_over_runs = one_run % max_run
                    num_all_ones = one_run - left_over_runs
                    num_all_ones_list = (one_run_prefix + ['1'] * (word_size - 2)) * (one_run // max_run)
                    temp_left_over_list = to_binary(left_over_runs)
                    if left_over_runs == 0:
                        left_over_runs_list = []
                    else:
                        left_over_runs_list = one_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                    final_list = final_list + num_all_ones_list + left_over_runs_list
                else:
                    final_list = final_list + one_run_prefix + ['0'] * ((word_size - 2) - (len(num_one_run))) + num_one_run
                one_run = 0
                build_word = []

        first_count = 1

        # if the bits we read in is all zeros or all ones and it's exactly word size - 1 in size
        if len(temp_list) > 0 and temp_list.count(temp_list[0]) == len(temp_list) and len(temp_list) == (word_size - 1):
            run_counter += 1
            # increment number of zero runs or one runs
            if any(x == '0' for x in temp_list):
                zero_run += 1
                build_word = temp_list

            if any(x == '1' for x in temp_list):
                one_run += 1
                build_word = temp_list
        # if the bits we read in is not all zeros or all ones but exactly word size - 1 in
        elif len(temp_list) == word_size - 1:

            literal_counter += 1
            if zero_run == one_run == 0:
                final_list = final_list + ['0'] + temp_list
                build_word = []
            else:

                if any(x == '0' for x in build_word):
                    num_zero_run = to_binary(zero_run)
                    if zero_run > max_run:
                        left_over_runs = zero_run % max_run
                        num_all_ones = zero_run - left_over_runs
                        num_all_ones_list = (zero_run_prefix + ['1'] * (word_size - 2)) * (zero_run // max_run)
                        temp_left_over_list = to_binary(left_over_runs)
                        if left_over_runs == 0:
                            left_over_runs_list = []
                        else:
                            left_over_runs_list = zero_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                        final_list = final_list + num_all_ones_list + left_over_runs_list
                    else:
                        final_list = final_list + zero_run_prefix + ['0'] * (
                                (word_size - 2) - (len(num_zero_run))) + num_zero_run
                    zero_run = 0
                    final_list = final_list + ['0'] + temp_list
                    build_word = []

                if any(x == '1' for x in build_word):
                    num_one_run = to_binary(one_run)
                    if one_run > max_run:
                        left_over_runs = one_run % max_run
                        num_all_ones = one_run - left_over_runs
                        num_all_ones_list = (one_run_prefix + ['1'] * (word_size - 2)) * (one_run // max_run)
                        temp_left_over_list = to_binary(left_over_runs)
                        if left_over_runs == 0:
                            left_over_runs_list = []
                        else:
                            left_over_runs_list = one_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                        final_list = final_list + num_all_ones_list + left_over_runs_list
                    else:
                        final_list = final_list + one_run_prefix + ['0'] * (
                                (word_size - 2) - (len(num_one_run))) + num_one_run
                    one_run = 0
                    final_list = final_list + ['0'] + temp_list
                    build_word = []
        # in this case, it must be a short literal
        else:
            literal_counter += 1
            if zero_run == one_run == 0 and temp_list != []:
                final_list = final_list + ['0'] + temp_list + ((word_size - 1) - len(temp_list)) * ['0']
            # literal_flag = 1
            else:
                if any(x == '0' for x in build_word):

                    num_zero_run = to_binary(zero_run)
                    if zero_run > max_run:
                        left_over_runs = zero_run % max_run
                        num_all_ones = zero_run - left_over_runs
                        num_all_ones_list = (zero_run_prefix + ['1'] * (word_size - 2)) * (zero_run // max_run)
                        temp_left_over_list = to_binary(left_over_runs)
                        if left_over_runs == 0:
                            left_over_runs_list = []
                        else:
                            left_over_runs_list = zero_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                        final_list = final_list + num_all_ones_list + left_over_runs_list
                    else:
                        final_list = final_list + zero_run_prefix + ['0'] * (
                                (word_size - 2) - (len(num_zero_run))) + num_zero_run
                    zero_run = 0
                    final_list = final_list + ['0'] + temp_list + ((word_size - 1) - len(temp_list)) * ['0']
                    build_word = []

                if any(x == '1' for x in build_word):
                    num_one_run = to_binary(one_run)
                    if one_run > max_run:
                        left_over_runs = one_run % max_run
                        num_all_ones = one_run - left_over_runs
                        num_all_ones_list = (one_run_prefix + ['1'] * (word_size - 2)) * (one_run // max_run)
                        temp_left_over_list = to_binary(left_over_runs)
                        if left_over_runs == 0:
                            left_over_runs_list = []
                        else:
                            left_over_runs_list = one_run_prefix + ['0'] * ((word_size - 2) - (len(temp_left_over_list))) + temp_left_over_list
                        final_list = final_list + num_all_ones_list + left_over_runs_list
                    else:
                        final_list = final_list + one_run_prefix + ['0'] * (
                                (word_size - 2) - (len(num_one_run))) + num_one_run
                    one_run = 0
                    final_list = final_list + ['0'] + temp_list + ((word_size - 1) - len(temp_list)) * ['0']
                    build_word = []
        # after each iteration, update left end and right end and empty the temp list
        left_end = right_end
        right_end = word_size * right_index - (1 * right_index)
        temp_list = []
    # print(str(final_list))
    #print(run_counter)
    #print(literal_counter)
    return final_list

# turns a integer to binary form without the first tow bits
def to_binary(num):

    temp = list(map(str, str(bin(num))))[2:]
    return temp


if __name__ == "__main__":
    create_index('animals.txt', 'write_up/', False)
    (compress_index('animals_sorted', 'new_test_result/', "WAH", 64))


