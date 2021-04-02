import requests
import json

class Hero:

    def __init__(self, name):


    #def get_id(self, name):
        self.request = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name, timeout=(2, 2))
        self.text = self.request.text
        self.name = name
        text = self.text
        json_hero = json.loads(text)
        id_hero = (json_hero["results"][0]["id"])
        int_hero = (json_hero["results"][0]["powerstats"]["intelligence"])
        print(text)
        print (f'Имя героя: {name}, id героя: {id_hero}, мозги героя: {int_hero}')


        if "Hulk" or "Captain America" or "Thanos" == name:
            if  int(int_hero) > int(dict_heroes[0]):
                dict_heroes[0] = int_hero
                dict_heroes[1] = self.name

dict_heroes = {0: 0, 1: 'Anonimus'}

hero1 = Hero("Thanos")
hero2 = Hero("Captain America")
hero3 = Hero("Hulk")

print("Максимальный интелект равен " + dict_heroes[0] + " у героя " + dict_heroes[1])
