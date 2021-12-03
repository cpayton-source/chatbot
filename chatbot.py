#date library
from datetime import datetime
# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# All possible questions and answers
answers = {
        'Good Morning': 'Good Morning',
        'Good Night' : 'Good Night',
        'Hi': 'Hello',
        'What is your name?' : 'My name is Cameron Payton',
        'age' : '20 years old',
        'day' : datetime.today().date(),
        'time' : datetime.today().time(),
        'year' : datetime.today().year,
        'location' : 'Enter a place:   '
        }

print('Hello Welcome to my chatbot! Please ask a question or make a statement to start talking')
print('If you would like to stop, enter quit')
#Keep going until user wants to stop
while(True):
    # Get input from user
    question = input()

    # Get answers from bot dictionary
    questions = answers.keys()

    # If your done
    if question.lower() == 'quit':
        break
    elif question.lower() == 'location':

        # Get the location you would like to search for
        question = input(answers['location'])

        # entering the location name
        getLoc = loc.geocode(question)

        # printing address
        print(getLoc.address)

        # Coordinates
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        print('\n')

    # If the question was typed wrong
    elif not question in questions:

        # Look for the question in questions
        for possibleQuestion in questions:
            if question.lower() in possibleQuestion.lower():
                print(f'\nI do not understand, did you mean {possibleQuestion}?')
                a = input()
                if a.lower() == 'y' or a.lower() == 'yes':
                    print(f'\n{answers[possibleQuestion]}')
                    break
    else:
        print(f'\n{answers[question]}')
