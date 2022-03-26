import indexer
from domain import *
import os

if __name__ == '__main__':
    PROJECT_NAME = 'repository'
    DOMAIN_NAME = get_domain_name('https://www.cpp.edu/')
    html_dir = os.path.join(PROJECT_NAME)

    indexer = indexer.Indexer()
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                indexer.set_file_name(os.path.join(root, file))
                with open(os.path.join(root, file), 'r', encoding='utf-8') as html_file:
                    html_string = html_file.read()
                    # feed the HTML to words parser
                    indexer.feed(html_string)


    query = input("Please enter your query: ").lower()
    while(query != "e"):
        index = indexer.get_index()

        args = query.split(" ")
        current_search_word = ""
        file_matches = {}
        word_count = 0
        result = set()
        # checks that all words exist in index
        for word in args:
            if word not in index:
                print(result)

            if word != "and":
                word_count += 1
                files = index[word]
                for file in files:
                    if file in file_matches:
                        prev_count = file_matches[file]
                        file_matches[file] = prev_count+1
                    else:
                        file_matches[file] = 1

        for match in list(file_matches):
            if file_matches[match] is word_count:
                result.add(match)

        print("Results are", result)
        query = input("Enter 'e' to exit, or enter another query:").lower()



