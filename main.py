import csv
import random


# with open('JEOPARDY_CSV.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_file)
#
#     for row in csv_reader:
#
#         while True:
#             print(row[5])
#             x = input("")
#             if x == row[6]:
#                 print("correct!")
#                 break
#             raise NameError


questions = []
count = 1

with open('JEOPARDY_CSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)

    for row in csv_reader:
        questions.append((row[5], row[6]))

    while count != 0:
        random.shuffle(questions)
        print(questions[0][0])
        x = input("")
        if x == questions[0][1]:
            print("correct")
            continue
        count -= 1
        print("Unfortunately, no, correct answer is: " + questions[0][1])


