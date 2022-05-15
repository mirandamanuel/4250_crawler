import indexer
from collections import OrderedDict
from operator import itemgetter
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


def ranked_bool(index):
    query = input("Please enter your query: ").lower()
    result = sorted(evaluate(index, query).items(), key=lambda x: x[1], reverse=True)
    return print(result)


def evaluate(index, query):
    result = {}
    # JACK AND JILL
    if query.find("(") == -1:
        terms = query.split(" ")
        print(terms)
        if "and" in terms[1]:
            print("correct op")
            if "not" in terms[2]:
                result = not_op(index[terms[0]], index[terms[3]])
                del terms[0]
                del terms[0]
                del terms[0]
                del terms[0]
            else:
                result = and_op(index[terms[0]], index[terms[2]])
                del terms[0]
                del terms[0]
                del terms[0]
        elif "or" in terms[1]:
            result = or_op(index[terms[0]], index[terms[2]])
            del terms[0]
            del terms[0]
            del terms[0]
        while terms:
            if "and" in terms[0]:
                if "not" in terms[1]:
                    result = not_op(result, index[terms[2]])
                    del terms[0]
                    del terms[0]
                    del terms[0]
                else:
                    result = and_op(result, index[terms[1]])
                    del terms[0]
                    del terms[0]
            elif "or" in terms[0]:
                result = or_op(result, index[terms[1]])
                del terms[0]
                del terms[0]
        return result
    # JACK AND (JILL OR RANDY)
    else:
        open_paren = query.find("(")
        close_paren = query.rfind(")")
        subquery = query[open_paren + 1:close_paren]
        terms = query.split(" ")
        if "and" in terms[1]:
            if "not" in terms[2]:
                return not_op(index[terms[0]], evaluate(index, subquery))
            else:
                return and_op(index[terms[0]], evaluate(index, subquery))
        elif "or" in terms[1]:
            return or_op(index[terms[0]], evaluate(index, subquery))


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
    indexer = indexer.Indexer()
    index = indexer.index_dict
    # indexer.print()
    ranked_bool(index)
