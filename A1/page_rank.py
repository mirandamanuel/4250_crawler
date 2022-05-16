import hashlib
import math


def page_rank(path, inlink_csv, iterations):
    hash_num_dict = {}
    # generate dictionary for {hashed_links:num_of_outlinks} using report.csv
    with open(fr'{path}\report.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]   # skip the first line
        for line in lines:
            page_url, num = line.split(', ')
            hashed_url = hashlib.md5(page_url.encode()).hexdigest().upper()
            hash_num_dict[hashed_url] = int(num)

    inlink_dict = {}    # {hash:[hash, hash...]}
    with open(fr'{path}\{inlink_csv}', 'r', encoding='utf-8') as f:
        for line in f:
            page_hash, inlinks = line.split(',', 1)
            inlink_dict[page_hash] = inlinks.replace('\n', '').split(',')

    # start page rank
    # iteration 0
    PR = {}
    for page in hash_num_dict:
        PR[page] = 1 / len(hash_num_dict)
    print(f'iteration 0: {list(PR.values())[0:5]}')
    print(sum(list(PR.values())))

    # iteration 1~n
    # Try x iterations for now
    for i in range(iterations):
    # i = 0
    # last_result = PR.values()
    # while True:
        tmp_PR = PR.copy()
        for page in hash_num_dict:
            tmp_PR[page] = 0

            inlinks = inlink_dict.get(page)
            if inlinks:
                for inlink in inlinks:
                    tmp_PR[page] += PR[inlink] / hash_num_dict[inlink]   # sum of PR(v) / N_v
            else:   # if inlinks is None (i.e. No pages link to this page)
                tmp_PR[page] = 0

        PR = tmp_PR.copy()
        print(f'iteration {i + 1}: {list(PR.values())[0:5]}')
        print(sum(list(PR.values())))
        # i += 1
        #
        # if abs(list(PR.values())[0] - list(last_result)[0]) <= 0.000001:
        #     break


# def is_not_converged():
#     global perplexity
#
#     H = 0
#     for val in PR:
#         H += PR[val] * math.log(PR[val], 2)
#
#     perplexity.append(2 ** (-H))
#
#     if len(perplexity) < 5:
#         return True
#
#     count = 0
#     diff_elements = []
#
#     for i in range(len(perplexity) - 5, len(perplexity) - 1):
#         diff_elements.append(int(perplexity[i]) - int(perplexity[i + 1]))
#
#     for val in diff_elements[-4:]:
#         if val != 0:
#             return True
#         count += 1
#
#     if count == 4:
#         return False
#
#     return True


if __name__ == '__main__':
    path = r'repository\gmarket.co.kr'
    inlink_csv = 'gmarket_inlink.csv'
    iterations = 10
    page_rank(path, inlink_csv, iterations)


