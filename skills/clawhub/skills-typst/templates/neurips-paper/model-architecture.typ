= Model Architecture <sec-model>

Most competitive neural sequence transduction models have an encoder-decoder
structure @cho2014learning @bahdanau2014neural @sutskever2014sequence. Here, the
encoder maps an input sequence of symbol representations $(x_1, ..., x_n)$ to a
sequence of continuous representations $bold(z) = (z_1, ..., z_n)$. Given
$bold(z)$, the decoder then generates an output sequence $(y_1, ..., y_m)$ of
symbols one element at a time. At each step the model is auto-regressive
@graves2013generating, consuming the previously generated symbols as additional
input when generating the next.

#figure(
  placement: top,
  image("Figures/ModalNet-21.png", width: 50%),
  caption: [The Transformer - model architecture.],
) <fig-arch>

The Transformer follows this overall architecture using stacked self-attention and
point-wise, fully connected layers for both the encoder and decoder, shown in the
left and right halves of @fig-arch, respectively.

== Encoder and Decoder Stacks

*Encoder:* The encoder is composed of a stack of $N = 6$ identical layers. Each
layer has two sub-layers. The first is a multi-head self-attention mechanism, and
the second is a simple, position-wise fully connected feed-forward network. We
employ a residual connection @he2016deep around each of the two sub-layers,
followed by layer normalization @ba2016layer. That is, the output of each
sub-layer is $op("LayerNorm")(x + op("Sublayer")(x))$, where $op("Sublayer")(x)$
is the function implemented by the sub-layer itself. To facilitate these residual
connections, all sub-layers in the model, as well as the embedding layers, produce
outputs of dimension $d_"model" = 512$.

*Decoder:* The decoder is also composed of a stack of $N = 6$ identical layers. In
addition to the two sub-layers in each encoder layer, the decoder inserts a third
sub-layer, which performs multi-head attention over the output of the encoder
stack. Similar to the encoder, we employ residual connections around each of the
sub-layers, followed by layer normalization. We also modify the self-attention
sub-layer in the decoder stack to prevent positions from attending to subsequent
positions. This masking, combined with fact that the output embeddings are offset
by one position, ensures that the predictions for position $i$ can depend only on
the known outputs at positions less than $i$.

== Attention <sec-attention>

An attention function can be described as mapping a query and a set of key-value
pairs to an output, where the query, keys, values, and output are all vectors. The
output is computed as a weighted sum of the values, where the weight assigned to
each value is computed by a compatibility function of the query with the
corresponding key.

// Figure 2 is declared here, right after the Attention intro and BEFORE the
// "Scaled Dot-Product Attention" subsection, so it appears between 3.2 and 3.2.1
// (as in the original). Kept inline (not floated): being taller than the space
// left on the page, it moves to the top of the next page with 3.2.1 flowing below.
#figure(
  grid(
    columns: (auto, auto),
    column-gutter: 1.5em,
    align: bottom,
    stack(spacing: 4pt, align(center, text(size: 9pt)[Scaled Dot-Product Attention]),
      image("Figures/ModalNet-19.png", height: 2.05in)),
    stack(spacing: 4pt, align(center, text(size: 9pt)[Multi-Head Attention]),
      image("Figures/ModalNet-20.png", height: 2.05in)),
  ),
  caption: [(left) Scaled Dot-Product Attention. (right) Multi-Head Attention
    consists of several attention layers running in parallel.],
) <fig-attn>

=== Scaled Dot-Product Attention

We call our particular attention "Scaled Dot-Product Attention" (@fig-attn). The
input consists of queries and keys of dimension $d_k$, and values of dimension
$d_v$. We compute the dot products of the query with all keys, divide each by
$sqrt(d_k)$, and apply a softmax function to obtain the weights on the values.

In practice, we compute the attention function on a set of queries simultaneously,
packed together into a matrix $Q$. The keys and values are also packed together
into matrices $K$ and $V$. We compute the matrix of outputs as:

$ op("Attention")(Q, K, V) = op("softmax") ((Q K^T) / sqrt(d_k)) V $

The two most commonly used attention functions are additive attention
@bahdanau2014neural, and dot-product (multiplicative) attention. Dot-product
attention is identical to our algorithm, except for the scaling factor of
$1 / sqrt(d_k)$. Additive attention computes the compatibility function using a
feed-forward network with a single hidden layer. While the two are similar in
theoretical complexity, dot-product attention is much faster and more
space-efficient in practice, since it can be implemented using highly optimized
matrix multiplication code.

While for small values of $d_k$ the two mechanisms perform similarly, additive
attention outperforms dot product attention without scaling for larger values of
$d_k$ @britz2017massive. We suspect that for large values of $d_k$, the dot
products grow large in magnitude, pushing the softmax function into regions where
it has extremely small gradients#footnote[To illustrate why the dot products get
large, assume that the components of $q$ and $k$ are independent random variables
with mean $0$ and variance $1$. Then their dot product,
$q dot.c k = sum_(i=1)^(d_k) q_i k_i$, has mean $0$ and variance $d_k$.]. To
counteract this effect, we scale the dot products by $1 / sqrt(d_k)$.

=== Multi-Head Attention <sec-multihead>

Instead of performing a single attention function with $d_"model"$-dimensional
keys, values and queries, we found it beneficial to linearly project the queries,
keys and values $h$ times with different, learned linear projections to $d_k$,
$d_k$ and $d_v$ dimensions, respectively. On each of these projected versions of
queries, keys and values we then perform the attention function in parallel,
yielding $d_v$-dimensional output values. These are concatenated and once again
projected, resulting in the final values, as depicted in @fig-attn.

Multi-head attention allows the model to jointly attend to information from
different representation subspaces at different positions. With a single attention
head, averaging inhibits this.

$ op("MultiHead")(Q, K, V) &= op("Concat")("head"_1, ..., "head"_h) W^O \
  "where " "head"_i &= op("Attention")(Q W_i^Q, K W_i^K, V W_i^V) $

Where the projections are parameter matrices $W_i^Q in RR^(d_"model" times d_k)$,
$W_i^K in RR^(d_"model" times d_k)$, $W_i^V in RR^(d_"model" times d_v)$ and
$W^O in RR^(h d_v times d_"model")$.

In this work we employ $h = 8$ parallel attention layers, or heads. For each of
these we use $d_k = d_v = d_"model" \/ h = 64$. Due to the reduced dimension of
each head, the total computational cost is similar to that of single-head attention
with full dimensionality.

=== Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways:

- In "encoder-decoder attention" layers, the queries come from the previous
  decoder layer, and the memory keys and values come from the output of the
  encoder. This allows every position in the decoder to attend over all positions
  in the input sequence. This mimics the typical encoder-decoder attention
  mechanisms in sequence-to-sequence models such as @wu2016google
  @bahdanau2014neural @gehring2017convolutional.

- The encoder contains self-attention layers. In a self-attention layer all of the
  keys, values and queries come from the same place, in this case, the output of
  the previous layer in the encoder. Each position in the encoder can attend to all
  positions in the previous layer of the encoder.

- Similarly, self-attention layers in the decoder allow each position in the
  decoder to attend to all positions in the decoder up to and including that
  position. We need to prevent leftward information flow in the decoder to preserve
  the auto-regressive property. We implement this inside of scaled dot-product
  attention by masking out (setting to $-oo$) all values in the input of the
  softmax which correspond to illegal connections. See @fig-attn.

== Position-wise Feed-Forward Networks <sec-ffn>

In addition to attention sub-layers, each of the layers in our encoder and decoder
contains a fully connected feed-forward network, which is applied to each position
separately and identically. This consists of two linear transformations with a
ReLU activation in between.

$ op("FFN")(x) = max(0, x W_1 + b_1) W_2 + b_2 $

While the linear transformations are the same across different positions, they use
different parameters from layer to layer. Another way of describing this is as two
convolutions with kernel size 1. The dimensionality of input and output is
$d_"model" = 512$, and the inner-layer has dimensionality $d_"ff" = 2048$.

== Embeddings and Softmax

Similarly to other sequence transduction models, we use learned embeddings to
convert the input tokens and output tokens to vectors of dimension $d_"model"$. We
also use the usual learned linear transformation and softmax function to convert
the decoder output to predicted next-token probabilities. In our model, we share
the same weight matrix between the two embedding layers and the pre-softmax linear
transformation, similar to @press2016using. In the embedding layers, we multiply
those weights by $sqrt(d_"model")$.

== Positional Encoding

Since our model contains no recurrence and no convolution, in order for the model
to make use of the order of the sequence, we must inject some information about the
relative or absolute position of the tokens in the sequence. To this end, we add
"positional encodings" to the input embeddings at the bottoms of the encoder and
decoder stacks. The positional encodings have the same dimension $d_"model"$ as the
embeddings, so that the two can be summed. There are many choices of positional
encodings, learned and fixed @gehring2017convolutional.

In this work, we use sine and cosine functions of different frequencies:

$ "PE"_("pos", 2i) = sin("pos" \/ 10000^(2i \/ d_"model")), quad
  "PE"_("pos", 2i+1) = cos("pos" \/ 10000^(2i \/ d_"model")) $

where $"pos"$ is the position and $i$ is the dimension. That is, each dimension of
the positional encoding corresponds to a sinusoid. The wavelengths form a geometric
progression from $2 pi$ to $10000 dot.c 2 pi$. We chose this function because we
hypothesized it would allow the model to easily learn to attend by relative
positions, since for any fixed offset $k$, $"PE"_("pos" + k)$ can be represented as
a linear function of $"PE"_"pos"$.

We also experimented with using learned positional embeddings
@gehring2017convolutional instead, and found that the two versions produced nearly
identical results (see @tab-variations row (E)). We chose the sinusoidal version
because it may allow the model to extrapolate to sequence lengths longer than the
ones encountered during training.
