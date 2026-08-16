# Leakage-Resistant Molecular ML Validation Protocol

## 1. Pre-register the claim

Before viewing test labels, record:

- endpoint and units;
- assay/species/construct restrictions;
- intended chemical and biological domain;
- classification threshold or regression transform;
- screening budget and primary metric;
- required novelty;
- split algorithm and random seed;
- model families and tuning budget;
- candidate-selection rule.

## 2. Curate before splitting

1. Parse structures.
2. Define parent/largest-fragment policy.
3. Normalize charges and aromaticity.
4. Define tautomer and stereochemistry policy.
5. Generate canonical parent identifiers.
6. Group exact duplicates, salts, tautomers, stereochemical variants as appropriate.
7. Resolve assay units and endpoint semantics.
8. Preserve censored qualifiers.
9. Aggregate replicates only after conflict review.
10. Keep all provenance fields.

A standardized parent must never cross train and test through duplicate rows.

## 3. Choose the outer split from deployment

### Random/stratified

Use only when future cases are random draws from the same chemical distribution. It is useful
for debugging but weak evidence for scaffold hopping.

### Scaffold

Groups Bemis–Murcko scaffolds. Better than random for many projects, but different scaffolds
can remain highly similar. Measure maximum train–test Tanimoto similarity.

### Structure-cluster

Cluster fingerprints and hold out complete clusters. Choose clustering and threshold without
using labels. Prefer this for novel-chemotype claims.

### Temporal

Train on measurements available before a cutoff and test later data. Preserve timestamp and
project history. This often best reflects prospective medicinal chemistry. If replicate or
conflicting records for one standardized parent span the cutoff, never let a target aggregate that
uses a later measurement enter the earlier training block. Quarantine that parent to the later
side (the bundled CLI uses its latest source timestamp), or pre-register another parent-level
policy that uses no future labels.

### Series/project

Hold out complete medicinal-chemistry series or projects. Useful when series identifiers are
available.

### DTI entity-cold

- drug-cold: no test drug in training;
- target-cold: no test target in training;
- both-cold: neither entity in training.

Random pair splits are insufficient for new-entity claims.

### External laboratory/source

Hold out a different lab, database, assay campaign, or organization. Confirm that endpoint
semantics remain comparable.

## 4. Keep all learned operations inside inner folds

The following operations leak if fitted before cross-validation:

- imputation;
- scaling;
- variance/correlation filtering when data-dependent;
- supervised feature selection;
- PCA;
- oversampling/undersampling;
- calibration;
- hyperparameter tuning;
- threshold optimization;
- learned representations.

Use a pipeline or explicitly fit each operation on the inner training fold.

## 5. Required baselines

- prevalence/mean/median;
- nearest-neighbor similarity;
- linear/logistic model;
- RF;
- SVM/SVR;
- GB/XGBoost.

Use the same outer molecules and comparable tuning budgets.

## 6. Metrics

### Rare-active classification

Primary:

- average precision / PR-AUC;
- precision and recall at the exact test budget;
- hit rate;
- enrichment factor at 0.1%, 1%, or another budget-aligned fraction;
- MCC or balanced accuracy.

Secondary:

- ROC-AUC;
- sensitivity/specificity;
- calibration curve and Brier score;
- diversity and novelty of selected hits.

### Regression

- MAE;
- RMSE;
- R²;
- Spearman and optionally Kendall rank correlation;
- error by nearest-neighbor similarity, scaffold, response range, and domain;
- top-k recovery when ranking is the decision.

### Uncertainty

- empirical coverage at requested level;
- average interval width or prediction-set size;
- coverage by similarity/domain bin;
- calibration under the outer split, not only random CV.

## 7. Prevent leaderboard/test overfitting

- Treat the outer test as single-use.
- Do not choose features after viewing outer errors.
- Do not perform early stopping on the outer test.
- Do not repeatedly submit variants to a public leaderboard and report the best as unbiased.
- If test labels influenced development, rename the set validation and obtain a new test.

## 8. Applicability domain

Report multiple complementary checks:

1. nearest training Tanimoto;
2. descriptor range or robust distance;
3. local training density;
4. known structural/target/assay exclusions;
5. ensemble or conformal uncertainty;
6. response-range warning.

A compound can be structurally in-domain but mechanistically out-of-domain.

## 9. Interpretation stability

- calculate explanations per fold/seed;
- compare RF permutation importance and boosted-tree SHAP;
- group correlated descriptors;
- map fingerprint bits to structures;
- test whether the feature tracks series identity or nuisance variables;
- report unstable explanations as unstable;
- seek experimental confirmation.

## 10. Prospective validation

Freeze:

- library version;
- model and environment hash;
- selection threshold;
- diversity algorithm;
- number of compounds;
- counter-screen plan.

Report every tested compound and outcome where licensing permits. Do not report only confirmed
hits.

## 11. Minimum model card

- intended use and prohibited uses;
- training data and licenses;
- endpoint and curation;
- representation;
- split and similarity distribution;
- algorithm and hyperparameters;
- primary/secondary metrics with uncertainty;
- calibration and domain;
- known biases and failure modes;
- model/software versions;
- prospective evidence status.

## 12. Regulatory alignment

For regulatory-facing QSAR, document the OECD principles:

1. defined endpoint;
2. unambiguous algorithm;
3. defined applicability domain;
4. goodness-of-fit, robustness, and predictivity;
5. mechanistic interpretation where possible.

Also ensure correct input, in-domain substance, reliable prediction, and fitness for the intended
regulatory purpose.
