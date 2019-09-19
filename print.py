char = input('What character do you want to print? ')
num_str = input('Enter number of lines: ')
num_lines = int(num_str)

temp_char = ''
for i in range(num_lines):
    temp_char += char
    print(temp_char)

