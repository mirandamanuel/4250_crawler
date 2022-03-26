from indexer import Indexer
class retrieval():

    def __init__(self, index):
        self.index = index
        self.results = []

    def search(self, type='AND'):
        query = input("Enter query: ").lower()
        self.results = []
        terms = query.split(" ")

        F_index = self.index.get()
        for i in F_index:
            F_index[i] = set(F_index[i])

        result = set()
        for term in terms:
            if term in F_index:
                if len(result) != 0:
                    result = result & F_index[term]
                else:
                    result = F_index[term]

        if type == 'AND':

            self.results = list(result)
            results = "Results: "
            for doc in self.results:
                results += doc + " "
        print(results)


index = Indexer()
index.create_index("output/frequentWords(cpp).csv")
ret = retrieval(index)
ret.search()

index.create_index("output/frequentWords(gmarket).csv")
ret = retrieval(index)
ret.search()

index.create_index("output/frequentWords(tudn).csv")
ret = retrieval(index)
ret.search()

