
Preprocessing of ZuCo corpus (only NR and SR) for testing NEAT

In the original experiment from the paper the following data points were removed:
- where the word was outside of the vocabulary of the model
- where the word was mapped to positions 1–3 or 48–50 of a sequence when splitting the data


Determine the human fixation rate:

- Dundee: 62.1% on dev set and 61.3% on the test set
- ZuCo: 70.3% (run `zuco_fixation_rate.py`) for SR + NR, 54.74% for TSR
