#!/usr/bin/env python

"""
Use covariance data to generate distance values
"""

import math

class VectorData:
    def __init__(self, raw_vectors):
        self.total_count = 0
        self.vector_data = raw_vectors
        self.term_counts = self.get_counts()
    def get_counts(self):
        count_dict = {}
        for entry in self.vector_data:
            occurences = 0
            for dim in entry['elements']:
                occurences += entry['elements'][dim]
            count_dict[entry['word']] = occurences
            self.total_count += occurences
        return count_dict
    def vec_entropy(self):
        term_ent = {}
        for entry in self.vector_data:
            hw = 0
            for elem in self.vector_data['elements']:
                px = float(self.term_counts[elem])/(2*self.total_count)
                wi = px * math.log(px, 2)
                hw -= wi
            ent_dict[entry] = {elem : { 'px' : px, 'hw' : hw } } 
        return ent_dict
    def v_information(self):
        v_info = {}
        vec_ent = self.vec_entropy()
        for entry in self.vector_data:
            v_info[entry] = {}
            for dim in entry['elements']:
                cooc = entry['elements'][dim]
                if v_info.has_key(cooc) and v_info[cooc].has_key(entry):
                    pass
                else:
                    pxy = float(cooc)/self.total_count
            #        ixy = pxy * math.log((pxy/(vec




if __name__ == '__main__':

    from pymongo import Connection

    connection = Connection('localhost', 27017)
    db = connection.simplicial_semantics
    raw_counts = db.row_vecs.find()
    collection = db.tfidf_vecs
    
    #vec_data = VectorData(raw_counts)
    for obj in raw_counts:
        print obj['word'], len(obj['elements'])



