# Seq2Seq prediction using Encoder-Decoder Architecture and Attention

In this exercise we are going to implement 2 models

1. [Learning_Phrase_Representations_using_RNN_Encoder_Decoder_for_Statistical_Machine_Translation](./References/Learning_Phrase_Representations_using_RNN_Encoder_Decoder_for_Statistical_Machine_Translation.ipynb).
2. [Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate](./References/Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate.ipynb).

on the below mentioned datasets.



## 1. Question-Answer Dataset

This dataset provides corpus of Wikipedia articles, manually-generated factoid questions from them, and manually-generated answers to these questions, for use in academic research. These data were collected by Noah Smith, Michael Heilman, Rebecca Hwa, Shay Cohen, Kevin Gimpel, and many students at Carnegie Mellon University and the University of Pittsburgh between 2008 and 2010. Check [here](https://www.cs.cmu.edu/~ark/QA-data/) to know more.

### [Model1](Q&A_model1.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(2235, 256)
    (rnn): GRU(256, 512)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (embedding): Embedding(1471, 256)
    (rnn): GRU(768, 512)
    (fc_out): Linear(in_features=1280, out_features=1471, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 0m 8s
	Train Loss: 5.300 | Train PPL: 200.255
	 Val. Loss: 3.949 |  Val. PPL:  51.906
Epoch: 02 | Time: 0m 8s
	Train Loss: 4.460 | Train PPL:  86.499
	 Val. Loss: 3.865 |  Val. PPL:  47.695
Epoch: 03 | Time: 0m 8s
	Train Loss: 4.321 | Train PPL:  75.290
	 Val. Loss: 3.885 |  Val. PPL:  48.668
Epoch: 04 | Time: 0m 8s
	Train Loss: 4.214 | Train PPL:  67.643
	 Val. Loss: 3.854 |  Val. PPL:  47.181
Epoch: 05 | Time: 0m 8s
	Train Loss: 4.126 | Train PPL:  61.919
	 Val. Loss: 3.851 |  Val. PPL:  47.062
Epoch: 06 | Time: 0m 8s
	Train Loss: 4.025 | Train PPL:  56.007
	 Val. Loss: 3.764 |  Val. PPL:  43.140
Epoch: 07 | Time: 0m 8s
	Train Loss: 3.829 | Train PPL:  46.034
	 Val. Loss: 3.732 |  Val. PPL:  41.763
Epoch: 08 | Time: 0m 8s
	Train Loss: 3.735 | Train PPL:  41.906
	 Val. Loss: 3.695 |  Val. PPL:  40.249
Epoch: 09 | Time: 0m 8s
	Train Loss: 3.633 | Train PPL:  37.811
	 Val. Loss: 3.756 |  Val. PPL:  42.766
Epoch: 10 | Time: 0m 8s
	Train Loss: 3.506 | Train PPL:  33.305
	 Val. Loss: 3.762 |  Val. PPL:  43.016
```

### [Model2](Q&A_model2.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(2234, 256)
    (rnn): GRU(256, 512, bidirectional=True)
    (fc): Linear(in_features=1024, out_features=512, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (attention): Attention(
      (attn): Linear(in_features=1536, out_features=512, bias=True)
      (v): Linear(in_features=512, out_features=1, bias=False)
    )
    (embedding): Embedding(1486, 256)
    (rnn): GRU(1280, 512)
    (fc_out): Linear(in_features=1792, out_features=1486, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 0m 7s
	Train Loss: 5.020 | Train PPL: 151.398
	 Val. Loss: 3.708 |  Val. PPL:  40.763
Epoch: 02 | Time: 0m 7s
	Train Loss: 4.316 | Train PPL:  74.872
	 Val. Loss: 3.552 |  Val. PPL:  34.897
Epoch: 03 | Time: 0m 7s
	Train Loss: 4.102 | Train PPL:  60.476
	 Val. Loss: 3.547 |  Val. PPL:  34.708
Epoch: 04 | Time: 0m 7s
	Train Loss: 3.919 | Train PPL:  50.331
	 Val. Loss: 3.516 |  Val. PPL:  33.661
Epoch: 05 | Time: 0m 7s
	Train Loss: 3.693 | Train PPL:  40.175
	 Val. Loss: 3.524 |  Val. PPL:  33.929
Epoch: 06 | Time: 0m 7s
	Train Loss: 3.441 | Train PPL:  31.221
	 Val. Loss: 3.454 |  Val. PPL:  31.627
Epoch: 07 | Time: 0m 7s
	Train Loss: 3.169 | Train PPL:  23.780
	 Val. Loss: 3.429 |  Val. PPL:  30.841
Epoch: 08 | Time: 0m 7s
	Train Loss: 2.839 | Train PPL:  17.093
	 Val. Loss: 3.405 |  Val. PPL:  30.123
Epoch: 09 | Time: 0m 7s
	Train Loss: 2.546 | Train PPL:  12.757
	 Val. Loss: 3.365 |  Val. PPL:  28.944
Epoch: 10 | Time: 0m 7s
	Train Loss: 2.266 | Train PPL:   9.643
	 Val. Loss: 3.331 |  Val. PPL:  27.967
```

## 2. Stanford Question Answering Dataset (SQuAD)

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable. Check [here](https://rajpurkar.github.io/SQuAD-explorer/) to know more.

### [Model1](SQuAD_model1.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(18975, 256)
    (rnn): GRU(256, 512)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (embedding): Embedding(16610, 256)
    (rnn): GRU(768, 512)
    (fc_out): Linear(in_features=1280, out_features=16610, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 3m 36s
	Train Loss: 6.220 | Train PPL: 502.922
	 Val. Loss: 5.806 |  Val. PPL: 332.395
Epoch: 02 | Time: 3m 38s
	Train Loss: 5.809 | Train PPL: 333.264
	 Val. Loss: 5.796 |  Val. PPL: 328.833
Epoch: 03 | Time: 3m 36s
	Train Loss: 5.527 | Train PPL: 251.349
	 Val. Loss: 5.502 |  Val. PPL: 245.102
Epoch: 04 | Time: 3m 37s
	Train Loss: 5.154 | Train PPL: 173.116
	 Val. Loss: 5.398 |  Val. PPL: 220.893
Epoch: 05 | Time: 3m 35s
	Train Loss: 4.804 | Train PPL: 121.996
	 Val. Loss: 5.416 |  Val. PPL: 225.053
Epoch: 06 | Time: 3m 34s
	Train Loss: 4.414 | Train PPL:  82.608
	 Val. Loss: 5.478 |  Val. PPL: 239.365
Epoch: 07 | Time: 3m 33s
	Train Loss: 3.979 | Train PPL:  53.446
	 Val. Loss: 5.673 |  Val. PPL: 291.048
Epoch: 08 | Time: 3m 36s
	Train Loss: 3.453 | Train PPL:  31.589
	 Val. Loss: 5.936 |  Val. PPL: 378.516
Epoch: 09 | Time: 3m 35s
	Train Loss: 2.953 | Train PPL:  19.158
	 Val. Loss: 6.169 |  Val. PPL: 477.937
Epoch: 10 | Time: 3m 37s
	Train Loss: 2.556 | Train PPL:  12.884
	 Val. Loss: 6.365 |  Val. PPL: 581.222
```

### [Model2](SQuAD_model2.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(19047, 256)
    (rnn): GRU(256, 512, bidirectional=True)
    (fc): Linear(in_features=1024, out_features=512, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (attention): Attention(
      (attn): Linear(in_features=1536, out_features=512, bias=True)
      (v): Linear(in_features=512, out_features=1, bias=False)
    )
    (embedding): Embedding(16638, 256)
    (rnn): GRU(1280, 512)
    (fc_out): Linear(in_features=1792, out_features=16638, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```

Epoch: 01 | Time: 3m 53s
	Train Loss: 6.097 | Train PPL: 444.396
	 Val. Loss: 5.455 |  Val. PPL: 233.892
Epoch: 02 | Time: 3m 54s
	Train Loss: 5.389 | Train PPL: 218.937
	 Val. Loss: 5.238 |  Val. PPL: 188.380
Epoch: 03 | Time: 3m 52s
	Train Loss: 4.901 | Train PPL: 134.375
	 Val. Loss: 5.182 |  Val. PPL: 178.000
Epoch: 04 | Time: 3m 54s
	Train Loss: 4.347 | Train PPL:  77.246
	 Val. Loss: 5.263 |  Val. PPL: 193.032
Epoch: 05 | Time: 3m 54s
	Train Loss: 3.624 | Train PPL:  37.501
	 Val. Loss: 5.591 |  Val. PPL: 267.979
Epoch: 06 | Time: 3m 54s
	Train Loss: 2.908 | Train PPL:  18.314
	 Val. Loss: 5.896 |  Val. PPL: 363.558
Epoch: 07 | Time: 3m 53s
	Train Loss: 2.427 | Train PPL:  11.329
	 Val. Loss: 6.162 |  Val. PPL: 474.509
Epoch: 08 | Time: 3m 54s
	Train Loss: 2.111 | Train PPL:   8.259
	 Val. Loss: 6.351 |  Val. PPL: 572.913
Epoch: 09 | Time: 3m 53s
	Train Loss: 1.860 | Train PPL:   6.421
	 Val. Loss: 6.591 |  Val. PPL: 728.565
Epoch: 10 | Time: 3m 54s
	Train Loss: 1.660 | Train PPL:   5.261
	 Val. Loss: 6.763 |  Val. PPL: 865.327
```

## 3. Customer Support on twitter

The Customer Support on Twitter dataset is a large, modern corpus of tweets and replies to aid innovation in natural language understanding and conversational models, and for study of modern customer support practices and impact. Check [here](https://www.kaggle.com/thoughtvector/customer-support-on-twitter) to know more.

### [Model1](twcs_model1.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(10004, 128)
    (rnn): GRU(128, 256)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (embedding): Embedding(10004, 128)
    (rnn): GRU(384, 256)
    (fc_out): Linear(in_features=640, out_features=10004, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 39m 43s
	Train Loss: 3.922 | Train PPL:  50.484
	 Val. Loss: 5.675 |  Val. PPL: 291.609
Epoch: 02 | Time: 39m 35s
	Train Loss: 3.377 | Train PPL:  29.272
	 Val. Loss: 5.658 |  Val. PPL: 286.667
Epoch: 03 | Time: 39m 33s
	Train Loss: 3.275 | Train PPL:  26.436
	 Val. Loss: 5.712 |  Val. PPL: 302.400
```

### [Model2](twcs_model2.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(10004, 256)
    (rnn): GRU(256, 512, bidirectional=True)
    (fc): Linear(in_features=1024, out_features=512, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (attention): Attention(
      (attn): Linear(in_features=1536, out_features=512, bias=True)
      (v): Linear(in_features=512, out_features=1, bias=False)
    )
    (embedding): Embedding(10004, 256)
    (rnn): GRU(1280, 512)
    (fc_out): Linear(in_features=1792, out_features=10004, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 14m 57s
	Train Loss: 4.697 | Train PPL: 109.572
	 Val. Loss: 5.487 |  Val. PPL: 241.542
Epoch: 02 | Time: 15m 6s
	Train Loss: 3.951 | Train PPL:  51.972
	 Val. Loss: 5.506 |  Val. PPL: 246.203
Epoch: 03 | Time: 15m 8s
	Train Loss: 3.609 | Train PPL:  36.912
	 Val. Loss: 5.533 |  Val. PPL: 252.943
Epoch: 04 | Time: 15m 9s
	Train Loss: 3.469 | Train PPL:  32.111
	 Val. Loss: 5.470 |  Val. PPL: 237.441
Epoch: 05 | Time: 15m 10s
	Train Loss: 3.338 | Train PPL:  28.152
	 Val. Loss: 5.561 |  Val. PPL: 259.974
```


## 4. AmbigQA Dataset

Ambiguity is inherent to open-domain question answering; especially when exploring new topics, it can be difficult to ask questions that have a single, unambiguous answer. We introduce AmbigQA, a new open-domain question answering task which involves predicting a set of question-answer pairs, where every plausible answer is paired with a disambiguated rewrite of the original question.

To study this task, we construct AmbigNQ, a dataset covering 14,042 questions from NQ-open, an existing open-domain QA benchmark. We find that over half of the questions in NQ-open are ambiguous. The types of ambiguity are diverse and sometimes subtle, many of which are only apparent after examining evidence provided by a very large text corpus. Visit the [website](https://nlp.cs.washington.edu/ambigqa/) to read more.

### [Model1](AmbigQA_model1.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(9717, 128)
    (rnn): GRU(128, 256)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (embedding): Embedding(7986, 128)
    (rnn): GRU(384, 256)
    (fc_out): Linear(in_features=640, out_features=7986, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 0m 40s
	Train Loss: 5.721 | Train PPL: 305.096
	 Val. Loss: 5.387 |  Val. PPL: 218.561
Epoch: 02 | Time: 0m 41s
	Train Loss: 5.202 | Train PPL: 181.691
	 Val. Loss: 5.400 |  Val. PPL: 221.515
Epoch: 03 | Time: 0m 41s
	Train Loss: 5.010 | Train PPL: 149.879
	 Val. Loss: 5.089 |  Val. PPL: 162.220
Epoch: 04 | Time: 0m 41s
	Train Loss: 4.670 | Train PPL: 106.668
	 Val. Loss: 4.898 |  Val. PPL: 134.031
Epoch: 05 | Time: 0m 41s
	Train Loss: 4.354 | Train PPL:  77.782
	 Val. Loss: 4.791 |  Val. PPL: 120.461
Epoch: 06 | Time: 0m 41s
	Train Loss: 4.055 | Train PPL:  57.694
	 Val. Loss: 4.637 |  Val. PPL: 103.279
Epoch: 07 | Time: 0m 42s
	Train Loss: 3.718 | Train PPL:  41.189
	 Val. Loss: 4.496 |  Val. PPL:  89.648
Epoch: 08 | Time: 0m 42s
	Train Loss: 3.302 | Train PPL:  27.176
	 Val. Loss: 4.379 |  Val. PPL:  79.798
Epoch: 09 | Time: 0m 42s
	Train Loss: 2.955 | Train PPL:  19.199
	 Val. Loss: 4.377 |  Val. PPL:  79.577
Epoch: 10 | Time: 0m 41s
	Train Loss: 2.655 | Train PPL:  14.226
	 Val. Loss: 4.336 |  Val. PPL:  76.370
```

### [Model2](AmbigQA_model2.ipynb)

#### Architecture

```
Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(9717, 128)
    (rnn): GRU(128, 256, bidirectional=True)
    (fc): Linear(in_features=512, out_features=256, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (attention): Attention(
      (attn): Linear(in_features=768, out_features=256, bias=True)
      (v): Linear(in_features=256, out_features=1, bias=False)
    )
    (embedding): Embedding(7986, 128)
    (rnn): GRU(640, 256)
    (fc_out): Linear(in_features=896, out_features=7986, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)
```

#### Training Logs

```
Epoch: 01 | Time: 1m 9s
	Train Loss: 5.466 | Train PPL: 236.513
	 Val. Loss: 4.882 |  Val. PPL: 131.879
Epoch: 02 | Time: 1m 8s
	Train Loss: 4.705 | Train PPL: 110.522
	 Val. Loss: 4.681 |  Val. PPL: 107.843
Epoch: 03 | Time: 1m 8s
	Train Loss: 4.196 | Train PPL:  66.441
	 Val. Loss: 4.475 |  Val. PPL:  87.800
Epoch: 04 | Time: 1m 7s
	Train Loss: 3.630 | Train PPL:  37.695
	 Val. Loss: 4.270 |  Val. PPL:  71.541
Epoch: 05 | Time: 1m 7s
	Train Loss: 3.122 | Train PPL:  22.689
	 Val. Loss: 4.273 |  Val. PPL:  71.750
Epoch: 06 | Time: 1m 7s
	Train Loss: 2.696 | Train PPL:  14.827
	 Val. Loss: 4.288 |  Val. PPL:  72.846
Epoch: 07 | Time: 1m 7s
	Train Loss: 2.361 | Train PPL:  10.599
	 Val. Loss: 4.397 |  Val. PPL:  81.181
Epoch: 08 | Time: 1m 8s
	Train Loss: 2.110 | Train PPL:   8.247
	 Val. Loss: 4.454 |  Val. PPL:  85.992
Epoch: 09 | Time: 1m 8s
	Train Loss: 1.912 | Train PPL:   6.768
	 Val. Loss: 4.560 |  Val. PPL:  95.542
Epoch: 10 | Time: 1m 8s
	Train Loss: 1.750 | Train PPL:   5.752
	 Val. Loss: 4.740 |  Val. PPL: 114.454
```


With this we are able to understand the Encoder-Decoder Architecture for Seq2Seq prediction problem and the importance of Attention to achieve better results.
