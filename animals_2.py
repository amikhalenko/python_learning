# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

#     гусей "Серый" и "Белый"
#     корову "Маньку"
#     овец "Барашек" и "Кудрявый"
#     кур "Ко-Ко" и "Кукареку"
#     коз "Рога" и "Копыта"
#     и утку "Кряква"

# Со всеми животными вам необходимо как-то взаимодействовать:

#     кормить
#     корову и коз доить
#     овец стричь
#     собирать яйца у кур, утки и гусей
#     различать по голосам(коровы мычат, утки крякают и т.д.)

# Задача №1

# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
# Задача №2

# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
# Задача №3

# У каждого животного должно быть определено имя(self.name) и вес(self.weight).

#     Необходимо посчитать общий вес всех животных(экземпляров класса);
#     Вывести название самого тяжелого животного.


class Animal:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
   
    def full(self):
        print('накормлен')

            
class Milk:
    def milk(self):
        print('подоена')

class Wool:
    def cut(self):
        print('подстрижен')

class Eggs:
    def collect(self):
        print('яйца собраны')

class Goose(Animal,Eggs):
    type_animal = 'гусь'

    def voice(self):
        print('гогочет')

    def info(self):
        print('Вид животного:',Goose.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.collect()
        self.voice()
        print('\n')

class Cow(Animal, Milk):
      type_animal = 'корова'

      def voice():
        print('мычит')

      def info(self):
        print('Вид животного:',Cow.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.milk()
        Cow.voice()
        print('\n')

class Sheeps(Animal, Wool):
      type_animal = 'овца'

      def voice():
        print('блеет')

      def info(self):
        print('Вид животного:',Sheeps.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.cut()
        Sheeps.voice()
        print('\n')

class Chickens(Animal, Eggs):
      type_animal = 'курица'

      def voice():
        print('кудахчет')

      def info(self):
        print('Вид животного:',Chickens.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.collect()
        Chickens.voice()
        print('\n')

class Goats(Animal, Milk):
      type_animal = 'коза'

      def voice():
        print('мекает')

      def info(self):
        print('Вид животного:',Goats.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.milk()
        Goats.voice()
        print('\n')

class Duck(Animal,Eggs):
    type_animal = 'утка'

    def voice(self):
        print('крякает')

    def info(self):
        print('Вид животного:',Duck.type_animal)
        print('Имя:',self.name)
        print('Вес:',self.weight,'кг')
        self.full()
        self.collect()
        self.voice()
        print('\n')

my_dict = {}

goose_1 = Goose('Белый', 6)
goose_1.info()
my_dict[goose_1.name] = goose_1.weight

goose_2 = Goose('Серый', 7)
goose_2.info()
my_dict[goose_2.name] = goose_2.weight

cow = Cow('Манька', 600)
cow.info()
my_dict[cow.name] = cow.weight

sheep_1 = Sheeps('Барашек', 50)
sheep_1.info()
my_dict[sheep_1.name] = sheep_1.weight

sheep_2 = Sheeps('Кудрявый', 55)
sheep_2.info()
my_dict[sheep_2.name] = sheep_2.weight

chicken_1 = Chickens('Ко-ко', 4)
chicken_1.info()
my_dict[chicken_1.name] = chicken_1.weight

chicken_2 =Chickens('Кукареку', 3)
chicken_2.info()
my_dict[chicken_2.name] = chicken_2.weight

goat_1 = Goats('Рога', 30)
goat_1.info()
my_dict[goat_1.name] = goat_1.weight

goat_2 = Goats('Копыта', 35)
goat_2.info()
my_dict[goat_2.name] = goat_2.weight

duck = Duck('Кряква', 6)
duck.info()
my_dict[duck.name] = duck.weight
print(my_dict)
def amount():
    amount = 0
    for i in my_dict:
        amount = amount + my_dict[i]
    return amount

def max_key():
    max_value = 0
    max_key = ''
    for key, value in my_dict.items():
        if max_value < value:
            max_value = value
            max_key = key  
    return max_key        
print('Суммарный вес животных: ', amount(),'\n','Самое увесистое животное: ', max_key(), sep='')