import os
import spacy
from spacy.lang.en import English

nlp = spacy.load('en_core_web_sm')
tokenizer = English().Defaults.create_tokenizer(nlp)

indir = "/Users/norahollenstein/Downloads/dailymail/stories/"
outdir = "../data/texts/"

dict_idx = 0

txt2digits = {}

for infile in os.listdir(indir)[:200]:

    text = open(indir+infile, "r").readlines()

    for line in text:
        if not line == "\n":
            tokens = tokenizer(line)
            for tok in tokens:
                if not str(tok).isspace():
                    if str(tok) not in txt2digits:
                        txt2digits[str(tok)] = dict_idx
                        dict_idx += 1

dictionary_file = open("../data/dictionary.txt", "w")
for word, digit in txt2digits.items():
    print(digit, word, file=dictionary_file)

file_idx = 0
filenames_file = open("../data/filenames.txt", "w")
for infile in os.listdir(indir)[:200]:

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
