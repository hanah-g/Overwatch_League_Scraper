from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app = Flask(__name__)

# a list of Overwatch heroes, in order: tanks, damage, support
tankTags = ['orisa', 'reinhardt', 'winston', 'wreckingball', 'dva', 'roadhog',
            'sigma', 'zarya']
damageTags = ['ashe', 'bastion', 'mccree', 'reaper', 'soldier',
              'sombra', 'symmetra', 'tracer', 'widowmaker', 'doomfist', 'echo',
              'genji', 'hanzo', 'junkrat', 'mei', 'pharah', 'torbjorn']
supportTags = ['brigitte',
               'lucio', 'mercy', 'ana', 'baptiste', 'moira', 'zenyatta']


def getStats(tag):
    url = f'https://dashreset.com/hero/{tag}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # a list of the different categories and stats associated with each
    # can take each element of them in for loop and turn to text to display
    categories = soup.find_all('div', {'class': 'text-xs font-medium'})
    stats = soup.find_all('div', {'class': 'text-lg text-t1'})
    print(tag.capitalize())
    for item in categories:
        print(item.text)
    for item2 in stats:
        print(item2.text)


# for item in heroTags:
# getStats(item)
mode = input("What role do you want to look at? 'tank' 'damage' or 'support'. 'quit' to quit.")

while True:
    if mode == "quit":
        print("Overwatch and the Overwatch League ©2021 Blizzard Entertainment, Inc.")
        break
    if mode == "tank":
        for hero in tankTags:
            getStats(hero)
        mode = input("What do you want to do next?")
    elif mode == "damage":
        for hero in damageTags:
            getStats(hero)
        mode = input("What do you want to do next?")
    elif mode == "support":
        for hero in supportTags:
            getStats(hero)
        mode = input("What do you want to do next?")
    else:
        print("Invalid input.")
        mode = input("What do you want to do next?")
