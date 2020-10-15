#
# Write the implementation for A2 in this file
#

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values
import math


def set_real(num,val):
    num[0] = val
def set_imaginary(num,val):
    num[1] = val

def get_real(num):
    return num[0]
def get_imaginary(num):
    return num[1]


def create_num(real, imaginary):
    """
    Gets a real and imaginary part and returns the corresponding complex number
    :param real: real part of the complex number
    :param imaginary: imaginary part
    :return: the complex number
    """
    num = []

    num.append(real)  # num[0] = real part
    num.append(imaginary)  # num[1] = imaginary part

    return num

def to_str(num):
    return str(get_real(num)) + '+' + str(get_imaginary(num)) + '*i'

def modulus(num):
    return math.sqrt(get_real(num)*get_real(num)+get_imaginary(num)*get_imaginary(num))

def add(num1,num2):
    return create_num(get_real(num1)+get_real(num2),get_imaginary(num1)+get_imaginary(num2))

def seq1(num_list):
    """
    Returns the longest sequence in which all numbers have modulus less than 10
    :param: num_list - list of complex numbers
    :return: maxseq - longest sequence as a list
    """
    maxseq = []
    seq = []

    for z in num_list:
        if modulus(z) <= 10: # checks if the modulus is less or equal to 10
            seq.append(z) # add z to current sequence
        else:
            if len(seq) > len(maxseq): # if modulus condition is not met, end the sequence, compare its length to the current longest one and start a new sequence
                maxseq = seq[:]
            seq.clear()

    if(len(seq) > len(maxseq)): # if in case the end of the sequence is the end of the list
        maxseq = seq[:]

    return maxseq

def seq2(num_list):
    """
    Returns the longest sequence in which consecutive number pairs have the same sum
    :param: num_list - list of complex numbers
    :return: maxseq - longest sequence as a list
    """
    maxseq = []
    seq = []
    seqsum = add(num_list[0],num_list[1]) # initalizes the sum of the current sequence to the sum of the first pair in the list

    for k in range (1, len(num_list)):
        for i in range(k,len(num_list),2): # step of 2 in order to get pairs
            z1 = num_list[i-1] # first number in current pair
            z2 = num_list[i] # second number in current pair
            sum = add(z1,z2)  # sum of the pair

            if sum == seqsum: # checks if the sum of the current pair is equal to the sum corresponding to the current sequence
                seq.append(z1)
                seq.append(z2)
            else:
                if len(seq) > len(maxseq): # if it's not equal then check if length of the current sequence is bigger than current maximum
                    maxseq = seq[:]
                seq.clear() # end current sequence
                seqsum = sum # start a new sequence by setting its corresponding pair sum to the sum of the current pair
                seq.append(z1)
                seq.append(z2) # add current pair to the new sequence

    if(len(seq) > len(maxseq)):
        maxseq = seq[:]

    return maxseq

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities

def seq1_ui(num_list):
    print("Longest sequence with property: the modulus of all elements is in the [0, 10] range ")
    seq = seq1(num_list)
    for z in seq:
        print(to_str(z))

def seq2_ui(num_list):
    print("Longest sequence with property: consecutive number pairs have equal sum ")
    seq = seq2(num_list)
    for z in seq:
        print(to_str(z))

def read_num():
    """
    Reads a complex number
    :return: a complex number or None if input is invalid
    """
    try:
        real = int(input("Input real part: "))
    except ValueError:
        return None

    try:
        imaginary = int(input("Input imaginary part: "))
    except ValueError:
        return None

    return create_num(real, imaginary)

def add_num_ui(num_list):

    while(True):
        num = read_num()
        if num == None:
            print("Invalid real or imaginary part")
            return
        num_list.append(num)

        cont = input("Input '-' to stop / '+' to continue ")
        if cont == '-':
            return


def display_numbers(num_list):
    for num in num_list:
        print(to_str(num))

def print_menu():
    print("1. Add a complex number: ")
    print("2. Display the list of complex numbers ")
    print("3. Display first sequence ")
    print("4. Display second sequence ")
    print("0. Exit")

def test_init(num_list):
    num_list.append(create_num(2,7))
    num_list.append(create_num(1,3))
    num_list.append(create_num(1,4))
    num_list.append(create_num(1,3))
    num_list.append(create_num(1,4))
    num_list.append(create_num(7,2))
    num_list.append(create_num(100,20))
    num_list.append(create_num(1,1))
    num_list.append(create_num(6,5))
    num_list.append(create_num(7,2))


def start():

    num_list = []
    test_init(num_list)

    command_dict = {'1': add_num_ui, '2': display_numbers, '3': seq1_ui, '4': seq2_ui}
    done = False

    while not done:
        print_menu()
        command = input("Enter command: ")

        if command == '0':
            done = True
        elif command not in command_dict:
            print("Invalid command")
        else:
            command_dict[command](num_list)
        print()

start()

