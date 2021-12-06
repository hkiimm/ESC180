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
        a = "C:/Users/hannahkim/Desktop/ESC180/ESC180/Projects/Project 3/" + filenames[i]
        text = open(a, "r", encoding="latin1").read().lower()
        text = text.replace(",", "").replace("--", " ").replace("-", " ").replace(":","").replace(";", "")
        text = text.replace("!", ".").replace("?", ".").split(".")

    for i in range (len(text)):
        sentences.append(text[i].split(" "))

    sem_descript = build_semantic_descriptors(sentences)

    return sem_descript


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    choice_similarity = [0]*len(choices)
    ind = 0

    if word in semantic_descriptors.keys():
        for i in range (len(choices)):
            if choices[i] in semantic_descriptors.keys():
                #check this
                choice_similarity[i] = similarity_fn(semantic_descriptors[word],semantic_descriptors[choices[i]])
            else:
                choice_similarity[i] = -1
    else:
        return 0

    max_sim = 0

    for i in range (len(choice_similarity)):
        if choice_similarity[i] > max_sim:
            ind = i
            max_sim = choice_similarity[i]

    return ind


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    #f = open(filename, encoding="latin1")
    #s = f.read().split("\n")
    s = open("C:/Users/hannahkim/Desktop/ESC180/ESC180/Projects/Project 3/test.txt", encoding="latin-1").read().split("\n")
    correct = 0

    for i in range (len(s)):
        line = s[i].split(" ")
        line2 = line[2:]
        if line2[most_similar_word(line[0], line2, semantic_descriptors, similarity_fn)] == line[1]:
            correct += 1

    return float(correct/len(s))
    

if __name__ == "__main__":
    #print (cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")