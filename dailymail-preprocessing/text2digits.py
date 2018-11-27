import os
import operator
import spacy
from spacy.lang.en import English

nlp = spacy.load('en_core_web_sm')
tokenizer = English().Defaults.create_tokenizer(nlp)

indir = "/Users/norahollenstein/Downloads/dailymail/stories/"
outdir = "../data/texts/"

dict_idx = 0
word_freq = {}

for infile in os.listdir(indir)[:2000]:

    text = open(indir+infile, "r").readlines()

    for line in text:
        if not line == "\n":
            tokens = tokenizer(line)
            for tok in tokens:
                if not str(tok).isspace():
                    if str(tok) not in word_freq:
                        word_freq[str(tok)] = 1
                    else:
                        word_freq[str(tok)] += 1

dictionary_file = open("../data/dictionary.txt", "w")
sorted_word_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
txt2digits = {}
for idx, word in enumerate(sorted_word_freq):
    print(word[0], idx, file=dictionary_file)
    txt2digits[word[0]] = idx


file_idx = 0
filenames_file = open("../data/filenames.txt", "w")
for infile in os.listdir(indir)[:2000]:

    text = open(indir+infile, "r").readlines()
    outfile = open(outdir + "dailymail_digits_" + str(file_idx) + ".txt", "w")
    print("dailymail_digits_" + str(file_idx) + ".txt", file=filenames_file)

    for line in text:
        if not line == "\n":
            tokens = tokenizer(line)
            for tok in tokens:
                if not str(tok).isspace():
                    print(txt2digits[str(tok)], file=outfile)
    print("\n", file=outfile)

    file_idx += 1

print("PREPROCESSING DONE.")
