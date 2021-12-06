#date library
from datetime import datetime
# importing geopy library
from geopy.geocoders import Nominatim
# To get a random fact
import randfacts
# Weather
from bs4 import BeautifulSoup
import requests

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# All Q&A for the convo: Basic small talk
convo = {
        'Good Morning': 'Good Morning',
        'Good Night' : 'Good Night',
        'Hi': 'Hello',
        'name?' : 'My name is Cameron Payton',
        'age' : '20 years old',
        'day' : datetime.today().date(),
        'time' : datetime.today().time(),
        'year' : datetime.today().year,
        'fact' : randfacts.get_fact(),
        'location' : 'KnowItAll: Enter a place:   ',
        'weather'  : 'KnowItAll: Enter a place:   ',

        }
        #'formulas' : 'geometry, algebra, or trigonometry?'
 #-------------------Code by adityatri-------------------
 #https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
 #----------------------------------------------------------------

print('KnowItAll: Hello Welcome to my CamBot! What would you like from me?')
print('KnowItAll: If you would like to stop talking, enter quit')

#Keep going until user wants to stop
while(True):
    # Get input from user
    question = input("Human: ")

    # Get answers from bot dictionary
    questions = convo.keys()

    # Different types of maths
    #form = formulas.keys()

    # If your done
    if question.lower() == 'quit' or 'quit' in question.lower():
        print("\nKnowItAll: Thanks for the chat!")
        break
    elif question.lower() == 'location' or 'location' in question.lower():
        # Get the location you would like to search for
        question = input(convo['location'])
        # entering the location name
        getLoc = loc.geocode(question)
        # printing address
        print(getLoc.address)
        # Coordinates
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        print('\n')
    elif question.lower() == 'weather' or 'weather' in question.lower():
        city = input(convo['weather'])
        city = city + " weather"
        weather(city)
        # If the question was typed wrong
    elif question.lower() == 'fact' or 'fact' in question.lower():
        fac = randfacts.get_fact()
        print(f'\nKnowItAll: {fac}')
    elif not question in questions:
        # Look for the question in questions
        flag = False
        for possibleQuestion in questions:
            if question.lower() in possibleQuestion.lower() or possibleQuestion.lower() in question.lower():
                print(f'\nKnowItAll: {convo[possibleQuestion]}')
                flag = True
                break
        if flag == False:
            print(f'\nKnowItAll: Possible choices are {questions}. Run program again')
    else:
        print(f'\nKnowItAll: {convo[question]}')



#print(f'\nKnowItAll: I do not understand, did you mean {possibleQuestion}?')
#a = input()
#if a.lower() == 'y' or a.lower() == 'yes':

        '''
        if(question == 'formulas'):
            answer = input('What kind of math do you need help on?')
            # If the user entered incorrectly
            if not answer in formulas:
                flag = True
                for i in formulas:
                    if answer.lower() in i:
                        print(f'\nI do not understand, did you mean {i}?')
                        a = input()
                        if a.lower() == 'y' or a.lower() == 'yes':
                            print(f'\n{formulas[i]}')
                            flag = False
                            break
                            if flag == False:
                                print(f'Possible choices are {form}. Run program again')

                #f = input(f'\n{}?')
                '''
'''
# Displays geometry and algebra formulas
formulas = {
        'geometry': 'Area of a circle, circumference, area of a rectangle, or distanced?',
        'algebra' : 'linear, quad, or pythagorean theoream',
        'trigonometry' : 'tan, cot, sin, cos, csc, or sec?'
}

# Formulas for geometry
geometry = {
        'area of a circle': 'Pi * (Radius ^ 2)',
        'circumference': 'Pi * Diameter',
        'area of a rectangle': 'Length * Width',
        'distance': 'Rate * Time'
}
# Formulas for alegebra
algebra = {
    'linear' : 'y = mx+b',
    'quad' : 'x=−b±√(b2−4ac)/(2a)',
    'pythagorean theoream' : 'a^2 + b^2 = c^2',
}

# Formulas for trigonometry
trigonometry = {
        'tan':'opposite/adjacent or sin/cos',
        'cot':'adjacent/opposite or cos/sin',
        'sin':'opposite/hypotenuse or 1/cos',
        'cos':'adjacent/hypotenuse or 1/sec',
        'csc':'hypotenuse/opposite or 1/sin',
        'sec':'hypotenuse/opposite or 1/cos'
}
'''
