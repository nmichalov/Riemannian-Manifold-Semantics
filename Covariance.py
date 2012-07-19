#!/usr/bin/env python


"""
Uses word co-occurence data from a previous project of mine to generate a covariance matrix.
"""

    
def get_coocs(cooc_file):
    vectors = {}
    infile = open(cooc_file, 'r')
    for line in infile:
        bigram, index = line.split()
        unigrams = bigram.split('/')
        for i in range(2):
            row, dimension = unigrams[i], unigrams[1-i]
            if vectors.has_key(row):
                if vectors[row].has_key(dimension):
                    vectors[row][dimension] = vectors[row][dimension] + 1
                else:
                    vectors[row][dimension] = 1
            else:
                vectors[row] = { dimension : 1 }
    infile.close()
    return vectors


if __name__ == '__main__':
    
    from pymongo import Connection
    
    vector_dict = get_coocs('bigrams.txt')
    connection = Connection('localhost', 27017)
    db = connection.simplicial_semantics
    collection = db.row_vecs
    for entry in vector_dict:
        entry = { 'word' : entry, 'elements' : vector_dict[entry] }
        collection.insert(entry)    

