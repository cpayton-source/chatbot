# Weather
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
#date library
from datetime import datetime
# importing geopy library
from geopy.geocoders import Nominatim
import requests
import pycountry
# To get a random fact
import randfacts

# you have to get your api key from newapi.com and then paste it below
newsapi = NewsApiClient(api_key='a0c85a61ba84491da6e7fa9b0ac159ab')





# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
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


def getNews():
    input_country = input("Country: ")    # now we will take name of country from user as input
    input_countries = [f'{input_country.strip()}']
    countries = {}
    # iterate over all the countries in
    # the world using pycountry module
    for country in pycountry.countries:
        # and store the unique code of each country
        # in the dictionary along with it's full name
        countries[country.name] = country.alpha_2
    # now we will check that the entered country name is
    # valid or invalid using the unique code
    codes = [countries.get(country.title(), 'Unknown code')
             for country in input_countries]
    # now we have to display all the categories from which user will
    # decide and enter the name of that category
    option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
    # now we will fetch the new according to the choice of the user
    top_headlines = newsapi.get_top_headlines(
        # getting top headlines from all the news channels
        category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')
      # fetch the top news inder that category
    Headlines = top_headlines['articles']
       # now we will display the that news with a good readability for user
    if Headlines:
        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print(
                    f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
            else:
                print(
                    f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
    else:
        print(
            f"Sorry no articles found for {input_country}, Something Wrong!!!")
    option = input("Do you want to search again[Yes/No]?")
    if option.lower() == 'yes':
        getNews()
    else:
        print('What Else?')


 #----------------------------------------------------------------
# All Q&A for the convo: Basic small talk
convo = {
        'good morning': 'KnowItAll: Good Morning',
        'good night' : 'KnowItAll: Good Night',
        'hi': 'hello',
        'thank you': 'KnowItAll: You are very welcome!',
        'formulas' : 'What kind of math do you need help on?',
        'thanks': 'KnowItAll : You are very welcome!',
        'name?' : 'KnowItAll: My name is KnowItAll',
        'age' : 'KnowItAll: I have no age',
        'day' : datetime.today().date(),
        'time' : datetime.today().time(),
        'year' : datetime.today().year,
        'fact' : randfacts.get_fact(),
        'news' : 'KnowItAll: Enter a country',
        'location' : 'KnowItAll: Enter a place:   ',
        'weather'  : 'KnowItAll: Enter a place:   ',
        }
        #'formulas' : 'geometry, algebra, or trigonometry?'

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

print('KnowItAll: Hello Welcome! What would you like from me?')
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
    elif('formulas' in question.lower() or 'formula' in question.lower()):
        answer = input("geometry, algebra, or trigonometry? ")
        # If the user entered incorrectly
        if answer.lower() == 'geometry' or 'geometry' in answer.lower():
            print(f'KnowItAll: {geometry}')
        elif answer.lower() == 'algebra' or 'algebra' in answer.lower():
            print(f'KnowItAll: {algebra}')
        elif answer.lower() == 'trigonometry' or 'trigonometry' in answer.lower():
            print(f'KnowItAll: {trigonometry}')
        if not answer in formulas:
            # Look for the question in questions
            flag = False
            form = formulas.keys()
            for f in form:
                if answer.lower() in f or f in answer.lower():
                    if answer.lower() in 'geometry' or 'geometry' in answer.lower():
                        print(f'KnowItAll: {geometry}')
                        flag = True
                        break
                    elif answer.lower() in 'algebra' or 'algebra' in answer.lower():
                        print(f'KnowItAll: {algebra}')
                        flag = True
                        break
                    elif answer.lower() in 'trigonometry' or 'trigonometry' in answer.lower():
                        print(f'KnowItAll: {trigonometry}')
                        flag = True
                        break
                if flag == False:
                    print(f'\nKnowItAll: Possible choices are {formulas}. Run program again')
    elif question.lower() == 'weather' or 'weather' in question.lower():
        city = input(convo['weather'])
        city = city + " weather"
        weather(city)
        # If the question was typed wrong
    elif question.lower() == 'news' or 'news' in question.lower():
        print(convo['news'])
        getNews()
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

