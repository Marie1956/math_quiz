#!/usr/bin/env python3

'''
This program can be used to generate simple arithmetic quizes for kids.
You can customize this program to suit the kids's level of math skills.
For example, change the maximum number of trials or the range of numbers.

You can also limit the kind of arithemetics. By default, the program randomly
pick from one of the four operations (add, subtract, multiple, divide) for each 
quiz. You can modify the question_list to limit the choices. 
'''


from random import choice
import quiz


def read_config(config_file):

    with open(config_file, "rt") as f:
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
            diff = set(operation_list) - set(quiz.supported_operators().keys())
            if len(diff) > 0:
                raise RuntimeError('The config file contains unsupported operation(s): {}'.format(str(diff)))
        else:
            continue

    return {"QUIZ_CNT" : quiz_cnt,
            "MAX_TRIALS" : max_trials,
            "MIN_INT" : min_int,
            "MAX_INT" : max_int,
            "OPERATIONS" : operation_list}
            

def generate_report(record_list, quiz_cnt):
    
    report_lines = []
    
    report_lines.append("\n*** Summary Report ***\n\n")        

    for q, your_answer in record_list:

        if q.result != your_answer:
            wrong_answer ="(your answered: " + str(your_answer) + ")"
        else:
            wrong_answer = ""

        report_lines.append("{} {}\n\n".format(q.print(True), wrong_answer))

    correct_cnt = len([x for x in record_list if x[0].result == x[1]])

    report_lines.append("\nYou got {} correct out of {} questions.\n".format(correct_cnt, quiz_cnt)) 
    
    return report_lines


def display_report(report_lines):
    
    for line in report_lines:
        print(line)
        
        

def save_report(report_lines, report_file):
    
    with open(report_file, "wt") as f:
        f.writelines(report_lines)
        
      

def run_quiz(params):

    record_list = []                            # This holds the complete list of quizes

    print ("\n*** Math Quiz ***\n")

    for i in range(params.get("QUIZ_CNT")):

        operator = choice(params.get("OPERATIONS"))    # Randomly select one of the operations from the list

        q = quiz.create_quiz(operator, params.get("MIN_INT"), params.get("MAX_INT"))

        for j in range(params.get("MAX_TRIALS")):

            while True:

                your_input = input("Quiz {} of {}: {}".format(i+1, params.get("QUIZ_CNT"), q.print(False)))

                try:
                    your_answer = int(your_input)
                    break
                except:
                    print("please enter a number.")
                    continue

            if your_answer == q.result:
                break
            else:
                print("Failed attempt {} of {}".format(j+1, params.get("MAX_TRIALS")))

        print("")

        record_list.append((q, your_answer))


    return record_list



if __name__ == "__main__":
    
    params = read_config("math_quiz.ini") 
    
    record_list = run_quiz(params)
    
    report_lines = generate_report(record_list, params.get("QUIZ_CNT"))

    display_report(report_lines)
    
    save_report(report_lines, "quiz_report.txt")
