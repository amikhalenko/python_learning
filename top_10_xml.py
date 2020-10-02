
uniques = {}

def reading_xml(max_letters):
    import xml.etree.ElementTree as ET

    parser = ET.XMLParser(encoding = 'UTF-8')
    tree = ET.parse('files/newsafr.xml', parser)
    root = tree.getroot()
    news_list = root.findall('channel/item')
    for news in news_list:
        descript = news.find("description").text
        descs = descript.split(' ')

        for word in descs:
            if len(word) > max_letters:
                if word.lower() in uniques:
                    uniques[word.lower()] += 1
                else:
                    uniques[word.lower()] = 1

    return(uniques)

def top_N(max_letters, max_words):
    uniques = reading_xml(max_letters)

    list_d = list(uniques.items())

    list_d.sort(key=lambda item: item[1])
    list_d.reverse()

    new_list = list_d[:][0:max_words]

    for item in new_list:
        print('слово "%s" встречается %d раз' % (item[0], item[1]))

    return()

top_N(6, 10)