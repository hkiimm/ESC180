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

    for i in vec1.keys():
        if i in vec2.keys():
            numerator += vec1[i] * vec2[i]

    return round(numerator/(norm(vec1))/(norm(vec2)), 5)


def build_semantic_descriptors(sentences):
    semantic_descriptors = {}
 
    for sentence in sentences:
        unique_words = list(set(sentence))
        for i in range(len(unique_words)):
            coord_1 = unique_words[i]
            for j in range(i):
                coord_2 = unique_words[j]
                if coord_1 != coord_2:
                    if coord_1 not in semantic_descriptors:
                        semantic_descriptors[coord_1] = {}
                    if coord_2 not in semantic_descriptors[coord_1]:
                        semantic_descriptors[coord_1][coord_2] = 1
                    else:
                        semantic_descriptors[coord_1][coord_2] += 1

                    if coord_2 not in semantic_descriptors:
                        semantic_descriptors[coord_2] = {}
                    if coord_1 not in semantic_descriptors[coord_2]:
                        semantic_descriptors[coord_2][coord_1] = 1
                    else:
                        semantic_descriptors[coord_2][coord_1] += 1

    return semantic_descriptors



def build_semantic_descriptors_from_files(filenames):
    text = ""
    sentences = []
    sem_descript = {}

    for filename in filenames:
        text += open(filename, "r", encoding="latin1").read().lower()

    text = text.replace(",", "").replace("--", " ").replace("-", " ").replace(":","").replace(";", "").replace("\n", " ")
    text = text.replace("!", ".").replace("?", ".").split(".")

    for i in range (len(text)):
        sentences.append([x for x in text[i].split(" ") if x != ''])

    sem_descript = build_semantic_descriptors(sentences)

    return sem_descript



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    choice_similarity = [0]*len(choices)
    ind = 0
    if word in semantic_descriptors.keys():
        for i in range (len(choices)):
            if choices[i] in semantic_descriptors.keys():
                choice_similarity[i] = similarity_fn(semantic_descriptors[word],semantic_descriptors[choices[i]])
            else:
                choice_similarity[i] = -1
    else:
        return -1

    max_sim = -1

    for i in range (len(choice_similarity)):
        if choice_similarity[i] > max_sim:
            ind = i
            max_sim = choice_similarity[i]

    return choices[ind]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    s = open(filename, encoding="latin-1").read().split("\n")
    correct = 0
    count = 0
    for i in range (len(s)):
        line = s[i].split(" ")
        if len(line) > 2:
            line2 = line[2:]

            if most_similar_word(line[0], line2, semantic_descriptors, similarity_fn) == line[1]:
                correct += 1
            count += 1

    return float(correct/(count))*100



if __name__ == "__main__":
    #print (cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")