from bs4 import BeautifulSoup
import lxml
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    # bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    bridge = [end, start]
    # bridge = [start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file), encoding='utf8') as data:
            soup = BeautifulSoup(data, "lxml")

        # body = soup.find(id="bodyContent")
        print(soup.prettify())

        # TODO посчитать реальные значения
        # Количество картинок (img) с шириной (width) не меньше 200
        images = soup.find(id="bodyContent").find_all('img')
        image_count = len([image for image in images if int(image['width']) >= 200])
        # print(imgs)

        # Количество заголовков, первая буква текста внутри которого: E, T или C
        headers = soup.find(id='bodyContent').find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        header_re = re.compile(r'[ETC]')
        # Python way
        header_count = len(
            [header for header in headers for header_string in header.strings if header_re.match(str(header_string))])
        # print(header_count)

        # Длина максимальной последовательности ссылок, между которыми нет других тегов
        parents_set = set()
        [parents_set.add(tag.find_parent()) for tag in soup.find(id="bodyContent").find_all('a') if tag]
        links_len = max_links_len = 1 if parents_set else 0
        siblings_list = [parent.find('a', recursive=False).find_next_siblings() for parent in parents_set]

        link_re = re.compile(r'^<a.*')
        for siblings in siblings_list:
            if siblings:
                links_len = 1
            else:
                continue
            for sibling in siblings:
                if link_re.match(str(sibling)):
                    print(str(sibling))
                    links_len += 1
                else:
                    links_len = 0
                if max_links_len < links_len:
                    max_links_len = links_len

        print(max_links_len)

        # Количество списков, не вложенных в другие списки
        lists_list = soup.find(id="bodyContent").find_all(['ul', 'ol'])
        lists = len(lists_list)
        for tag in lists_list:
            if tag.find_parent().name in {'ul', 'ol', 'li'}:
                lists -= 1
        # print(lists)

        out[file] = [image_count, header_count, max_links_len, lists]
        # print(out)

        # print('##', headers[17])
        # print('##', headers[17].string)
        # print(headers[17].strings)
        # for string in headers[17].strings:
        #     print('===', string)
        # # u"The Dormouse's story"
        # # headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        # print('\n'.join([str(header) for header in headers]))
        # print('\n'.join([str(header.string) for header in headers]))



        # Normal way
        # header_count = 0
        # for header in headers:
        #     if header_re.match(str(header.string)):
        #         header_count += 1
        # print(header_count)

        # Python way
        # headers = len([header for header in headers if header_re.match(str(header.string))])
        # header_count = len([header_string for header_string in map(strings, [header for header in headers]) if header_re.match(str(header_string))])

# Normal way
        # header_count = 0
        # for header in headers:
        #     for header_string in header.strings:
        #         if header_re.match(str(header_string)):
        #             header_count += 1
        # print(header_count)

    return out


if __name__ == '__main__':
    start = 'Stone_Age'
    end = 'Python_(programming_language)'
    path = './wiki/'
    # print(build_tree(start, end, path))
    parse(start, end, path)