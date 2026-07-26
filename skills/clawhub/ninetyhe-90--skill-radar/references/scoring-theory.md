# Scoring Theory — Mathematical Foundations

## 1. Bayesian Decision Framework

The core question: Given query q and skill s, what is P(Relevant=1 | q, s)?

By Bayes' theorem:

```
P(R=1 | q, s) = P(q | R=1, s) * P(R=1 | s) / P(q | s)
```

Where:
- **P(R=1 | s)** = Prior: base probability this skill gets invoked by any query
  - In declarative routing: corresponds to `priority / 100`
  - In data-driven routing: corresponds to historical invocation frequency

- **P(q | R=1, s)** = Likelihood: if this skill IS relevant, how likely is this query?
  - In declarative routing: corresponds to `keyword_score + pattern_score`

- **P(q | s)** = Evidence: normalization factor (usually cancels in ranking)

## 2. Connection to BM25

BM25 score formula:

```
Score(q, s) = SUM_i IDF(t_i) * f(t_i, s) * (k1 + 1) / [f(t_i, s) + k1 * (1 - b + b * |s| / avgsl)]
```

Translation to our scenario:
- **Document d** = skill description text
- **Query q** = user query
- **IDF(t)** = the fewer skills a keyword appears in, the higher its discriminative power
- **Term frequency saturation** = diminishing returns when a keyword appears multiple times

## 3. Why We Use a Simplified Linear Model

The full Bayesian posterior in log-odds form:

```
log P(R=1 | q, s) / P(R=0 | q, s)
= log P(R=1) / P(R=0)                           <- log prior odds
+ SUM_i log P(feature_i | R=1) / P(feature_i | R=0)  <- log likelihood ratio per feature
```

Our scoring formula is a first-order linear approximation of this:

```
Score = W_kw * keyword_score + W_pat * pattern_score + W_int * intent_score
      + W_ctx * context_score + W_pri * priority_score
```

Each component maps to a posterior term:
- `keyword_score` approximates SUM of keyword likelihood ratios
- `pattern_score` approximates SUM of pattern likelihood ratios
- `priority_score` approximates log prior odds

## 4. Information-Theoretic Interpretation of BM25 Components

### 4.1 IDF as Surprise

IDF(t) = log(N / df(t)), where N = total skills, df(t) = skills containing term t.

This is the "surprise" (information content) of seeing term t in a skill description. Rare terms carry more information.

In our system:
- A keyword appearing in only 1 out of 50 skills has high discriminative power
- A keyword appearing in 30 out of 50 skills is nearly useless

### 4.2 TF Saturation

In standard BM25, term frequency is saturated: appearing 10 times is not 10x better than appearing once.

In our system:
- Each keyword is matched at most once in the query (binary TF)
- But keyword_score = hit_count / total_keywords, which naturally saturates at 1.0

## 5. Pattern Matching as Binary Evidence

When a regex pattern matches:
- The probability of this being a true match jumps significantly
- In Bayesian terms: P(pattern_match | R=1) >> P(pattern_match | R=0)
- Therefore the likelihood ratio is very high -> strong evidence

When no pattern matches:
- This is NOT strong negative evidence (the query might just use an expression the skill author didn't anticipate)
- Therefore pattern_score = 0 reduces the total but doesn't exclude

## 6. Anti-pattern as Hard Negative Evidence

- anti_pattern match -> P(R=1 | q, s) approximately 0
- This is a deliberate design choice: false negatives (missing a relevant skill) are preferred over false positives (triggering the wrong skill)
- Mathematically: we're setting an asymmetric loss function where the cost of incorrect activation >> cost of missed activation

## 7. Priority as Prior

priority/100 encodes the skill author's belief about base invocation probability:
- "My skill is general-purpose" -> high priority
- "My skill is very niche" -> low priority

This is a subjective prior, which is valid in Bayesian reasoning — the system allows it to be overridden by strong evidence (high keyword + pattern scores).

## 8. Threshold Strategies — Decision Theory

### 8.1 Fixed Threshold (Neyman-Pearson)

- Score > 0.30 -> recall
- Score <= 0.30 -> reject

Equivalent to setting a fixed decision boundary in score space. Optimizes for a specific false-positive rate.

### 8.2 Top-k (Resource-Constrained)

Always return exactly k results regardless of absolute score. Useful when:
- Context window is fixed (can only fit k skill descriptions)
- Prefer diversity over precision

### 8.3 Gap-Based (Confidence-Aware)

**Information-theoretic interpretation**: The gap between top-1 and top-2 scores approximates the "confidence" of the decision. Large gap -> low entropy -> confident decision; small gap -> high entropy -> need more information (let the LLM see both skills and choose).

```
if top1_score - top2_score > delta:
    return [top1]      # High confidence, single skill
else:
    return [r for r in results if r.score >= theta]  # Low confidence, let LLM choose
```

### 8.4 Pattern-Gate (Precision-First)

Only return results that matched at least one regex pattern. This is the most conservative strategy — demands explicit evidence before activation.

## 9. Score Fusion — Why Weighted Sum

When combining multiple signals, common approaches:
1. **Weighted sum** (our choice): Score = w1*s1 + w2*s2 + ...
2. **Weighted product**: Score = s1^w1 * s2^w2 * ...
3. **Rank fusion (RRF)**: Score = 1/(k + rank1) + 1/(k + rank2)
4. **Logistic regression**: Learned weights from labeled data

Why we chose weighted sum:
1. Cold-start scenario has no training data -> rules out logistic regression
2. Not a multi-retrieval fusion problem -> rules out RRF
3. Don't want a single zero signal to exclude -> rules out weighted product
4. Explainability is a core requirement -> weighted sum is most transparent

## 10. Calibration — Converting Scores to Probabilities

Raw scores from our formula are NOT probabilities. To convert:

### Platt Scaling (with sufficient data)

```
P(R=1 | score) = 1 / (1 + exp(A * score + B))
```

Where A, B are fitted from labeled data (query-skill pairs with known relevance).

### Isotonic Regression (non-parametric)

When the relationship between score and probability is non-linear, use isotonic regression to learn a monotonic mapping.

### In Practice (Cold Start)

Without labeled data, treat scores as relative rankings only. The threshold theta is then calibrated empirically:
- Start with theta = 0.30
- Monitor precision/recall in production
- Adjust based on user feedback

## 11. Progressive Enhancement with Usage Data

As usage data accumulates, the system can evolve:

```
Day 0:   Score = rule-based formula (this system)
Day N:   Score = rule-based + historical_frequency_bonus
Day N+M: P(R=1 | q, s) <- Bayesian update with observed outcomes
         P(R=1 | s) <- (alpha * historical_count / total_requests) + (1-alpha) * priority/100
```

This is the principled path from cold-start to learned routing — start with author declarations, gradually incorporate evidence.
