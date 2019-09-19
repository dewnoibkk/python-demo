char = input('What character do you want to print? ')
num_str = input('Enter number of lines: ')
num_lines = int(num_str)

########################################

temp_char = ''
for i in range(num_lines):
    temp_char += char

for i in range(num_lines):
    print(temp_char[0:(len(temp_char)-i)])

########################################

print()
for i in range(num_lines):
    num_print = num_lines - i
    temp_char = ''
    for j in range(num_print):
        temp_char += char
    print(temp_char)
