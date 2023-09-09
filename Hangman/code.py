import collections
import random
import string
from random import choice

answer = []

i=0


def get_random_string(length):
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length))
    return result

length = int(input('enter the length of word: '))
question = get_random_string(length)   

def convert(question):
    puzzle = []
    puzzle[:0]=question
    return puzzle    

tries = int(input('Enter the number of tries: '))

while i<tries: 
    i += 1   
    user = input(f'{i}= Guess_The_Letters: ')  
    if user in question:
        answer.append(user)
        answer = list(dict.fromkeys(answer))
        
        
    else:
       print('guess again')
       
list = convert(question)

if collections.Counter(answer) == collections.Counter(list):
    print(f'well done  you found the correct word {question}')
else:
    print(f'wrong answer, correct answer is {question}')
