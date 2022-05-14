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
    # dictionary where key is a document and value is the term frequency (tf)
    tf_dict = {}

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
                        current_tf_dict = self.index_dict[current_word]
                        if self.file_name in current_tf_dict:
                            doc_tf = current_tf_dict[self.file_name]
                            current_tf_dict[self.file_name] = doc_tf + 1
                        else:
                            current_tf_dict[self.file_name] = 1
                    else:
                        self.index_dict[current_word] = {self.file_name: 1}

    def set_file_name(self, file_name):
        self.file_name = file_name

    def print(self):
        for word in self.index_dict:
            print(word + ":")
            print(self.index_dict[word])
            print()

    def __init__(self):
        super().__init__()
        project_name = 'repository'
        html_dir = os.path.join(project_name)
        for root, dirs, files in os.walk(html_dir):
            for file in files:
                if file.endswith('.html'):
                    self.set_file_name(os.path.join(root, file))
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as html_file:
                        html_string = html_file.read()
                        # feed the HTML to words parser
                        self.feed(html_string)

