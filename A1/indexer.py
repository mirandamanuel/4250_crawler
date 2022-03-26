from html.parser import HTMLParser
from domain import *
import collections
import os


class Indexer(HTMLParser):
    # tags to search text within
    search_tags = ['p', 'div', 'span', 'a', 'h1', 'h2', 'h2', 'h3', 'h4']

    # current tag
    current_tag = ''

    # index represented as dictionary
    index_dict = {}

    file_name = ''

    # handle starting tag
    def handle_starttag(self, tag, attr):
        # store current tag
        self.current_tag = tag

        # handle tag's data

    def handle_data(self, data):
        # make sure current tag matches search tags
        if self.current_tag in self.search_tags:
            # loop over word list within current tag
            for word in data.strip().split():
                # convert word to lowercase and filter characters
                current_word = word.lower()
                current_word = current_word.replace('.', '')
                current_word = current_word.replace(':', '')
                current_word = current_word.replace(',', '')
                current_word = current_word.replace('"', '')

                # filter words
                if (
                        len(current_word) >= 2 and
                        current_word[0].isalpha()
                ):
                    if current_word in self.index_dict:
                        current_list = self.index_dict[current_word]
                        current_list.add(self.file_name)
                    else:
                        self.index_dict[current_word] = {self.file_name}

    def get_index(self):
        return self.index_dict

    def set_file_name(self, file_name):
        self.file_name = file_name



if __name__ == '__main__':
    PROJECT_NAME = 'repository'
    DOMAIN_NAME = get_domain_name('https://www.cpp.edu/')
    html_dir = os.path.join(PROJECT_NAME)


    index = Indexer()
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                index.set_file_name(os.path.join(root, file))
                with open(os.path.join(root, file), 'r', encoding='utf-8') as html_file:
                    html_string = html_file.read()
                    # feed the HTML to words parser
                    index.feed(html_string)

    with open(os.path.join(PROJECT_NAME, 'index.csv'), 'w', encoding='utf-8') as f:
        for key in index.get_index().keys():
            print(key, str(index.get_index()[key]), sep=", ", file=f)

