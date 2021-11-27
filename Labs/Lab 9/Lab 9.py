import urllib.request


hey = open("C:/Users/Hannah/Desktop/Lab 9/pride_and_prejudice.txt", encoding="latin-1").read().split()


dict1 = dict.fromkeys(hey, 0)
for i in (hey):
    dict1[i] += 1

## Problem 1A

def word_count (w):
    dict1 = dict.fromkeys(hey, 0)
    if w not in dict1:
        return 0

    for i in (hey):
        dict1[i] += 1

    return dict[w]

## Problem 1B

def top10(L):
    L.sort(reverse=True)
    return L[0:10]

## Problem 1C
def top_words(freq):
    tup = tuple(freq.items())
    tup_inv = sorted(tuple((y, x) for x, y in tup), reverse = True)
    print (tup_inv)
    for i in range (10):
        print (tup_inv[i][1])


if __name__ == "__main__":
    # inv_freq = {6: "the", 12: "a", 1:"hi"}
    # print(sorted(inv_freq.items()))
    top_words(dict1)


## Problem 2
# Check document

## Problem 3
def result_num(search_term):
    #https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p=engineering%20science&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1


    link = "https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p=" + urllib.parse.quote(search_term) + "&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1"

    f = urllib.request.urlopen(link)
    page = f.read().decode("utf-8")
    f.close()

    return(int(page[page.index("About")+6:page.index("search results")].replace(",", "")))

def choose_variant(variants):
    results = [0]*len(variants)

    for i in range (len(variants)):
        results[i] = result_num(variants[i])

    return variants[results.index(max(results))]

if __name__ == "__main__":
    print(choose_variant(["top ranked school uoft", "top ranked school waterloo"]))