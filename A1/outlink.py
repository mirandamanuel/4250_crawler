import math
import operator

path = '/Users/shaghikissakhanian/Desktop/A2/lib/repository/co.kr/report.csv'
output = '/Users/shaghikissakhanian/Desktop/A2/lib/repository/co.kr/output.csv'

P = set()
inlinks = dict()
outlinks = dict()
sinks = set()
perplexity = list()

D = 0.85

PR = dict()


def main():
    global inlinks
    global outlinks
    global sinks
    global P
    global PR

    Dicts()
    N = len(P)

    for p in P:
        PR[p] = 1 / N

    newPR = dict()

    while isnotconverged():
        sinkPR = 0
        for p in sinks:
            sinkPR += PR[p]
        for p in P:
            newPR[p] = (1 - D) / N
            newPR[p] += D * sinkPR / N
            for q in inlinks[p]:
                if q in PR:
                    newPR[p] += D * PR[q] / len(outlinks[q])

        for p in P:
            PR[p] = newPR[p]

    count = 0
    for val in sorted(PR.items(), key=operator.itemgetter(1), reverse=True):
        if count > 499:
            return

        f = open(output, "a")
        f.write(str(PR[val[0]]) + " count: " + str(len(inlinks[val[0]])) + " " + str(val[0]) + "\n")
        f.close()

        count += 1


def Dicts():
    global P
    global inlinks
    global outlinks
    global sinks

    count = set()
    f = open(path, "r")
    alllines = f.readlines()

    for eachlinewithend in alllines:
        eachline = eachlinewithend.replace("\n", "")
        links = eachline.split(" ")
        setoflinks = set(links[1:])
        count.add(links[0])

        inlinks[links[0]] = set([link for link in links[1:] if link != ""])
        P.add(links[0])

        for link in setoflinks:
            if link == "":
                continue
            else:
                if link not in outlinks:
                    outlinks[link] = {links[0]}
                else:
                    outlinks[link].add(links[0])

    setlinks = set(outlinks.keys())
    sinks = count - setlinks


def isnotconverged():
    global perplexity

    H = 0
    for val in PR:
        H += PR[val] * math.log(PR[val], 2)

    perplexity.append(2 ** (-H))

    if len(perplexity) < 5:
        return True

    count = 0
    diffelements = []

    for i in range(len(perplexity) - 5, len(perplexity) - 1):
        diffelements.append(int(perplexity[i]) - int(perplexity[i + 1]))

    for val in diffelements[-4:]:
        if val != 0:
            return True
        count += 1

    if count == 4:
        return False

    return True


if __name__ == '__main__':
    main()
