# Algorithm Guide: RF, SVM/SVR, and Gradient Boosting for Drug Discovery

## 1. Random Forest

### Mechanism

Random Forest trains many decorrelated decision trees on bootstrap samples. At each split, a
random feature subset is considered. Classification aggregates votes/probabilities; regression
averages tree outputs:

\[
\hat f(x)=B^{-1}\sum_{b=1}^{B}T_b(x).
\]

The method primarily reduces the variance of a single deep tree.

### Best uses

- first nonlinear QSAR/QSPR baseline;
- ECFP/Morgan or descriptor activity prediction;
- ADMET/toxicity classification and regression;
- active/decoy screening;
- protein–ligand scoring (RF-Score family);
- exploratory feature ranking;
- active learning with ensemble disagreement.

### Strengths

- little need for scaling;
- nonlinear and interaction-aware;
- tolerates irrelevant and correlated variables better than many linear models;
- trees train in parallel;
- handles classification, regression, and multi-output tasks;
- out-of-bag diagnostics and permutation importance are available.

### Limitations

- weak extrapolation outside observed feature/response space;
- stepwise regression surfaces;
- impurity importance favors some feature types and is distorted by correlation;
- out-of-bag estimates do not simulate novel chemical series;
- probabilities can be miscalibrated;
- large/deep forests consume memory.

### Tuning priorities

1. minimum samples per leaf;
2. maximum features per split;
3. maximum depth;
4. class weights or balanced sampling;
5. number of trees until estimates stabilize.

Starting search:

- `n_estimators`: 500, 1000, 2000;
- `max_features`: `sqrt`, `log2`, 0.1, 0.25, 0.5;
- `min_samples_leaf`: 1, 2, 5, 10, 20;
- `max_depth`: None, 8, 16, 32;
- `class_weight`: None, `balanced`, custom.

## 2. Support Vector Machine / Regression

### Mechanism

A soft-margin SVM minimizes model norm and margin violations:

\[
\min_{w,b,\xi}\;\frac{1}{2}\|w\|^2+C\sum_i\xi_i
\]

subject to

\[
y_i(w^T\phi(x_i)+b)\ge1-\xi_i.
\]

A kernel computes inner products in the transformed feature space without explicitly forming it.
SVR uses an epsilon-insensitive regression loss.

### Best uses

- small/medium datasets with more features than compounds;
- sparse fingerprint classification with linear SVM;
- nonlinear QSAR with RBF or validated chemistry kernels;
- potency/property regression with SVR;
- ligand-based and structure-based virtual screening;
- pairwise drug–target kernels;
- SVM-based conformal prediction and Venn–Abers calibration.

### Strengths

- strong high-dimensional generalization within domain;
- convex optimization for a fixed kernel;
- custom kernels can encode chemical similarity;
- only support vectors determine the decision function;
- linear SVM scales well for very sparse vectors.

### Limitations

- continuous features require leakage-safe scaling;
- C, gamma, epsilon, and kernel require tuning;
- nonlinear kernel training/memory scale poorly with sample count;
- no native probabilities;
- nonlinear models are difficult to interpret;
- custom similarities may not be valid positive-semidefinite kernels.

### Tuning priorities

- compare linear and RBF kernels before exotic kernels;
- search `C` on a log scale from about 1e-3 to 1e3;
- search RBF `gamma` from roughly 1e-6 to 1e1 after scaling;
- tie SVR epsilon to assay noise, often 0.01–0.5 transformed units;
- tune class weights against the decision metric;
- calibrate probabilities on inner/cross-validation predictions.

## 3. Gradient Boosting

### Mechanism

Gradient boosting adds weak trees sequentially:

\[
F_m(x)=F_{m-1}(x)+\eta h_m(x),
\]

where each tree approximates the negative gradient of the loss. It primarily reduces bias while
regularization limits variance.

### Implementations

#### scikit-learn GradientBoosting

Reference stagewise tree boosting. Suitable for modest dense tables. It lacks many scalability
and regularization features of modern packages.

#### XGBoost

Adds a regularized objective, second-order updates, sparse-aware split finding, row/column
subsampling, parallel construction, and mature CPU/GPU interfaces. Usually the first boosted
model to benchmark for QSAR accuracy.

#### LightGBM

Uses histogram splits, gradient-based one-side sampling, exclusive feature bundling, and
leaf-wise growth. Often fastest for large sparse tables. Constrain leaves/depth and minimum leaf
samples to avoid small-data overfit.

#### CatBoost

Uses ordered boosting and target statistics for categorical features. Useful when molecular
features are combined with legitimate categorical context such as assay, species, target family,
or protocol. Such categories can also leak, so splitting must block shortcuts.

### Best uses

- medium/large molecular descriptor or fingerprint tables;
- ADMET/toxicity endpoint prediction;
- ligand-based virtual screening;
- drug–target/network feature fusion;
- docking rescoring;
- ranking and multi-objective surrogate models;
- feature-interaction discovery.

### Strengths

- excellent structured-data accuracy;
- nonlinear interactions;
- handles sparse inputs and missing values in modern implementations;
- class/sample weights and custom objectives;
- regularization, row/column sampling, and early stopping;
- fast inference and scalable training.

### Limitations

- larger tuning burden than RF;
- sequential rounds can fit assay noise;
- tree models extrapolate poorly;
- gain and SHAP rankings can change across implementations and hyperparameters;
- early stopping can leak if it uses the final test;
- class imbalance requires explicit metrics and weights.

### Tuning priorities

- learning rate: about 0.01–0.2;
- rounds: large cap with inner early stopping;
- depth/leaves: shallow to moderate;
- row subsampling: 0.5–1.0;
- column subsampling: 0.3–1.0;
- minimum child/leaf size and split gain;
- L1/L2 regularization;
- positive-class weight;
- objective and metric aligned to deployment.

## 4. Bagging versus boosting

| Property | Random Forest | Gradient Boosting |
|---|---|---|
| Tree relationship | Independent randomized trees | Sequential error-correcting trees |
| Main statistical effect | Variance reduction | Bias reduction with regularization |
| Parallelism | Across trees | Mostly inside each boosting round |
| Tuning | Moderate | Higher |
| Noise behavior | Often robust | Can chase noise if under-regularized |
| Typical result | Strong safe baseline | Often higher tabular accuracy |

## 5. Representation interactions

| Feature type | RF | SVM/SVR | GB/XGBoost |
|---|---|---|---|
| Morgan bits | Strong | Strong, especially linear | Strong; use sparse input where supported |
| Morgan counts | Strong | Scale/normalize when appropriate | Strong |
| Compact descriptors | Strong | Standardize | Strong |
| Thousands of correlated descriptors | Robust baseline; clean obvious defects | Scale and feature-select inside folds | Regularize and subsample columns |
| Docking terms | Strong | Strong with scaling | Strong |
| PLEC/contact fingerprints | RF-Score-like | Effective target-specific scorer | Effective with enough data |
| Network/omics features | Strong | Strong after scaling | Strong feature fusion |

## 6. Selection rule

No algorithm wins universally. Select the complete pipeline under an outer split matching the
claim. The winner should improve the decision-relevant metric over nearest-neighbor and simple
baselines, remain calibrated/domain-aware, and survive an external or prospective test.
