import requests
import json

print("*************************************************************")
print("             HMC NEWS WORLD        ")
print("**************************************************************\n")

query = input("What type of news are you interested in? \n")
# country = input("Which country would you prefer? \n")

url = f"https://newsapi.org/v2/everything?q={query}&apiKey=edf388bdc2e74343945371a2c5e476b6"
r = requests.get(url)
news = json.loads(r.text)
print("\n")
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["author"])
    print(article["source"]["name"])

    print("\n-------------------------------------------------------------------------------------\n")
