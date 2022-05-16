import hashlib
import os


def page_rank(path, iterations):

    num_outlink_dict = {}   # {hash: int}
    with open(fr'{path}\num_of_outlink.csv', 'r', encoding='utf-8') as f:
        for line in f:
            page_hash, num = line.split(',')
            num_outlink_dict[page_hash] = int(num)

    inlink_dict = {}    # {hash:[hash, hash...]}
    with open(fr'{path}\inlink.csv', 'r', encoding='utf-8') as f:
        for line in f:
            page_hash, inlinks = line.split(',', 1)
            inlink_dict[page_hash] = inlinks.replace('\n', '').split(',')

    # start page rank
    # iteration 0
    PR = {}
    for page in num_outlink_dict:
        PR[page] = 1 / len(num_outlink_dict)
    print(f'iteration 0: {list(PR.values())[0:5]}...')
    print(f'    Sum: {sum(list(PR.values()))}')

    # iteration 1~n
    # for i in range(iterations):
    i = 0
    while True:
        last_result = PR.values()
        tmp_PR = PR.copy()
        for page in num_outlink_dict:
            tmp_PR[page] = 0

            inlinks = inlink_dict.get(page)
            if inlinks:
                for inlink in inlinks:
                    tmp_PR[page] += PR[inlink] / num_outlink_dict[inlink]   # sum of PR(v) / N_v
            else:   # if inlinks is None (i.e. No pages link to this page)
                tmp_PR[page] = 0

        PR = tmp_PR.copy()
        print(f'iteration {i + 1}: {list(PR.values())[0:5]}...')
        print(f'    Sum: {sum(list(PR.values()))}')
        i += 1

        # diff = abs(list(PR.values())[0] - list(last_result)[0])
        diff = max(abs(a - b) for a, b in zip(list(PR.values()), list(last_result)))
        print(f'    Max Diff: {diff}')
        if diff <= 0.000001:    # converge
            break

    return dict(sorted(PR.items(), key=lambda x: x[1], reverse=True))


def top_100(path, PR):
    # generate dictionary for hash:links using report.csv
    hash_link_dict = {}
    with open(fr'{path}\report.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]   # skip the first line
        for line in lines:
            # print(line)
            page_url, _ = line.split(', ')
            hashed_url = hashlib.md5(page_url.encode()).hexdigest().upper()
            hash_link_dict[hashed_url] = page_url

    with open(os.path.join(path, 'top100.csv'), 'w', encoding='utf-8') as f:
        for page in list(PR.keys())[:100]:
            f.write(f'{hash_link_dict[page]}, {PR[page]}\n')



if __name__ == '__main__':
    path = r'repository\cpp.edu'
    iterations = 20     # ignore
    PR = page_rank(path, iterations)
    top_100(path, PR)


