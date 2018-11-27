# Modeling Human Reading with Neural Attention

Code for Modeling Human Reading with Neural Attention (EMNLP 2016).

Code adapted to test on ZuCo data.


## Preparing data

Data is expected in `data/` in the following structure: Texts in numerical form in `data/texts/`, a vocabulary in `data/dictionary.txt`, and a list of texts in `data/filenames.txt`. Samples of the appropriate format are given in the directories.


Models are saved to and loaded from `models/`.

## Creating an autoencoding model:

`th main-attention.lua 1 false false 64 50 1000 50000 5.0 false 0.1 100 0.0001 20 false none autoencoder-1 combined true 11 true 5.0 full true fixed`

or in general:

`th main-attention.lua 1 false false BATCH_SIZE SEQUENCE_LENGTH LSTM_DIMENSION VOCABULARY 5.0 false LEARNING_RATE EMBEDDINGS_DIMENSION 0.0001 20 false none NAME_OF_YOUR_MODEL combined true CORPUS_NUMBER true 5.0 full true fixed`

`VOCABULARY` is smaller or equal to the number of tokens in `data/dictionary.txt`. All words with indices greater than the vocabulary size will be replaced by "OOV".

`SEQUENCE_LENGTH`: each article is chopped into fixed-length strings for processing, default = 50.

`CORPUS_NUMBER` can be any integer, remnant from older version of code.

To control the learning rate during training, edit the file `lr-1`, whose content is the learning rate.

To control the attention rate during training, edit `attention-1` in the same directory, whose content is the attention rate (a number between 0 and 1). In the original experiments, it was initialized at 1 and annealed to 0.6.

### Training:
During training, the autoencoder occasionally outputs a word sequence with some annotation like the following:

`common   '  0.12863277395199  1.0437612589932e-05        '  0.18989889768736  6.0917715431689e-06        1  1`

which contains the following information:

- the actual word
- the word reconstructed by the decoder
- the probability assigned to that word
- the probability the decoder assigns to the correct word
- the word predicted by the language model
- the probability assigned to that word by the LM
- the prob. assigned to the correct word by the LM
- the fixation probability (which is controlled by the content of attention-1 during training of the autoencoder)
- whether the word was actually fixated

Training will stop after 1 epoch, as specified in the variable EPOCHS_NUMBER in setParameters.lua. During this epoch, you can manually anneal the attention rate in attention-1 down to something like 0.6 so that the model gets used to skipping. The model is saved after every 500 training steps.

## Creating an attention network:

`th main-attention.lua 1 false true 64 10 1000 50000 5.0 false 0.7 100 0.0001 20 false autoencoder-1 attention-1 combined true 1 true 5.0 full true fixed`

or in general:

`th main-attention.lua 1 false true BATCH_SIZE SEQUENCE_LENGTH LSTM_DIMENSION VOCABULARY TOTAL_ATTENTION_WEIGHT false LEARNING_RATE EMBEDDINGS_DIMENSION 0.1 20 false NAME_OF_AUTOENCODING_MODEL NAME_OF_ATTENTION_MODEL combined true 1 true ENTROPY_WEIGHT full true fixed`

where `TOTAL_ATTENTION_WEIGHT` is alpha, `ENTROPY_WEIGHT` is gamma from Section 4.1 of the paper.

To control the learning rate of REINFORCE during training, modify the file named `lr-att-1`, whose content is this rate (0.01 in the original experiments).

## Running an attention network to create predictions:

`th main-attention.lua 1 true true 64 10 1000 50000 5.0 false 0.7 100 0.0001 20 false attention-1 attention-1 combined false 1 true 5.0 full true fixed`

or in general:

`th main-attention.lua 1 true true BATCH_SIZE SEQUENCE_LENGTH LSTM_DIMENSION VOCABULARY TOTAL_ATTENTION_WEIGHT false LEARNING_RATE EMBEDDINGS_DIMENSION 0.1 20 false NAME_OF_ATTENTION_MODEL NAME_OF_ATTENTION_MODEL combined false 1 true ENTROPY_WEIGHT full true fixed`

This will create files with attention output in `data/annotation/`.


