import csv
import os
import pickle

class Indexer:
    def __init__(self):
        self.F_index = {}
    def create_index(self, filename):
        self.F_index = {}
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                index = 0
                r = csv.reader(file)
                for row in r:
                    if row:
                        index += 1
                        for word in row:
                            if word not in self.F_index:
                                self.F_index[word] = [f"doc{index}"]
                            else:
                                if f"doc{index}" not in self.F_index[word]:
                                    self.F_index[word].append(f"doc{index}")

        with open('index.pkl', 'wb') as f:
            pickle.dump(self.F_index, f)
    def load(self, name):
        try:
            with open(name, 'rb') as f:
                self.F_index = pickle.load(f)
        except:
            self.F_index = {}
    def get(self):
        return self.F_index