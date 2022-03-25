from indexer import Index

class retrieval():
    
    def __init__(searchWords, index):
        
        searchWords.index = index
        searchWords.results = []

    
    def search(searchWords, search_type = 'AND'):
        
        
        # get user input
        query = input("Please enter your query: ").lower()
        
        # clear results
        searchWords.results = []
        
        
        terms = query.split(" ")
        
        # get the indexes and put them into doc
        indexFile = searchWords.index.getIndex()
        for i in indexFile:
            indexFile[i] = set(indexFile[i])
        
        #
        result_set = set()
        for term in terms:
            if term in indexFile:
                if len(result_set) != 0:
                    result_set = result_set & indexFile[term]
                else:
                    result_set = indexFile[term]

        # print out results
        if search_type =='AND':
            
            searchWords.results = list(result_set)
            result = "Relevant results are: "
            for doc in searchWords.results:
                result += doc + " "                
        print(result)
   
#search from these files
foundIndex = Index()
foundIndex.createIndex("output/frequentWords(cpp).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()

foundIndex.createIndex("output/frequentWords(gmarket).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()

foundIndex.createIndex("output/frequentWords(tudn).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()