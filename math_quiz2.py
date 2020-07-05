#!/usr/bin/env python3

'''
This program can be used to generate simple arithmetic quizes for kids.
You can customize this program to suit the kids's level of math skills.
For example, change the maximum number of trials or the range of numbers.

You can also limit the kind of arithemetics. By default, the program randomly
pick from one of the four operations (add, subtract, multiple, divide) for each 
quiz. You can modify the question_list to limit the choices. 
'''


import random


class MathQuiz():

    def __init__(self, quiz_cnt, max_trials, min_int, max_int, operation_list):

        self.quiz_cnt = quiz_cnt                      # Total number of quizzes 
        self.max_trials = max_trials                  # Maximum number of trials for a given quiz

        self.min_int = min_int                        # The minimum number used in the quiz
        self.max_int = max_int                        # The maximum number used in the quiz

        self.operation_list = operation_list               # The list of operations 


    def run(self):

        quiz_list = []                            # This holds the complete list of quizes
        answer_list = []                          # This holds the complete list of quizes

        print ("\n*** Math Quiz ***\n")

        for i in range(quiz_cnt):

            operation = random.choice(operation_list)    # Randomly select one of the operations from the list

            while True:

                a = random.randint(min_int, max_int)
                b = random.randint(min_int, max_int)

                if (operation == "/") and (a % b != 0):  # Ensure the division can be performed
                    continue

                if (operation == "-") and (a < b):       # Eliminate the possibility of negative answer
                    quiz = (b, operation, a) 
                else:
                    quiz = (a, operation, b) 

                if quiz not in quiz_list:
                    break                    # avoid duplicate quizs


            for j in range(max_trials):

                while True:
                    your_input = input("Quiz {} of {}: {} {} {} = ".format(i+1, quiz_cnt, quiz[0], quiz[1], quiz[2]))

                    try:
                        your_answer = int(your_input)
                        break
                    except:
                        print("please enter a number.")
                        continue

                if operation == "+":
                    correct_answer = quiz[0] + quiz[2]
                elif operation == "-":
                    correct_answer = quiz[0] - quiz[2]
                elif operation == "*":
                    correct_answer = quiz[0] * quiz[2]
                elif operation == "/":
                    correct_answer = int(quiz[0] / quiz[2])
                else:
                    raise RuntimeError('The system encountered a mysterious operation: {}'.format(operation))

                if your_answer == correct_answer:
                    break
                else:
                    print("please try again (attempt {} of {})".format(j+1, max_trials))

            print("")

            quiz_list.append(quiz)
            answer_list.append((correct_answer, your_answer))

        return quiz_list, answer_list

    def show_report(self, quiz_list, answer_list):

        print("\n*** Summary Report ***", end="\n\n")        

        for i in range(quiz_cnt):
            print ("{} {} {} = {} {}"     \
                .format(quiz_list[i][0], quiz_list[i][1], quiz_list[i][2], answer_list[i][0],     \
                "" if answer_list[i][0] == answer_list[i][1] else ("(your answered: " + str(answer_list[i][1]) + ")")))

        correct_cnt = len([x for x in answer_list if x[0] == x[1]])

        print("\nYou got {} correct out of {} questions.\n".format(correct_cnt, quiz_cnt))


if __name__ == "__main__":

    with open("math_quiz.ini", "rt") as f:
        lines = f.readlines()

    for line in lines:

        key = line.strip().split("=")[0].strip()
        value = line.strip().split("=")[1].strip()

        if key == "QUIZ_CNT":
            quiz_cnt = int(value)
        elif key == "MAX_TRIALS":
            max_trials = int(value)
        elif key == "MIN_INT":
            min_int = int(value)
        elif key == "MAX_INT":
            max_int = int(value)
        elif key == "OPERATIONS":
            operation_list = list(value)
            if set(operation_list).issubset({"+", "-", "*", "/"}) == False:
                raise RuntimeError('The system encountered a mysterious operation: {}'.format(operation))
        else:
            continue

    quiz = MathQuiz(quiz_cnt, max_trials, min_int, max_int, operation_list)
    
    quiz_list, answer_list  = quiz.run()

    quiz.show_report(quiz_list, answer_list)

