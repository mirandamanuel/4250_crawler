from indexer import Index

class retrieval():
    
    def __init__(searchWords, index):
        ''' use Index instance as its argument'''
        searchWords.index = index
        searchWords.results = []

    
    def search(searchWords, search_type = 'AND'):
        ''' search for term based on search type
        (only AND operator is required for this assignment)'''
        
        # get user input
        query = input("Please enter your query: ").lower()
        
        # clear results
        searchWords.results = []
        
        # process term
        terms = query.split(" ")
        
        # get indexes and turn lists into sets of documents
        file_index = searchWords.index.get_index()
        for i in file_index:
            file_index[i] = set(file_index[i])
        
        # perform set operations
        result_set = set()
        for term in terms:
            if term in file_index:
                if len(result_set) != 0:
                    result_set = result_set & file_index[term]
                else:
                    result_set = file_index[term]

        # print out results (unsorted)
        if search_type =='AND':
            
            searchWords.results = list(result_set)
            result = "Relevant results are: "
            for doc in searchWords.results:
                result += doc + " "                
        print(result)
   
#search from these files
foundIndex = Index()
foundIndex.create_index("A1/output/frequentWords(cpp).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()

foundIndex.create_index("A1/output/frequentWords(gmarket).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()

foundIndex.create_index("A1/output/frequentWords(tudn).csv")
SearchWord = retrieval(foundIndex)
SearchWord.search()