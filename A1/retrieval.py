import indexer
from domain import *
import os


def unranked_bool(indexer_instance):
    query = input("Please enter your query: ").lower()
    while query != "e":
        index = indexer_instance.index_dict
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
                        file_matches[file] = prev_count + 1
                    else:
                        file_matches[file] = 1

        for match in list(file_matches):
            if file_matches[match] is word_count:
                result.add(match)

        print("Results are", result)
        query = input("Enter 'e' to exit, or enter another query:").lower()


def ranked_bool(indexer_instance):
    query = input("Please enter your query: ").lower()



if __name__ == '__main__':
    indexer = indexer.Indexer()
    indexer.print()
    #ranked_bool(indexer)
