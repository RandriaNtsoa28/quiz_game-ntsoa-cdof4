# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:22:09 2024

@author: ASUS
"""

import json
import random

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
    "question": "What is the chemical symbol for the element gold?",
    "options": ["Au", "Ag", "Fe", "Hg"],
    "answer": "Au"
    },
    {
    "question": "The Great Wall of China was built during the Ming Dynasty.",
    "options": ["True", "False"],
    "answer": "True"
    },
    {
    "question": "Which country is the largest by land area?",
    "options": ["Russia", "Canada", "China", "United States"],
    "answer": "Russia"
    },
    {
    "question": "In basketball, the term 'slam dunk' was popularized by commentator _______.",
    "options": ["Chick Hearn", "Marv Albert", "Bill Russell", "Bob Costas"],
    "answer": "Chick Hearn"
    },
    {
    "question": "Who wrote the novel '1984'?",
    "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien"],
    "answer": "George Orwell"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        answer = int(input("Enter your answer (1-4): "))
        if question['options'][answer - 1] == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")
    return score

def main():
    #questions = load_questions("questions.txt")
    random.shuffle(questions)
    score = run_quiz(questions)
    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    main()
