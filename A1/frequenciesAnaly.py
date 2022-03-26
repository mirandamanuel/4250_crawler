from matplotlib import pyplot as plt
import os

if __name__ == '__main__':
    ######### for Zipf's law ########
    # freq_list = []
    # total = 0
    #
    # path = r'repository\frequentWords_gmarket.co.kr.csv'
    # with open(path, 'r', encoding='utf-8') as f:
    #     for line in f:
    #         word, count = line.split(',')
    #         count = count.split(' ')[1]
    #         freq_list.append(int(count))
    #         total += int(count)
    #
    # prob_list = []
    # for item in freq_list:
    #     prob_list.append(item / total)
    #
    # plt.plot([x for x in range(len(prob_list))], prob_list)
    # plt.title('gmarket.co.kr')
    # plt.xlabel('Rank')
    # plt.ylabel('Probability')
    # plt.xlim(0)
    # plt.ylim(0)
    # plt.show()
    # # print(prob_list)

    ######### for Heap's law ########
    vocabulary_list = []
    collection_list = []

    path = r'repository\vocab_vs_col_gmarket.co.kr.csv'
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            unique_words, total_words = line.split(',')
            vocabulary_list.append(int(unique_words))
            collection_list.append(int(total_words))

    plt.plot(collection_list, vocabulary_list)
    plt.title('gmarket.co.kr')
    plt.xlabel('Words in Collection')
    plt.ylabel('Words in Vocabulary')
    plt.xlim(0)
    plt.ylim(0)
    plt.show()
