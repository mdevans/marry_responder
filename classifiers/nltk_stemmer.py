# Purpose: NLTK Stemmer
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download("punkt")  # download the necessary package

stemmer = PorterStemmer()

share_stems = [
    "share",
    "send",
    "sent",
    "pass",
    "give",
    "given",
    "distribut",
    "forward",
    "dissemin",
    "circul",
    "transmit",
    "spread",
    "add",
    "ad",
    "provid",
    "make",
    "includ",
    "use",
]

ask_stems = [
    "can",
    "could",
    "would",
    "may",
    "might",
    "permission",
    "allow",
    "accept",
    "comfort",
    "alright",
]


def any_intersection(list1, list2):
    return any(word in list2 for word in list1)


def all_intersection(word_list, reference_list):
    return all(word in reference_list for word in word_list)


def classify_phrase_intent(text: str) -> str:
    stemmed_words = [stemmer.stem(w) for w in word_tokenize(text)]

    if any_intersection(share_stems, stemmed_words):
        if (
            any_intersection(ask_stems, stemmed_words)
            or all_intersection(["is", "it"], stemmed_words)
            or all_intersection(["is", "ok"], stemmed_words)
            or all_intersection(["do", "you"], stemmed_words)
            or all_intersection(["do", "we"], stemmed_words)
            or all_intersection(["are", "you"], stemmed_words)
        ):
            return "ask"
        return "shared"

    return "unclear"
