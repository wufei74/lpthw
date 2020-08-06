#Counting Lines

from sys import argv

script, input_file=argv
line_count = 0 #Set the initial lines to zero
print(f"We are going to count how many lines are in the file {input_file}.")

#First we open the file provided via arguments
#open_file = open(input_file)

#Then we read the contents of the file and set it to a variable
#file_content = open_file.read()
#Do we even need the previous step?

#Next lets iterate through the file and count how many lines there are
with open(input_file) as f:
    for line in f:
        line_count += 1
        stripped_line = line.strip()
        print(stripped_line)


print(f"There are {line_count} lines in the file {input_file}.")
