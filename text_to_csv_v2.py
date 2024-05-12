import csv

# Function to read the questions and answers from the text file
def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        question = {}
        for line in lines:
            if line.strip():
                if line.startswith("View Answer"):
                    question['answer'] = line.split(":")[-1].strip()
                    questions.append(question)
                    question = {}
                elif line.strip().startswith(tuple('123456789')):
                    question['question'] = line.strip()
                elif line.strip().startswith("a)"):
                    question['a'] = line.strip()[3:]
                elif line.strip().startswith("b)"):
                    question['b'] = line.strip()[3:]
                elif line.strip().startswith("c)"):
                    question['c'] = line.strip()[3:]
                elif line.strip().startswith("d)"):
                    question['d'] = line.strip()[3:]
                elif line.startswith("Explanation"):
                    question['explanation'] = line.split(":")[-1].strip()
    return questions

# Function to write the questions and answers to a CSV file
def write_questions_to_csv(questions, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Answer', 'Explanation'])
        for question in questions:
            writer.writerow([question['question'], question.get('a', ''), question.get('b', ''), 
                             question.get('c', ''), question.get('d', ''), question['answer'], question.get('explanation', '')])

# Path to the text file containing questions and answers
file_path = 'formatted_questions.txt'

# Read questions from the text file
questions = read_questions_from_file(file_path)

# Path to the output CSV file
csv_file = 'questions.csv'

# Write questions to the CSV file
write_questions_to_csv(questions, csv_file)

print("Conversion completed successfully!")
