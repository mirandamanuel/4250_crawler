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
    subqueries = []
    first_occ = query.find("(")
    last_occ = query.rfind(")")
    subquery = query[first_occ + 1:last_occ]
    print(subquery)



def and_op(term1_dict, term2_dict):
    result = {}
    for doc in term1_dict:
        if doc in term2_dict:
            result[doc] = min(term1_dict[doc], term2_dict[doc])
    return result


def or_op(term1_dict, term2_dict):
    result = {}
    for doc in term1_dict:
        if doc in term2_dict:
            result[doc] = term1_dict[doc] + term2_dict[doc]
        else:
            result[doc] = term1_dict[doc]
    for doc in term2_dict:
        if doc not in result:
            result[doc] = term2_dict[doc]
    return result


def not_op(term1_dict, term2_dict):
    result = {}
    for doc in term1_dict:
        if doc not in term2_dict:
            result[doc] = term1_dict[doc]
    return result


if __name__ == '__main__':
    # indexer = indexer.Indexer()
    # indexer.print()
    ranked_bool(indexer)
