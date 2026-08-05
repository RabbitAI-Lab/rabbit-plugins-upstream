= Training

This section describes the training regime for our models.

== Training Data and Batching

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5
million sentence pairs. Sentences were encoded using byte-pair encoding
@britz2017massive, which has a shared source-target vocabulary of about 37000
tokens. For English-French, we used the significantly larger WMT 2014
English-French dataset consisting of 36M sentences and split tokens into a 32000
word-piece vocabulary @wu2016google. Sentence pairs were batched together by
approximate sequence length. Each training batch contained a set of sentence pairs
containing approximately 25000 source tokens and 25000 target tokens.

== Hardware and Schedule

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models
using the hyperparameters described throughout the paper, each training step took
about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12
hours. For our big models (described on the bottom line of @tab-variations), step
time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).

== Optimizer

We used the Adam optimizer @kingma2015adam with $beta_1 = 0.9$, $beta_2 = 0.98$ and
$epsilon = 10^(-9)$. We varied the learning rate over the course of training,
according to the formula:

$ "lrate" = d_"model"^(-0.5) dot.c min("step_num"^(-0.5), "step_num" dot.c "warmup_steps"^(-1.5)) $

This corresponds to increasing the learning rate linearly for the first
$"warmup_steps"$ training steps, and decreasing it thereafter proportionally to the
inverse square root of the step number. We used $"warmup_steps" = 4000$.

== Regularization <sec-reg>

We employ three types of regularization during training:

*Residual Dropout.* We apply dropout @srivastava2014dropout to the output of each
sub-layer, before it is added to the sub-layer input and normalized. In addition,
we apply dropout to the sums of the embeddings and the positional encodings in both
the encoder and decoder stacks. For the base model, we use a rate of
$P_"drop" = 0.1$.

*Label Smoothing.* During training, we employed label smoothing of value
$epsilon_"ls" = 0.1$ @szegedy2016rethinking. This hurts perplexity, as the model
learns to be more unsure, but improves accuracy and BLEU score.
