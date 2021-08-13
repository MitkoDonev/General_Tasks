sentence1 = "We are really pleased to meet you in our city"
sentence2 = "The city was hit by a really heavy storm"


def removeDuplicatedWords(text):
    return list(set(text))


def findMatching(text1, text2):
    sentece1_as_list = sentence1.split()
    sentece2_as_list = sentence2.split()

    text1 = removeDuplicatedWords(sentece1_as_list)
    text2 = removeDuplicatedWords(sentece2_as_list)

    matching = []
    mismatching = []

    for word in text1:
        if word in text2:
            matching.append(word)
        else:
            mismatching.append(word)

    for word in text2:
        if word not in text1:
            mismatching.append(word)

    return matching, mismatching


matching, mismatching = findMatching(sentence1, sentence2)

print(f"Matching: {matching}\nMismatching: {mismatching}")
