#import "neurips.typ": neurips

#show: neurips.with(
  title: "Attention Is All You Need",
  // Each author: (name, affiliation, email, note?). Empty affiliation is skipped;
  // `note` adds that author's own footnote (†, ‡, …). All share the * footnote.
  authors: (
    (name: "Ashish Vaswani",    affiliation: "Google Brain",          email: "avaswani@google.com"),
    (name: "Noam Shazeer",      affiliation: "Google Brain",          email: "noam@google.com"),
    (name: "Niki Parmar",       affiliation: "Google Research",       email: "nikip@google.com"),
    (name: "Jakob Uszkoreit",   affiliation: "Google Research",       email: "usz@google.com"),
    (name: "Llion Jones",       affiliation: "Google Research",       email: "llion@google.com"),
    (name: "Aidan N. Gomez",    affiliation: "University of Toronto",  email: "aidan@cs.toronto.edu",
      note: [Work performed while at Google Brain.]),
    (name: "Łukasz Kaiser",     affiliation: "Google Brain",          email: "lukaszkaiser@google.com"),
    (name: "Illia Polosukhin",  affiliation: "",                      email: "illia.polosukhin@gmail.com",
      note: [Work performed while at Google Research.]),
  ),
  authors-per-row: (4, 3, 1),  // rows of 4, 3, 1 — matches the published layout
  venue: [31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.],
  equal-contribution: [
    Equal contribution. Listing order is random. Jakob proposed replacing RNNs with
    self-attention and started the effort to evaluate this idea. Ashish, with Illia,
    designed and implemented the first Transformer models and has been crucially
    involved in every aspect of this work. Noam proposed scaled dot-product
    attention, multi-head attention and the parameter-free position representation
    and became the other person involved in nearly every detail. Niki designed,
    implemented, tuned and evaluated countless model variants in our original
    codebase and tensor2tensor. Llion also experimented with novel model variants,
    was responsible for our initial codebase, and efficient inference and
    visualizations. Lukasz and Aidan spent countless long days designing various
    parts of and implementing tensor2tensor, replacing our earlier codebase,
    greatly improving results and massively accelerating our research.
  ],
  abstract: [
    The dominant sequence transduction models are based on complex recurrent or
    convolutional neural networks that include an encoder and a decoder. The best
    performing models also connect the encoder and decoder through an attention
    mechanism. We propose a new simple network architecture, the Transformer, based
    solely on attention mechanisms, dispensing with recurrence and convolutions
    entirely. Experiments on two machine translation tasks show these models to be
    superior in quality while being more parallelizable and requiring significantly
    less time to train. Our model achieves 28.4 BLEU on the WMT 2014
    English-to-German translation task, improving over the existing best results,
    including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French
    translation task, our model establishes a new single-model state-of-the-art
    BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction
    of the training costs of the best models from the literature. We show that the
    Transformer generalizes well to other tasks by applying it successfully to
    English constituency parsing both with large and limited training data.
  ],
)

#include "introduction.typ"
#include "background.typ"
#include "model-architecture.typ"
#include "why-self-attention.typ"
#include "training.typ"
#include "results.typ"

= Conclusion

In this work, we presented the Transformer, the first sequence transduction model
based entirely on attention, replacing the recurrent layers most commonly used in
encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than
architectures based on recurrent or convolutional layers. On both WMT 2014
English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new
state of the art. In the former task our best model outperforms even all previously
reported ensembles.

We are excited about the future of attention-based models and plan to apply them to
other tasks. We plan to extend the Transformer to problems involving input and
output modalities other than text and to investigate local, restricted attention
mechanisms to efficiently handle large inputs and outputs such as images, audio and
video. Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at
#link("https://github.com/tensorflow/tensor2tensor").

*Acknowledgements.* We are grateful to Nal Kalchbrenner and Stephan Gouws for their
fruitful comments, corrections and inspiration.

#bibliography("references.bib", style: "association-for-computing-machinery", title: "References")

#include "visualizations.typ"
