import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()


def lemmatize_words(word_list):
    lemmas = []
    for word, tag in nltk.pos_tag(word_list):
        wn_tag = get_wordnet_pos(tag)
        if wn_tag is not None:
            lemma = lemmatizer.lemmatize(word.lower(), pos=wn_tag)
        else:
            lemma = lemmatizer.lemmatize(word.lower())
        lemmas.append(lemma)
    return lemmas


def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return None


sharing_words = [
    "share",
    "send",
    "pass",
    "give",
    "distribute",
    "forward",
    "disseminate",
    "circulate",
    "transmit",
    "spread",
    "add",
    "provide",
    "make",
    "include",
    "use",
    "post",
    "deliver",
    "release",
    "transfer",
    "convey",
    "accessible",
    "make",
]

asking_words = [
    "can",
    "could",
    "would",
    "may",
    "might",
    "permission",
    "allow",
    "accept",
    "comfort",
    "ask",
    "get",
    "request",
    "inquire",
    "seek",
    "query",
    "wonder",
    "want",
    "solicit",
    "invite",
]


def any_intersection(list1, list2):
    return any(word in list2 for word in list1)


def all_intersection(word_list, reference_list):
    return all(word in reference_list for word in word_list)


def classify_phrase_intent(text: str) -> str:
    lemmatized_words = lemmatize_words(word_tokenize(text))

    if any_intersection(sharing_words, lemmatized_words):
        if (
            any_intersection(asking_words, lemmatized_words)
            or all_intersection(["be", "it"], lemmatized_words)
            or all_intersection(["be", "ok"], lemmatized_words)
            or all_intersection(["do", "you"], lemmatized_words)
            or all_intersection(["are", "you"], lemmatized_words)
            or all_intersection(["do", "we"], lemmatized_words)
        ):
            return "ask"
        return "shared"

    return "unclear"
