# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.
# Задача №1

# Написать программу для файла в формате json.
# Задача №2.

# Написать программу для файла в формате xml.
def reading_json():
    import json

    uniques = []
    with open('files/newsafr.json', 'r', encoding ='utf-8') as f:
        data = json.load(f)
        for values_rss in data.values():
            values_channel = values_rss['channel']['items']

            for pair in values_channel:
                descs = pair['description'].split(' ')

                for word in descs:
                    if len(word) > 6:
                        uniques.append(word)
    return(uniques)

def top_10():
    counts = []
    uniques = reading_json()
    print(uniques)
    for unique in uniques:
        count = 0
        for word in uniques:
            if word == unique:
                count += 1
        if (count, unique) not in counts:
            counts.append((count, unique))

    counts.sort()
    counts.reverse()

    for i in range(0, 10):
        count, word = counts[i]
        print('слово "%s" встречается %d раз' % (word, count))
    return()
top_10()
