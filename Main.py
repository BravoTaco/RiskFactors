import FileHandler as File_Handler
import StringUtilities as String_Util


def ask_question(question):
    print (question)
    return input("Input: ")


file_contents = False

while not file_contents:
    file_path = ask_question("Please input the file location.")
    file_contents = File_Handler.retrieve_file_contents(file_path)
    if not file_contents:
        print ("File not found. Please check that you have entered the correct path. Entered path: [" + file_path + "]")
        try_again = ask_question("Would you like to try and enter the file path again? (Y) || (N)")
        if try_again != 'Y' and try_again != 'y':
            quit(1)

file_contents = file_contents.replace('%', "")
split_contents = file_contents.split('\n')

state_objects = []

try:
    state_objects = String_Util.initialize_states(String_Util.filter_state_information(split_contents))
except ValueError:
    print ("File is in an invalid format. Please fix the file before retrying.")
    quit(1)

min_max_values = String_Util.set_min_max_values(state_objects)

output_data = File_Handler.construct_columns(min_max_values)
print ("Organized the data, into columns and rows.")
print (output_data)
answer = ask_question("Would you like to save the data? (Y) || (N)")

if answer == 'Y' or answer == 'y':
    output_file_path = ask_question("Please input the location to save the file to.")
    output_file_path += "\\FinalRiskFactors.txt"
    File_Handler.save_file(output_file_path, output_data)
    print ("Saved file to [" + output_file_path + "]")

print ("Program has ended.")
