from bs4 import BeautifulSoup
import lxml
import re
import os


def parse(path, file):
    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}

    with open("{}{}".format(path, file), encoding='utf8') as data:
        soup = BeautifulSoup(data, "lxml")

    # print(soup.prettify())
    # links = soup.find(id='bodyContent').find_all(True)
    # print('\n'.join([str(link) for link in links]))

    print('\t=========================\n\n')
    # find all tags a
    # find all parrents of these tags, and gather to the list
    # find first a tag of a parent
    # find all siblings (not only a)
    # count continuous a's
    parents_set = set()
    [parents_set.add(tag.find_parent()) for tag in soup.find('body').find_all('a') if tag]

    max_links_len = 1 if parents_set else 0

    # print('\n\t==PARENTS_SET==')
    # print('\n='.join(map(str, parents_set)))

    siblings_list = [parent.find('a', recursive=False).find_next_siblings() for parent in parents_set]
    link_re = re.compile(r'^<a .*')
    for siblings in siblings_list:
        if siblings:
            print('\n'.join(map(str, siblings)))
            links_len = 1
        else:
            continue
        for sibling in siblings:
            if link_re.match(str(sibling)):
                links_len += 1
            else:
                links_len = 0
            if max_links_len < links_len:
                max_links_len = links_len

        print(max_links_len)

    # print('\n\t==Siblings==')
    # print('\n'.join(map(str, [siblings for siblings in siblings_list if siblings])))
    #
    # print(max_links_len)
#     print(re.findall('<a[^>]+href="([^"]+)', file))
#
#     print([a['href'] for a in soup('a')])
#
#     print([a['href'] for a in soup.select('a[href]')])


if __name__ == '__main__':
    path = './'
    file = 'Python.html'
    parse(path, file)
