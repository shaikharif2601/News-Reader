# first install pyttsx3 module in your system (pip install pyttsx3) this module helps us to read the new

import pyttsx3

engine = pyttsx3.init()                     #setting the voice for the program.
voices = engine.getProperty('voices')       # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)  

rate = engine.getProperty('rate')
engine.setProperty('rate', 170)            # changing the rate of the voice
# engine.say("hello world")
engine.runAndWait()

if __name__ == '__main__':
    try:
        engine.say("Welcome to our news portal")
        print("\t*************************************Welcome to our news portal************************************")

        engine.say("press 1 to listen Top headlines from India")
        print("\n\tpress 1 to listen Top headlines from India")
        engine.say("press 2 to listen Top headlines from Google News")
        print("\n\tpress 2 to listen Top headlines from Google News")
        engine.say("press 3 to listen Top headlines from United States")
        print("\n\tpress 3 to listen Top headlines from United States")
        engine.say("press 4 to listen Top headlines from TechCrunch")
        print("\n\tpress 4 to listen Top headlines from TechCrunch")
        engine.say("press 5 to listen articles published by the Wall Street Journal")
        print("\n\tpress 5 to listen articles published by the Wall Street Journal")
        engine.say("enter you suggestion in the terminal :- ")
        engine.runAndWait()
    except Exception as ex:
        engine.say(ex)
        engine.runAndWait()
        print(ex)
x = int(input("\n\tenter you suggestion in the terminal :- "))

try:
    if x == 1:
        try:
            if __name__ == '__main__':
                import json
                import requests
                engine.say("Top headlines from India are :")
                print("\t\tTop headlines from India are :\n")
                url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1131990f881d4678b76f0f17cc9b02bd"
                response = requests.get(url)
                text = response.text
                my_jason = json.loads(text)
                arts = my_jason['articles']
                for article in arts:
                    print(article['title'])
                    engine.say(article['title'])
                    engine.runAndWait()
        except Exception as ex:
            print(ex)
            engine.say(ex)
            engine.runAndWait()
    elif x == 2:
        try:
            if __name__ == '__main__':
                import json
                import requests
                engine.say(" Top headlines from Google News are")
                print(" Top headlines from Google News are")
                url = 'https://newsapi.org/v2/everything?q=apple&from=2021-07-01&to=2021-07-01&sortBy=popularity&' \
                      'apiKey=1131990f881d4678b76f0f17cc9b02bd'
                response = requests.get(url)
                text = response.text
                my_jason = json.loads(text)
                arts = my_jason['articles']
                for article in arts:
                    print(article['title'])
                    engine.say(article['title'])
                    engine.runAndWait()
        except Exception as ex:
            print(ex)
            engine.say(ex)
            engine.runAndWait()

    elif x == 3:
        try:
            if __name__ == '__main__':
                import json
                import requests
                engine.say("Top headlines from United States")
                print("Top headlines from United States are")
                url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=1131990f881d4678b76f0f17cc9b02bd"
                response = requests.get(url)
                text = response.text
                my_jason = json.loads(text)
                arts = my_jason['articles']
                for article in arts:
                    print(article['title'])
                    engine.say(article['title'])
                    engine.runAndWait()
        except Exception as ex:
            print(ex)
            engine.say(ex)
            engine.runAndWait()

    elif x == 4:
        try:
            if __name__ == '__main__':
                import json
                import requests
                engine.say("Top headlines from TechCrunche")
                print("Top headlines from TechCrunche")
                url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&" \
                      "apiKey=583441f43bd64544abef5e190da8c372"
                response = requests.get(url)
                text = response.text
                my_jason = json.loads(text)
                arts = my_jason['articles']
                for article in arts:
                    print(article['title'])
                    engine.say(article['title'])
                    engine.runAndWait()
        except Exception as ex:
            print(ex)
            engine.say(ex)
            engine.runAndWait()

    elif x == 5:
        try:
            if __name__ == '__main__':
                import json
                import requests
                engine.say("articles published by the Wall Street Journal are")
                print("articles published by the Wall Street Journal are")
                url = "https://newsapi.org/v2/everything?domains=wsj.com&" \
                      "apiKey=583441f43bd64544abef5e190da8c372"
                response = requests.get(url)
                text = response.text
                my_jason = json.loads(text)
                arts = my_jason['articles']
                for article in arts:
                    print(article['title'])
                    engine.say(article['title'])
                    engine.runAndWait()
        except Exception as ex:
            print(ex)
            engine.say(ex)
            engine.runAndWait()
    else:
        if __name__ == '__main__':
            engine.say("wrong input")

except Exception as ex:
    engine.say(ex)
    engine.runAndWait()
    print(ex)
