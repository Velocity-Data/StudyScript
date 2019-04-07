#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json

'''You need to change the following variables to use the 
text with the questions you would like to use.'''
test = 'A+'

'''This is the class which runs the question and answer scheme 
of the program and is the heart of the program. Changing this could 
have detrimental effects on the program and whether or not it works.'''
class Question:
    def __init__(self, question, answers, correctAnswer):
        self.question = question
        self.answers = answers
        self.correct = correctAnswer

    def askQuestion(self):
        print(self.question)

        for i in range(len(self.answers)):
            print('\t{}){}'.format(i, self.answers[i]))

        while True:
            try:
                answer = int(input('\nChoose your answer!>>> '))
                break
            except ValueError:
                print('Please type a number')
        return True if answer == self.correct else False

#This is the function which will calculate your final score.
def score_func():
    final_score = score / 63.0 * 100.0
    if final_score >= 75:
        print('You\'re killin it!')
        print("Your score is %d percent!" % final_score)
    elif final_score >= 51:
        print('You passed but you could do better!')
        print("Your score is %d percent!" % final_score)
    elif final_score < 50:
        print('You failed, really you need to study bro...')
        print("Your score is %d percent!" % final_score)
    else:
        print('Something went wrong with the calculation of your score.')

def ready():
    print(' ') 
    yn = input('Are you ready to get started?!(y or n)>>> ')
    print(' ')   
    if yn == 'y':
        print("OK, Let's get started!")
    elif yn == 'n':
        print("Alright, come back later.")
        quit()
    else:
        print("You didn't specify y or n y = yes and n = no... Try again.")
        ready()


score = 0
with open("{}.txt".format(test), 'rt') as finput:
    questions = [Question(**args) for args in json.load(finput)]


print(' ')
print('''Welcome to the {}.! This is an easy to use digital flash-card 
    program to help you study for the A+ Exams through your terminal or command 
    prompt. It is relatively easy to learn how use. A question will appear on the 
    screen, followed by a set of either multiple-choice or true and false answers. The 
    answers will be ordered from 0-2 or 0-3 or 0-4 rather then 1-2, 1-3, 1-4. Please 
    make sure to note the correct number for the answer you will choose then type it 
    in and hit enter, you will be told whether your answer was right or wrong then it 
    will continue to the next question and so on and so forth. At the end of the script 
    it will give you you're score as a percentage so you know if you did well or not.'''.format(test))
ready()
print(' ')
print('===================================================================================')
print('===================================================================================')
print(' ')

if __name__ == '__main__':
    for q in questions:
        if(q.askQuestion()):
            print('Correct! You\'re killin\' it!')
            score += 1
        else:
            print('You\'re wrong! You suck!!')

    score_func()
    print('You have completed this round of Study FlashCards.')
    quit()
