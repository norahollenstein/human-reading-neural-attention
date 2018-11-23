import os

indir = "/Users/norahollenstein/Downloads/dailymail/stories/"
outdir = "../data/texts/"

for infile in os.listdir(indir)[:10]:

    text = open(infile, "r").readlines()

    txt2digits = {}
    idx = 0
    for line in infile:
        if not line == "\n":
            line = line.split("\t")
            if line[0] not in txt2digits:
                    txt2digits[line[0]] = idx
                    idx += 1

    dictionary_file = open("../data/dictionary.txt", "w")
    for word, digit in txt2digits.items():
        print(digit, word, file=dictionary_file)

    filenames_file = open("../data/filenames.txt", "w")

    i = 0
    for line in infile:
        outfile = open(outdir + "dailymail_digits_"+str(i)+".txt", "a")
        if not line == "\n":
            line = line.split("\t")

            print(txt2digits[line[0]], file=outfile)
        else:
            print("\n", file=outfile)
            print("dailymail_digits_"+str(i)+".txt", file=filenames_file)
            i += 1

print("PREPROCESSING DONE.")