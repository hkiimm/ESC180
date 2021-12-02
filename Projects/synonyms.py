'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    denominator = 0

    for i in vec1.keys():
        if i in vec2.keys():
            numerator += vec1[i] * vec2[i]

    denominator = norm(vec1) * norm(vec2)

    return numerator/denominator


def build_semantic_descriptors(sentences):
    semantic_descriptors = {}

    for sentence in sentences:
        for keyword in sentence:
            for word in sentence:
                if word != keyword:
                    if keyword not in semantic_descriptors:
                        semantic_descriptors[keyword] = {}
                    if word in semantic_descriptors[keyword]:
                        semantic_descriptors[keyword][word] += 1
                    else:
                        semantic_descriptors[keyword][word] = 1

    return semantic_descriptors


def build_semantic_descriptors_from_files(filenames):
    text = ""
    sentences = []
    sem_descript = {}

    for i in range (len(filenames)):
        text += open(filenames[i], "r", encoding="latin1").read().lower()
        text = text.replace(",", "").replace("-", " ").replace("--", " ").replace(":","").replace(";", "")
        text = text.replace("!", ".").replace("?", ".").split(".")

    for i in range (len(text)):
        sentences.append(text[i].split(" "))

    sem_descript = build_semantic_descriptors(sentences)

    return sem_descript

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass