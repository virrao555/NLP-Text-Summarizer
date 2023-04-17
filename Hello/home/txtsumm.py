import spacy,sys
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation

document1 = sys.argv[1]


#TEXT PREPROCESSING + TOKENIZATION

stopwords = list(STOP_WORDS)
len(stopwords)
nlp = spacy.load("en_core_web_sm")
docx = nlp(document1)


# for token in docx:
#     print(token.text)
#

word_frequency = {}
for word in docx:
    if word.text not in stopwords:
        if word.text not in word_frequency.keys():
            word_frequency[word.text] = 1
        else:
            word_frequency[word.text] += 1
            
#print(word_frequency)

maximum_frequency = max(word_frequency.values())
# print(maximum_frequency)

for word in word_frequency.keys():
    word_frequency[word] = (word_frequency[word]/maximum_frequency)
#print(word_frequency)


# SENTECE TOKENIZATION
sentence_list = [sentence for sentence in docx.sents]
# Sentence Score via comparrng each word with sentence
sentence_scores = {}
for sent in sentence_list:
    for word in sent:
        if word.text.lower() in word_frequency.keys():
            if len(sent.text.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequency[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequency[word.text.lower()]
#print(sentence_scores)


summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
#print(summarized_sentences)

# Convert Sentences from Spacy Span to Strings for joining entire sentence
for w in summarized_sentences:
    w.text
# List Comprehension of Sentences Converted From Spacy.span to strings
final_sentences = [ w.text for w in summarized_sentences ]

summary = ' '.join(final_sentences)

result = summary.rstrip()
print(repr(summary))
