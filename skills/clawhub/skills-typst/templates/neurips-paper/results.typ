= Results <sec-results>

== Machine Translation

On the WMT 2014 English-to-German translation task, the big transformer model
(Transformer (big) in @tab-results) outperforms the best previously reported models
(including ensembles) by more than $2.0$ BLEU, establishing a new state-of-the-art
BLEU score of $28.4$. The configuration of this model is listed in the bottom line
of @tab-variations. Training took $3.5$ days on $8$ P100 GPUs. Even our base model
surpasses all previously published models and ensembles, at a fraction of the
training cost of any of the competitive models.

On the WMT 2014 English-to-French translation task, our big model achieves a BLEU
score of $41.0$, outperforming all of the previously published single models, at
less than $1 \/ 4$ the training cost of the previous state-of-the-art model. The
Transformer (big) model trained for English-to-French used dropout rate
$P_"drop" = 0.1$, instead of $0.3$.

For the base models, we used a single model obtained by averaging the last 5
checkpoints, which were written at 10-minute intervals. For the big models, we
averaged the last 20 checkpoints. We used beam search with a beam size of $4$ and
length penalty $alpha = 0.6$ @wu2016google. These hyperparameters were chosen after
experimentation on the development set. We set the maximum output length during
inference to input length $+ 50$, but terminate early when possible @wu2016google.

@tab-results summarizes our results and compares our translation quality and
training costs to other model architectures from the literature. We estimate the
number of floating point operations used to train a model by multiplying the
training time, the number of GPUs used, and an estimate of the sustained
single-precision floating-point capacity of each GPU#footnote[We used values of
2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively.].

#figure(
  placement: top,
  table(
    columns: 5,
    align: (col, _) => if col == 0 { left } else { center + horizon },
    inset: (x: 7pt, y: 3pt),
    table.hline(stroke: 0.8pt),
    table.cell(rowspan: 2)[*Model*],
    table.cell(colspan: 2)[*BLEU*],
    table.cell(colspan: 2)[*Training Cost (FLOPs)*],
    [EN-DE], [EN-FR], [EN-DE], [EN-FR],
    table.hline(stroke: 0.5pt),
    [ByteNet @kalchbrenner2017neural], [23.75], [—], [—], [—],
    [Deep-Att + PosUnk @zhou2016deep], [—], [39.2], [—], [$1.0 dot.c 10^(20)$],
    [GNMT + RL @wu2016google], [24.6], [39.92], [$2.3 dot.c 10^(19)$], [$1.4 dot.c 10^(20)$],
    [ConvS2S @gehring2017convolutional], [25.16], [40.46], [$9.6 dot.c 10^(18)$], [$1.5 dot.c 10^(20)$],
    [MoE @shazeer2017outrageously], [26.03], [40.56], [$2.0 dot.c 10^(19)$], [$1.2 dot.c 10^(20)$],
    table.hline(stroke: 0.5pt),
    [Deep-Att + PosUnk Ensemble @zhou2016deep], [—], [40.4], [—], [$8.0 dot.c 10^(20)$],
    [GNMT + RL Ensemble @wu2016google], [26.30], [41.16], [$1.8 dot.c 10^(20)$], [$1.1 dot.c 10^(21)$],
    [ConvS2S Ensemble @gehring2017convolutional], [26.36], [*41.29*], [$7.7 dot.c 10^(19)$], [$1.2 dot.c 10^(21)$],
    table.hline(stroke: 0.8pt),
    [Transformer (base model)], [27.3], [38.1],
    table.cell(colspan: 2)[$3.3 dot.c 10^(18)$],
    [Transformer (big)], [*28.4*], [*41.8*],
    table.cell(colspan: 2)[$2.3 dot.c 10^(19)$],
    table.hline(stroke: 0.8pt),
  ),
  caption: [
    The Transformer achieves better BLEU scores than previous state-of-the-art
    models on the English-to-German and English-to-French newstest2014 tests at a
    fraction of the training cost.
  ],
) <tab-results>

== Model Variations

To evaluate the importance of different components of the Transformer, we varied
our base model in different ways, measuring the change in performance on
English-to-German translation on the development set, newstest2013. We used beam
search as described in the previous section, but no checkpoint averaging. We present
these results in @tab-variations.

#figure(
  placement: top,
  text(size: 7.5pt, table(
    columns: 13,
    align: (col, _) => if col == 0 { left + horizon } else { center + horizon },
    inset: (x: 3pt, y: 2.6pt),
    table.vline(x: 1, stroke: 0.4pt),
    table.vline(x: 10, stroke: 0.4pt),
    table.hline(stroke: 0.8pt),
    table.header(
      [], [$N$], [$d_"model"$], [$d_"ff"$], [$h$], [$d_k$], [$d_v$], [$P_"drop"$],
      [$epsilon_"ls"$], [train\ steps], [PPL\ (dev)], [BLEU\ (dev)], [params\ $times 10^6$],
    ),
    table.hline(stroke: 0.5pt),
    [base], [6], [512], [2048], [8], [64], [64], [0.1], [0.1], [100K], [4.92], [25.8], [65],
    table.hline(stroke: 0.4pt),
    table.cell(rowspan: 4)[(A)],
    [], [], [], [1], [512], [512], [], [], [], [5.29], [24.9], [],
    [], [], [], [4], [128], [128], [], [], [], [5.00], [25.5], [],
    [], [], [], [16], [32], [32], [], [], [], [4.91], [25.8], [],
    [], [], [], [32], [16], [16], [], [], [], [5.01], [25.4], [],
    table.hline(stroke: 0.4pt),
    table.cell(rowspan: 2)[(B)],
    [], [], [], [], [16], [], [], [], [], [5.16], [25.1], [58],
    [], [], [], [], [32], [], [], [], [], [5.01], [25.4], [60],
    table.hline(stroke: 0.4pt),
    table.cell(rowspan: 7)[(C)],
    [2], [], [], [], [], [], [], [], [], [6.11], [23.7], [36],
    [4], [], [], [], [], [], [], [], [], [5.19], [25.3], [50],
    [8], [], [], [], [], [], [], [], [], [4.88], [25.5], [80],
    [], [256], [], [], [32], [32], [], [], [], [5.75], [24.5], [28],
    [], [1024], [], [], [128], [128], [], [], [], [4.66], [26.0], [168],
    [], [], [1024], [], [], [], [], [], [], [5.12], [25.4], [53],
    [], [], [4096], [], [], [], [], [], [], [4.75], [26.2], [90],
    table.hline(stroke: 0.4pt),
    table.cell(rowspan: 4)[(D)],
    [], [], [], [], [], [], [0.0], [], [], [5.77], [24.6], [],
    [], [], [], [], [], [], [0.2], [], [], [4.95], [25.5], [],
    [], [], [], [], [], [], [], [0.0], [], [4.67], [25.3], [],
    [], [], [], [], [], [], [], [0.2], [], [5.47], [25.7], [],
    table.hline(stroke: 0.4pt),
    [(E)], table.cell(colspan: 9)[positional embedding instead of sinusoids],
    [4.92], [25.7], [],
    table.hline(stroke: 0.5pt),
    [big], [6], [1024], [4096], [16], [], [], [0.3], [], [300K], [*4.33*], [*26.4*], [213],
    table.hline(stroke: 0.8pt),
  )),
  caption: [
    Variations on the Transformer architecture. Unlisted values are identical to
    those of the base model. All metrics are on the English-to-German translation
    development set, newstest2013. Listed perplexities are per-wordpiece, according
    to our byte-pair encoding, and should not be compared to per-word perplexities.
  ],
) <tab-variations>

In @tab-variations rows (A), we vary the number of attention heads and the
attention key and value dimensions, keeping the amount of computation constant, as
described in @sec-multihead. While single-head attention is 0.9 BLEU worse than the
best setting, quality also drops off with too many heads.

In @tab-variations rows (B), we observe that reducing the attention key size $d_k$
hurts model quality. This suggests that determining compatibility is not easy and
that a more sophisticated compatibility function than dot product may be beneficial.
We further observe in rows (C) and (D) that, as expected, bigger models are better,
and dropout is very helpful in avoiding over-fitting. In row (E) we replace our
sinusoidal positional encoding with learned positional embeddings
@gehring2017convolutional, and observe nearly identical results to the base model.

== English Constituency Parsing

To evaluate if the Transformer can generalize to other tasks we performed
experiments on English constituency parsing. This task presents specific
challenges: the output is subject to strong structural constraints and is
significantly longer than the input. Furthermore, RNN sequence-to-sequence models
have not been able to attain state-of-the-art results in small-data regimes
@vinyals2015grammar.

We trained a 4-layer transformer with $d_"model" = 1024$ on the Wall Street Journal
(WSJ) portion of the Penn Treebank @marcus1993building, about 40K training
sentences. We also trained it in a semi-supervised setting, using the larger
high-confidence and BerkeleyParser corpora from with approximately 17M sentences
@vinyals2015grammar. We used a vocabulary of 16K tokens for the WSJ only setting and
a vocabulary of 32K tokens for the semi-supervised setting.

We performed only a small number of experiments to select the dropout, both
attention and residual (@sec-reg), learning rates and beam size on the Section 22
development set, all other parameters remained unchanged from the English-to-German
base translation model. During inference, we increased the maximum output length to
input length $+ 300$. We used a beam size of $21$ and $alpha = 0.3$ for both WSJ
only and the semi-supervised setting.

#figure(
  placement: top,
  table(
    columns: 3,
    align: (col, _) => if col == 2 { center + horizon } else { left + horizon },
    inset: (x: 7pt, y: 3pt),
    table.hline(stroke: 0.8pt),
    table.header([*Parser*], [*Training*], [*WSJ 23 F1*]),
    table.hline(stroke: 0.5pt),
    [Vinyals \& Kaiser et al. (2014) @vinyals2015grammar], [WSJ only, discriminative], [88.3],
    [Petrov et al. (2006) @petrov2006learning], [WSJ only, discriminative], [90.4],
    [Zhu et al. (2013) @zhu2013fast], [WSJ only, discriminative], [90.4],
    [Dyer et al. (2016) @dyer2016recurrent], [WSJ only, discriminative], [91.7],
    table.hline(stroke: 0.4pt),
    [Transformer (4 layers)], [WSJ only, discriminative], [91.3],
    table.hline(stroke: 0.4pt),
    [Zhu et al. (2013) @zhu2013fast], [semi-supervised], [91.3],
    [Huang \& Harper (2009) @huang2009self], [semi-supervised], [91.3],
    [McClosky et al. (2006) @mcclosky2006effective], [semi-supervised], [92.1],
    [Vinyals \& Kaiser et al. (2014) @vinyals2015grammar], [semi-supervised], [92.1],
    table.hline(stroke: 0.4pt),
    [Transformer (4 layers)], [semi-supervised], [92.7],
    table.hline(stroke: 0.4pt),
    [Luong et al. (2015) @luong2016multi], [multi-task], [93.0],
    [Dyer et al. (2016) @dyer2016recurrent], [generative], [93.3],
    table.hline(stroke: 0.8pt),
  ),
  caption: [
    The Transformer generalizes well to English constituency parsing (results are
    on Section 23 of WSJ).
  ],
) <tab-parsing>

Our results in @tab-parsing show that despite the lack of task-specific tuning our
model performs surprisingly well, yielding better results than all previously
reported models with the exception of the Recurrent Neural Network Grammar
@dyer2016recurrent. In contrast to RNN sequence-to-sequence models
@vinyals2015grammar, the Transformer outperforms the BerkeleyParser
@petrov2006learning even when training only on the WSJ training set of 40K
sentences.
