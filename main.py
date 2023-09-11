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

total_right = 0

with open('JEOPARDY_CSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)

    for row in csv_reader:
        questions.append((row[5], row[6], row[3], row[4]))


    while count != 0:
        random.shuffle(questions)
        print(questions[0][2], "--", questions[0][3])
        print(questions[0][0])
        x = input("")
        if x == questions[0][1]:
            amount = questions[0][3].replace("$", "")
            total_right += int(amount)
            print("Correct:", total_right)
            continue
        count -= 1
        print("Unfortunately, no, the correct answer is: " + questions[0][1])
        print("Correct:", total_right)





