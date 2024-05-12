# Read the questions and answers from a text file
with open('scraped_data.txt', 'r') as file:
    content = file.readlines()

# Initialize an empty list to store the formatted content
formatted_content = []

# Initialize a variable to keep track of whether the previous line was part of a question
previous_line_was_question = False

# Loop through each line in the content
for line in content:
    # Strip any leading or trailing whitespace
    line = line.strip()
    # Check if the line is not empty and does not contain the word "advertisement"
    if line and "advertisement" not in line:
        # Append the line to the formatted content list
        formatted_content.append(line)
        # Update the variable to indicate that the current line is part of a question
        previous_line_was_question = True
    elif previous_line_was_question:
        # If the current line is empty and the previous line was part of a question,
        # append a single empty line to maintain spacing between questions
        formatted_content.append('')
        # Reset the variable to indicate that the next line is not part of a question
        previous_line_was_question = False

# Write the formatted content back to the text file
with open('formatted_questions.txt', 'w') as file:
    file.write('\n'.join(formatted_content))
