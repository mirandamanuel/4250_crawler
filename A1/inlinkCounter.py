from link import LinkFinder
import hashlib
import os


if __name__ == '__main__':
    path = r'repository\tudn.com'
    domain = 'https://www.tudn.com/'
    inlink_dict = {}    # {hash:[hash, hash...]}

    # generate dictionary for hash:links using report.csv
    hash_link_dict = {}
    with open(fr'{path}\report.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]   # skip the first line
        for line in lines:
            # print(line)
            page_url, _ = line.split(', ')
            hashed_url = hashlib.md5(page_url.encode()).hexdigest().upper()
            hash_link_dict[hashed_url] = page_url
    link_hash_dict = dict((v, k) for k, v in hash_link_dict.items())

    for file in os.listdir(path):
        if file.endswith('.html'):
            file_name = file.replace('.html', '')
            if file_name in hash_link_dict:
                # start counting
                with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                    html_string = f.read()

                    page_url = hash_link_dict[file_name]
                    finder = LinkFinder(domain, page_url)
                    finder.feed(html_string)
                    links = finder.page_links()

                    for link in links:
                        if link not in link_hash_dict:
                            # print(f'{link} has not been crawled yet')
                            pass
                        else:
                            hashed_link = link_hash_dict[link]
                            if hashed_link not in inlink_dict:
                                inlink_dict[hashed_link] = [file_name]
                            else:
                                inlink_dict[hashed_link].append(file_name)

            print(f'done with {file}')

    # print(inlink_dict)
    with open(os.path.join(path, 'tudn_inlink.csv'), 'w', encoding='utf-8') as f:
        for key in inlink_dict:
            # csv format: page X, page pointing to X, page pointing to X, ...
            f.write(f'{key},{",".join(str(vals) for vals in inlink_dict[key])}\n')
