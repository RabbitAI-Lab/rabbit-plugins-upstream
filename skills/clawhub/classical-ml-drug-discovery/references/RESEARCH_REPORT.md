# Random Forests, Support Vector Machines, and Gradient Boosting in Drug Discovery

**Deep-research report**  
**Research cut-off:** 13 August 2026  
**Scope:** How Random Forests (RF), Support Vector Machines/Support Vector Regression (SVM/SVR), and Gradient-Boosted Decision Trees (GBDT; especially XGBoost, LightGBM, and CatBoost) are used in small-molecule drug discovery; the open-source software, model hubs, and web services that implement or support these methods.

> **Scientific-use warning:** These methods rank hypotheses and prioritize experiments. A high model score is not proof of binding, efficacy, selectivity, safety, or clinical utility. Predictions should be checked against the model's applicability domain, then validated with orthogonal computation and prospective experiments.

---

## Table of contents

1. [Executive summary](#1-executive-summary)
2. [Where these algorithms fit in drug discovery](#2-where-these-algorithms-fit-in-drug-discovery)
3. [From molecules to machine-learning tables](#3-from-molecules-to-machine-learning-tables)
4. [Random Forests](#4-random-forests)
5. [Support Vector Machines and Support Vector Regression](#5-support-vector-machines-and-support-vector-regression)
6. [Gradient Boosting](#6-gradient-boosting)
7. [Direct comparison](#7-direct-comparison)
8. [Applications across the discovery pipeline](#8-applications-across-the-discovery-pipeline)
9. [A rigorous end-to-end workflow](#9-a-rigorous-end-to-end-workflow)
10. [Validation, leakage, interpretation, and uncertainty](#10-validation-leakage-interpretation-and-uncertainty)
11. [Open-source software](#11-open-source-software)
12. [Open-source or open-access websites](#12-open-source-or-open-access-websites)
13. [Recommended tool stacks](#13-recommended-tool-stacks)
14. [Practical starting ranges for model development](#14-practical-starting-ranges-for-model-development)
15. [Research gaps and future directions](#15-research-gaps-and-future-directions)
16. [Conclusions](#16-conclusions)
17. [Glossary](#17-glossary)
18. [References](#18-references)

---

## 1. Executive summary

### Main conclusions

1. **RF, SVM, and gradient boosting remain highly relevant even in the deep-learning era.** They are strong baselines and often strong production models when drug-discovery data are tabular, high-dimensional, noisy, imbalanced, and modest in size. The 2022 review of SVM in chemoinformatics describes it as a long-standing state-of-the-art approach for compound classification, molecular-property prediction, and virtual screening [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9325859/). A large 2023 benchmark trained 157,590 gradient-boosting models across 16 datasets, 94 endpoints, and about 1.4 million compounds, finding XGBoost generally most predictive and LightGBM fastest [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/).

2. **The molecular representation and validation design can matter as much as, or more than, the learner.** The same algorithm can behave very differently with ECFP/Morgan fingerprints, physicochemical descriptors, protein–ligand contact features, docking energy terms, or biological-network features. MoleculeNet emphasized that chemical-data splitting and featurization are integral parts of a benchmark, and that random splitting is often inappropriate for chemical data [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/).

3. **Random Forest is usually the safest first nonlinear baseline.** RF handles mixed and nonlinear signals, usually needs little preprocessing, tolerates many irrelevant descriptors, trains trees in parallel, supports classification and regression, and provides out-of-bag estimates and feature-importance measures. Its main weaknesses are stepwise predictions, weak extrapolation, potentially biased or unstable importance scores, and overoptimistic validation when analogues leak across splits.

4. **SVM/SVR is especially useful for small-to-medium, high-dimensional datasets.** It can operate effectively when the number of molecular features is large relative to the number of compounds, and kernels can express nonlinear molecular similarity. It requires careful scaling, kernel and hyperparameter selection, and probability calibration. Kernel SVM training becomes expensive as the compound count grows.

5. **Gradient boosting is often the strongest choice for structured molecular features at medium-to-large scale.** It builds trees sequentially to correct previous errors. XGBoost adds regularization and optimized training; LightGBM prioritizes speed and large sparse datasets; CatBoost uses ordered boosting and is useful when genuine categorical variables are present. On large QSAR benchmarks, XGBoost often gives the best accuracy, while LightGBM can be dramatically faster [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/).

6. **These models are used throughout discovery, not only for classic QSAR.** Applications include target/druggability prediction, drug–target interaction prediction, ligand-based virtual screening, docking rescoring, binding-affinity estimation, ADMET and toxicity prediction, lead optimization, drug repurposing, phenotypic-screen analysis, active learning, and experimental-batch selection.

7. **Retrospective performance is not prospective evidence.** RF-Score-VS produced much better retrospective early enrichment than AutoDock Vina on DUD-E, but such results are benchmark- and split-dependent [7](https://www.nature.com/articles/srep46710). Recent work shows that even scaffold splits can remain optimistic because compounds with different Bemis–Murcko scaffolds can still be very similar; cluster, temporal, and true external/prospective tests are preferable when they reflect the intended deployment [16](https://arxiv.org/abs/2406.00873).

8. **A strong open-source stack is already available.** A practical coding stack is **RDKit + scikit-learn + XGBoost/LightGBM + SHAP**, optionally managed through **DeepChem, DeepMol, AMPL, QSARtuna, QSPRpred, ZairaChem, or Flame**. Specialized choices include **ODDT/RF-Score-VS** for structure-based rescoring, **CPSign** for SVM-based conformal prediction, **OPERA** for transparent physicochemical/ADMET/toxicity QSAR predictions, and **QSAR-Co-X** for multi-target classification.

9. **Useful open web interfaces exist.** As of the research date, **QSAR in the Browser (QITB)** runs RF and XGBoost locally in the browser; **ADMETboost** exposes XGBoost ADMET models; **OCHEM** provides online data/model building; **EPA CompTox** exposes OPERA-derived predictions; **TDC** provides datasets and benchmarks; and the **Ersilia Model Hub** distributes pretrained models. Website availability, model versions, and licenses must be rechecked before production use.

### One-sentence selection guide

- **Start with RF** when you need a robust, low-friction baseline.
- **Add SVM/SVR** when data are small or medium and features are high-dimensional, after scaling and kernel tuning.
- **Add XGBoost** when predictive accuracy on structured features is the priority.
- **Try LightGBM** when the dataset is very large or iteration speed matters.
- **Use CatBoost** when meaningful categorical variables accompany molecular features or when ordered boosting helps small-data stability.
- **Select the winner only under deployment-relevant splits and metrics**, not by random cross-validation alone.

---

## 2. Where these algorithms fit in drug discovery

A conventional small-molecule discovery program repeatedly asks variants of four questions:

1. **What should be targeted?** Predict whether a protein is druggable, whether a compound interacts with a target, or whether a perturbation is therapeutically relevant.
2. **Which compounds should be tested?** Rank a virtual library by predicted activity, binding, phenotype, or novelty.
3. **Which hits should be optimized?** Predict potency, selectivity, physicochemical properties, ADME, toxicity, and developability.
4. **Which predictions are reliable enough to act on?** Estimate uncertainty, applicability domain, calibration, and prospective value.

RF, SVM, and gradient boosting are supervised-learning methods that map a feature vector \(x\) to a categorical or numerical endpoint \(y\):

- **Classification:** active/inactive, toxic/non-toxic, permeable/non-permeable, binder/non-binder.
- **Regression:** pIC50, pKi, solubility, logD, clearance, half-life, permeability, binding affinity, or a phenotypic readout.
- **Ranking:** order compounds so that experimentally valuable compounds occur early in a screened list.
- **Multi-task or multi-target modeling:** predict several endpoints or target activities, either with separate models, transformed task identifiers, or algorithms that support multiple outputs.

### Typical placement in a discovery cascade

```text
Public and internal assay data
        ↓
Structure/assay curation and endpoint harmonization
        ↓
Molecular, protein, complex, or biological-network featurization
        ↓
RF + SVM/SVR + XGBoost/LightGBM baselines
        ↓
Deployment-relevant validation and applicability-domain analysis
        ↓
Virtual library scoring and diversity-aware selection
        ↓
Docking / orthogonal models / medicinal-chemistry review
        ↓
Biochemical, cellular, ADME, and toxicity experiments
        ↓
Model update through active learning or design–make–test–analyze cycles
```

The models are therefore **decision-support components**, not replacements for target biology, medicinal chemistry, pharmacology, or experimental confirmation.

---

## 3. From molecules to machine-learning tables

The algorithms discussed here do not natively understand a SMILES string, a molecular graph, a protein sequence, or a crystal structure. They require numerical features. Feature generation is consequently a central scientific choice.

### 3.1 Common input representations

| Representation | Examples | What it captures | Typical suitability |
|---|---|---|---|
| **2D circular fingerprints** | ECFP/Morgan bit or count vectors | Local atom environments and substructures | Excellent baseline for RF, linear/RBF SVM, XGBoost; sparse and fast |
| **Structural keys** | MACCS, PubChem keys | Presence/absence of predefined patterns | Interpretable, compact baseline; may miss task-specific motifs |
| **Path/atom-pair fingerprints** | RDKit path, atom-pair, topological torsion | Bond paths and pair relationships | Useful when circular fingerprints miss longer-range topology |
| **Physicochemical descriptors** | molecular weight, logP, TPSA, H-bond counts, rotatable bonds | Global drug-like properties | Useful for ADMET, property prediction, and interpretation |
| **Large descriptor panels** | RDKit, Mordred, PaDEL | Topological, constitutional, fragment, charge, and optional 3D descriptors | Strong for RF/GB/SVR, but require curation, missing-value handling, and leakage-safe feature selection |
| **Docking and complex features** | Vina terms, atom-pair contact counts, protein–ligand extended-connectivity fingerprints (PLEC) | Geometry and interactions in a modeled complex | Structure-based rescoring and affinity prediction |
| **Protein features** | sequence composition, domains, embeddings, structure/pocket descriptors | Target identity and similarity | Drug–target interaction, target family, and druggability models |
| **Biological-network features** | graph paths, random-walk scores, omics/perturbation features | Context beyond chemical structure | Repurposing, DTI prediction, phenotypic response, target nomination |

RDKit is a widely used open-source source of 2D/3D operations, fingerprints, and descriptors [18](https://www.rdkit.org/docs/Overview.html). Mordred supplies a large open descriptor set [19](https://github.com/mordred-descriptor/mordred), and PaDEL remains common in published QSAR workflows, although its original implementation is old and wrappers/forks must be checked carefully.

### 3.2 Endpoint construction is part of the model

A technically strong algorithm cannot repair a poorly defined endpoint. Important choices include:

- Use one assay type, target construct, species, and measurement definition where possible.
- Convert units consistently before transformations.
- For molar potency, \(\mathrm{pIC}_{50}=-\log_{10}(\mathrm{IC}_{50}[M])\), but IC50, Ki, Kd, and EC50 are not interchangeable.
- Preserve assay conditions and qualifiers such as `<`, `>`, or approximate measurements.
- Aggregate replicates using a documented robust rule; investigate large disagreements instead of averaging blindly.
- Do not label untested compounds as inactive unless the modeling assumption is explicit and validated.
- If converting a continuous assay to active/inactive classes, justify the threshold and inspect compounds near it; binarization discards information and can create contradictory labels around the cutoff.
- Prevent the same parent structure, salt form, stereochemical variant, or near-duplicate from entering both training and test sets.

### 3.3 Representation and learner should be selected together

A model comparison is not only “RF versus SVM versus XGBoost.” It is a comparison of complete pipelines:

```text
curation + split + feature generator + preprocessing + learner + calibration + metric
```

For example:

- RBF-SVM on continuous descriptors normally needs scaling; RF generally does not.
- A linear SVM can be very strong on large sparse fingerprint vectors.
- XGBoost can exploit nonlinear interactions among global descriptors and fingerprint bits.
- RF can use the same features with fewer tuning decisions and provide a robust benchmark.
- Complex-based features can change a ligand-only QSAR task into a structure-based scoring task.

MoleculeNet's principal contribution was not merely a model leaderboard; it standardized datasets, featurizers, splitters, metrics, and implementations in DeepChem [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/).

---

## 4. Random Forests

### 4.1 How RF works

A Random Forest is an ensemble of decision trees. Each tree is trained on a bootstrap sample, and a random subset of features is considered at each split. For regression, predictions are averaged; for classification, votes or class probabilities are averaged:

\[
\hat f_{RF}(x)=\frac{1}{B}\sum_{b=1}^{B}T_b(x)
\]

where \(B\) is the number of trees and \(T_b\) is one tree. Random sampling decorrelates the trees, so averaging reduces the high variance of an individual tree. Breiman's original paper formalized the method [1](https://doi.org/10.1023/A:1010933404324). Svetnik and colleagues established RF as an important QSAR method by applying it to six cheminformatics datasets and emphasizing prediction, out-of-bag assessment, descriptor importance, and compound proximity [4](https://doi.org/10.1021/ci034160g).

### 4.2 Why RF fits drug-discovery data

RF is attractive because it:

- captures nonlinear effects and feature interactions without specifying their form;
- accepts binary fingerprints and continuous descriptors;
- is mostly insensitive to monotonic scaling;
- tolerates correlated and irrelevant predictors better than many linear models;
- works well on small-to-medium datasets, although extremely small datasets remain unstable;
- supports class weights and balanced variants for rare actives;
- trains trees in parallel;
- provides out-of-bag predictions, proximity measures, and feature-importance estimates.

### 4.3 Drug-discovery uses

#### Ligand-based QSAR and virtual screening

RF learns the relationship between molecular fingerprints/descriptors and an activity label or potency value. It is often used to rank ChEMBL, PubChem, ZINC, Enamine, or internal libraries before experimental screening.

#### ADMET and toxicity

RF models are common for aqueous solubility, permeability, plasma protein binding, BBB penetration, CYP inhibition/substrate status, hERG risk, Ames mutagenicity, hepatotoxicity, and acute toxicity. They are useful when endpoints are driven by nonlinear combinations of size, polarity, lipophilicity, charge, and structural alerts.

#### Structure-based scoring

RF can learn binding affinity or active/decoy discrimination from protein–ligand contact features and docking terms. The 2010 RF-Score study used RF to learn binding affinity from protein–ligand atom-pair contacts and demonstrated competitive performance on PDBbind [6](https://academic.oup.com/bioinformatics/article/26/9/1169/199938).

RF-Score-VS subsequently trained on 15,426 active and 893,897 inactive docked molecules across 102 targets. In a retrospective DUD-E study, the top 1% selected by RF-Score-VS contained a reported 55.6% actives versus 16.2% for Vina; at the top 0.1%, the reported rates were 88.6% versus 27.5%. It also improved affinity correlation in that benchmark [7](https://www.nature.com/articles/srep46710). These numbers demonstrate potential, but they should not be transferred to a new target or library without target-relevant validation.

#### Feature selection and chemical interpretation

RF's impurity or permutation importance can prioritize descriptors and fingerprint bits for further analysis. This is useful for generating hypotheses about fragments or physicochemical drivers, but importance is not causal evidence.

#### Active learning

An RF ensemble can rank an untested pool by predicted activity and uncertainty proxies such as tree variance. A batch can then be selected by combining predicted value, uncertainty, and chemical diversity. After assay results return, the model is retrained.

### 4.4 Strengths

- Strong default baseline with relatively modest tuning.
- Little need for feature scaling.
- Nonlinear and interaction-aware.
- Parallelizable and generally stable as tree count increases.
- Handles multi-output problems in common libraries.
- Useful diagnostics through out-of-bag predictions and permutation importance.
- Reasonably fast prediction for large screening libraries.

### 4.5 Limitations

1. **Weak extrapolation.** Tree ensembles divide observed feature space into regions. Regression predictions generally do not extrapolate smoothly beyond the training response range.
2. **Analogue dependence.** High performance can reflect close analogues rather than transferable SAR. This must be tested with cluster, scaffold, time, or external splits.
3. **Importance bias.** Mean-decrease-in-impurity importance can favor continuous or high-cardinality variables; correlated descriptors divide or distort importance. Prefer held-out permutation importance, grouped permutation, SHAP with caution, and stability analysis across resamples.
4. **Stepwise prediction surfaces.** Smooth potency trends can be represented less efficiently than by suitable kernels or continuous models.
5. **Class probability calibration.** Averaged tree probabilities are not guaranteed to be calibrated. Check reliability curves and Brier score; use leakage-safe calibration if decisions depend on absolute probabilities.
6. **Out-of-bag is not a deployment simulation.** OOB samples may remain close analogues of bootstrap training compounds. OOB accuracy does not replace a chemical-series or temporal holdout.
7. **Large memory footprint.** Thousands of deep trees on wide descriptor matrices can be large, though still manageable in many QSAR settings.

### 4.6 When RF is the preferred first choice

Use RF first when the dataset is tabular, nonlinear, no larger than a typical QSAR corpus, and you need a reliable benchmark quickly. It is also a good choice when preprocessing must be simple, interpretability is exploratory rather than mechanistic, or the team needs a CPU-friendly model.

---

## 5. Support Vector Machines and Support Vector Regression

### 5.1 How SVM works

For binary classification, a soft-margin SVM chooses a separating hyperplane with a large margin while penalizing violations:

\[
\min_{w,b,\xi}\;\frac{1}{2}\lVert w\rVert^2+C\sum_i\xi_i
\]

subject to

\[
y_i(w^T\phi(x_i)+b)\geq 1-\xi_i,\quad \xi_i\geq0.
\]

The transformation \(\phi\) can be implicit through a kernel \(K(x_i,x_j)\), such as linear, polynomial, radial-basis-function (RBF), Tanimoto, or other chemistry-aware similarity kernels. Only points that define or violate the margin—the support vectors—determine the final decision function. Cortes and Vapnik's foundational formulation introduced maximal-margin classification, soft margins, and kernel-based nonlinear decision surfaces [2](https://doi.org/10.1007/BF00994018).

SVR replaces class separation with an epsilon-insensitive regression objective: errors inside an \(\varepsilon\)-wide tube are not penalized, while larger deviations are.

### 5.2 Why SVM fits drug-discovery data

SVM is particularly suitable when:

- compounds are represented by thousands of sparse fingerprint bits or descriptors;
- sample count is limited compared with feature count;
- the active/inactive boundary is nonlinear;
- a chemically meaningful similarity can be encoded in a kernel;
- robust margin-based classification is more important than direct mechanistic interpretation.

The 2022 review documents SVM use for classification, ranking, property prediction, activity cliffs, multi-target prediction, orphan targets, and virtual screening [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9325859/).

### 5.3 Drug-discovery uses

#### Activity classification and potency regression

SVC predicts active/inactive status; SVR predicts pIC50, pKi, solubility, pKa, clearance, and other continuous endpoints. SVM can perform particularly well with carefully scaled descriptor panels or chemistry-specific kernels.

#### Ligand-based virtual screening

SVM decision scores can rank a large library. A classic prospective COX-2 study trained SVM classifiers on pharmacophore-point triangles; retrospective screening placed 50–90% of known actives within the top 0.1%, and a prospectively tested benzimidazole showed 0.2 μM cellular activity [8](https://pubs.acs.org/doi/abs/10.1021/jm050619h).

A separate HDAC1 study built SVM and kNN QSAR models, screened about 9.5 million structures, experimentally tested four novel-scaffold consensus hits, and confirmed three as HDAC1 actives; the most active had an IC50 of 1 μM [9](https://pubs.acs.org/doi/abs/10.1021/ci800366f).

#### Structure-based scoring

SVM can learn from protein–ligand atom-pair potentials, interaction fingerprints, or docking energy components. In a target-specific SVM-SP study, 1,125 compounds were screened against EGFR and CaMKII; three of the top EGFR candidates inhibited EGFR at 58, 2, and 10 μM and had low similarity to known EGFR inhibitors [10](https://pmc.ncbi.nlm.nih.gov/articles/PMC3092157/).

#### Drug–target interaction and multi-target modeling

Compound and protein similarities can be combined in pairwise kernels. The classifier then distinguishes known drug–target pairs from negative or unlabeled pairs. Linear combinations of target-specific SVMs can support multi-class or multi-target predictions [5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9325859/).

#### Activity-cliff modeling

Matched molecular-pair kernels and SVR can model pairs of close analogues with unexpectedly large potency differences. This is a specialized use in which pair representations can be more informative than treating each molecule independently.

#### Conformal prediction

SVM is a common base learner for conformal classification and regression. CPSign combines chemical signatures, LIBSVM/LIBLINEAR, conformal prediction, and Venn–Abers probability estimation to produce prediction sets, intervals, or calibrated probabilities [31](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214261/).

### 5.4 Strengths

- Strong on small-to-medium, high-dimensional datasets.
- Convex optimization for a fixed kernel gives a well-defined optimum.
- Flexible nonlinear modeling through kernels.
- Can directly encode molecular similarity.
- Margin maximization often generalizes well within the represented chemical domain.
- Linear SVM is efficient for very sparse, high-dimensional fingerprints.
- SVR supports continuous properties without discretization.

### 5.5 Limitations

1. **Scaling sensitivity.** Continuous descriptors must normally be standardized inside each training fold. Scaling before splitting leaks information.
2. **Kernel and hyperparameter sensitivity.** \(C\), \(\gamma\), kernel type, and SVR \(\varepsilon\) can change results substantially. They require nested or otherwise leakage-safe tuning.
3. **Kernel SVM scalability.** Training time and kernel-matrix memory can become prohibitive for hundreds of thousands or millions of compounds. Linear SVM, kernel approximation, or tree boosting may be preferable at that scale.
4. **No native probabilities.** SVM decision values are margins. Platt scaling, isotonic regression, or Venn–Abers calibration should use separate or cross-validated calibration data.
5. **Limited direct interpretation.** A linear SVM has coefficients, but nonlinear kernels do not produce simple fragment rules. Post-hoc explanations must be treated cautiously.
6. **Support-vector-heavy models.** If many compounds become support vectors, inference and storage grow.
7. **Kernel validity.** A custom similarity is not automatically a valid positive-semidefinite kernel. Empirical performance alone does not eliminate numerical or theoretical issues.

### 5.6 When SVM is preferred

Choose SVM/SVR when data are relatively small, features are wide, the problem has a plausible kernel geometry, or a conformal-prediction workflow is required. Prefer linear SVM for very sparse fingerprints at larger scale; prefer RBF or chemistry kernels when nonlinear boundaries are expected and the dataset is not too large.

---

## 6. Gradient Boosting

### 6.1 How gradient boosting works

Gradient boosting constructs an additive model. Starting from an initial prediction \(F_0\), each new weak learner—usually a shallow decision tree—fits the negative gradient of the loss, correcting the current ensemble:

\[
F_m(x)=F_{m-1}(x)+\eta h_m(x),
\]

where \(h_m\) is the new tree and \(\eta\) is the learning rate. Friedman formalized gradient descent in function space and tree boosting for regression and classification [3](https://doi.org/10.1214/aos/1013203451).

This differs fundamentally from RF:

- **RF/bagging:** trees are independently randomized and averaged, primarily reducing variance.
- **Boosting:** trees are fitted sequentially to errors, often reducing bias but requiring stronger regularization and tuning.

### 6.2 Important implementations

| Implementation | Key idea | Drug-discovery implication |
|---|---|---|
| **scikit-learn GradientBoosting** | Classical stagewise boosting | Good educational/reference implementation and smaller datasets; less optimized for very large sparse problems |
| **XGBoost** | Regularized objective, second-order optimization, sparse-aware implementation, row/column subsampling | Usually the first boosted-tree model to benchmark for QSAR accuracy |
| **LightGBM** | Histogram splits, leaf-wise growth, gradient-based sampling, exclusive-feature bundling | Fast iteration on large or sparse datasets; requires depth/leaf control to limit overfit |
| **CatBoost** | Ordered boosting and leakage-resistant categorical statistics | Useful when true categorical covariates accompany molecular data; categorical advantage is less important for all-numeric fingerprints |

XGBoost is Apache-2.0 licensed [22](https://github.com/dmlc/xgboost), LightGBM is MIT licensed [23](https://github.com/microsoft/LightGBM), and CatBoost is an open-source boosted-tree library [24](https://catboost.ai/).

### 6.3 Why gradient boosting fits drug discovery

Boosted trees:

- learn nonlinear interactions among fingerprints, descriptors, docking terms, and biological features;
- accept classification, regression, ranking, and custom losses;
- can handle sparse matrices and missing values in modern implementations;
- support class weighting and row/column subsampling;
- provide strong accuracy without learning a molecular representation end-to-end;
- scale to larger data than kernel SVM;
- support early stopping and efficient hyperparameter optimization.

Sheridan and colleagues compared XGBoost, RF, and single-task neural networks across 30 pharmaceutical QSAR datasets, establishing XGBoost as an efficient and competitive QSAR method [12](https://pubs.acs.org/doi/10.1021/acs.jcim.6b00591).

### 6.4 Drug-discovery uses

#### QSAR and virtual screening

XGBoost and LightGBM are used to predict target activity from fingerprints and descriptors, then rank libraries. A modern benchmark across 94 molecular endpoints found XGBoost generally strongest, while LightGBM was fastest; for datasets above 100,000 compounds, LightGBM was reported to train about 100 times faster than XGBoost and 50 times faster than CatBoost in that experimental setup [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/). These are benchmark-specific ratios, not universal speed guarantees.

#### ADMET and toxicity

ADMETboost combines multiple fingerprints/descriptors with XGBoost for 22 TDC ADMET endpoints [38](https://github.com/smu-tao-group/ADMET_XGBoost). The peer-reviewed paper reported historically high TDC leaderboard rankings [33](https://link.springer.com/article/10.1007/s00894-022-05373-8). The currently accessible web page states 11 first-place and 19 top-three tasks, while the paper abstract reported 18 first-place and 21 top-three tasks at publication time. This discrepancy illustrates why leaderboard versions, model versions, and access dates must be recorded rather than treating ranks as permanent facts.

Gradient boosting has also been used for hERG, Ames, DILI, BBB, solubility, clearance, plasma protein binding, CYP endpoints, maximum recommended daily dose, and multi-endpoint toxicology.

#### Drug–target interaction prediction

GBDT can combine drug similarity, target similarity, and heterogeneous-network path features. DTIGBDT used random-walk-updated similarities and path-category features, then a GBDT classifier to predict drug–target interactions; in the reported benchmark it achieved AUC 0.877 and AUPR 0.129, outperforming the compared methods [39](https://pmc.ncbi.nlm.nih.gov/articles/PMC6555260/). Such network benchmarks are highly sensitive to negative-sampling and entity leakage.

#### Structure-based rescoring

Tools such as deltaVinaXGB use boosted trees to combine Vina terms, solvent-accessible surface features, water effects, ligand stability, and other complex features [40](https://github.com/jenniening/deltaVinaXGB). These models may improve affinity ranking, but dependencies are older and their domain must be checked before use.

#### Feature selection and medicinal-chemistry hypotheses

Gain, split frequency, permutation importance, and SHAP can rank descriptors or fingerprint bits. However, the large gradient-boosting benchmark found that XGBoost, LightGBM, and CatBoost could rank features very differently, with overlap varying markedly by dataset [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/). Feature rankings should therefore be tested for stability and mapped back to chemistry before interpretation.

### 6.5 Strengths

- Often excellent predictive performance on tabular molecular data.
- Better scalability than kernel SVM.
- Rich regularization: learning rate, depth/leaves, row and column subsampling, L1/L2 penalties, minimum gain, and early stopping.
- Handles nonlinearities and interactions without explicit interaction engineering.
- Mature CPU/GPU implementations.
- Supports imbalance-aware weights and ranking objectives.
- Efficient prediction after training.

### 6.6 Limitations

1. **More tuning burden than RF.** Learning rate, rounds, tree depth/leaves, sampling, regularization, and class weights interact.
2. **Sequential overfitting.** Too many or too-deep trees can fit assay noise and chemical-series artifacts.
3. **Feature-importance instability.** Different implementations and hyperparameters can highlight different chemistry.
4. **Weak extrapolation.** Like RF, tree ensembles partition observed feature space and do not reliably extrapolate beyond it.
5. **Data leakage can produce spectacular but meaningless scores.** Target encoding, imputation, descriptor filtering, feature selection, oversampling, and tuning must happen inside each training fold.
6. **Class imbalance needs explicit treatment.** Accuracy and ROC-AUC alone can conceal poor rare-active retrieval.
7. **Categorical-feature advantages may not transfer.** CatBoost's categorical handling is less relevant when all features are numerical descriptors or binary fingerprint bits.

### 6.7 When gradient boosting is preferred

Use XGBoost as a high-performance baseline for medium-to-large structured molecular datasets. Use LightGBM when rapid iteration or very large sparse data dominate. Use CatBoost when categorical assay, protocol, cell-line, species, or target metadata are scientifically meaningful and leakage-safe, or when ordered boosting performs better on the task.

---

## 7. Direct comparison

| Criterion | Random Forest | SVM/SVR | Gradient Boosting |
|---|---|---|---|
| **Core principle** | Bag many randomized trees and average | Maximize margin or fit an epsilon-insensitive function in a kernel space | Add trees sequentially to reduce the loss |
| **Best data regime** | Small-to-medium tabular datasets | Small-to-medium, high-dimensional datasets; linear SVM scales further | Medium-to-large tabular/sparse datasets |
| **Scaling required** | Usually no | Usually yes for continuous features | Usually no |
| **Sparse fingerprints** | Good | Excellent for linear SVM; good for suitable kernels | Excellent in XGBoost/LightGBM |
| **Nonlinearity** | Native tree interactions | Kernel-dependent | Native tree interactions |
| **Training parallelism** | High across trees | Solver-dependent; kernel matrix can dominate | Sequential across boosting rounds, parallel inside tree construction |
| **Tuning burden** | Low-to-moderate | Moderate-to-high | Moderate-to-high |
| **Probability output** | Available but may need calibration | Not native; calibration required | Available but may need calibration |
| **Interpretability** | Feature importance, PDP/ALE, SHAP; unstable with correlations | Linear coefficients; nonlinear SVM harder to explain | Gain/permutation/SHAP; importance can be unstable |
| **Extrapolation** | Poor outside learned regions | Depends on kernel; still domain-limited | Poor outside learned regions |
| **Class imbalance** | Class weights, balanced RF, resampling | Class weights and margin tuning | Weights, scale_pos_weight, sampling, custom objectives |
| **Large datasets** | Good but memory can grow | Kernel SVM poor; linear SVM good | Usually strongest option |
| **Uncertainty** | Tree variance/quantile forests/conformal wrappers | Strong conformal ecosystem; margins are not probabilities | Ensembles, quantile objectives, conformal wrappers |
| **Typical first use** | Robust baseline | High-dimensional or custom-kernel benchmark | Accuracy-focused production baseline |

### No universally best algorithm

Model rank changes with endpoint, feature type, split, sample size, class imbalance, and optimization budget. A defensible study should compare all three families using:

- identical curated records;
- identical train/validation/test molecules;
- preprocessing contained within each fold;
- comparable tuning budgets;
- endpoint-appropriate metrics;
- repeated seeds or folds;
- external or prospective testing.

---

## 8. Applications across the discovery pipeline

### 8.1 Target identification and druggability

Protein sequence, domain, structural, interaction-network, and omics features can train RF, SVM, or GBDT classifiers to identify druggable proteins or target–disease relationships. This is an upstream use: the model predicts target suitability, not a compound's medicinal value. Network leakage is a major risk because related proteins and drugs may appear in both training and test pairs.

### 8.2 Drug–target interaction and polypharmacology

A DTI model can use:

- compound fingerprints;
- protein sequence/structure features;
- drug–drug and target–target similarity;
- known interaction-network paths;
- assay/context metadata.

SVM pairwise kernels and GBDT network-feature models are common. RF is also used for multi-target classification. Valid evaluation should include **drug-cold**, **target-cold**, or **both-cold** splits, not only random drug–target pairs.

### 8.3 Ligand-based virtual screening

This is the most common use. A target-specific model is trained on known actives and reliable inactives, then applied to a large library. The objective is usually **early enrichment**, not overall accuracy.

A strong selection step combines:

1. predicted activity or potency;
2. uncertainty/applicability domain;
3. chemical diversity or clustering;
4. novelty relative to known actives;
5. physicochemical and reactive-group filters;
6. synthesis/purchasability;
7. optional docking or shape/pharmacophore agreement.

### 8.4 Structure-based virtual screening and docking rescoring

RF and SVM were early successful machine-learning scoring functions. Gradient boosting later provided regularized alternatives. Features can include atom-type contact counts, PLEC fingerprints, docking energy components, solvent-accessible surface area, water-mediated contacts, and ligand strain.

Important distinction:

- **Affinity prediction:** regress a measured Kd/Ki/IC50-like value.
- **Pose scoring:** identify a near-native binding pose.
- **Virtual-screening classification/ranking:** separate actives from decoys/inactives.

A model strong at one objective may be weak at another. Training labels and evaluation must match the intended use.

### 8.5 ADMET and toxicity

Models predict properties that determine exposure and safety:

- absorption and permeability;
- oral bioavailability;
- lipophilicity, solubility, and ionization;
- BBB penetration and tissue distribution;
- plasma protein binding and volume of distribution;
- CYP inhibition/substrate status;
- clearance and half-life;
- hERG blockade;
- mutagenicity, DILI, acute toxicity, endocrine activity, and other hazards.

Classical models remain valuable because many individual ADMET datasets are too small for large neural networks and because descriptors provide chemically useful global information.

### 8.6 Hit-to-lead and lead optimization

Separate or multitask models predict potency, selectivity, and developability for proposed analogues. Optimization should be multi-objective: increasing potency while ignoring solubility, clearance, hERG, or synthesis can worsen the molecule. RF/GB surrogate models can be embedded in Bayesian optimization, genetic search, or enumeration-and-ranking workflows.

### 8.7 Drug repurposing

Approved or clinical compounds are scored against new targets or phenotypes using DTI, transcriptomic, network, and chemical features. The output is a prioritized hypothesis list. Indication plausibility also requires exposure, dose, tissue distribution, target engagement, and disease biology.

### 8.8 Phenotypic screening and patient/cell context

RF and boosting handle compound descriptors together with cell-line omics, assay metadata, or perturbation signatures. SVM can model high-dimensional transcriptomic features. Splits must prevent leakage across compounds, cell lines, plates, batches, or biological replicates.

### 8.9 Active learning and experimental design

These models can select the next compounds to test:

- **Exploitation:** highest predicted value.
- **Exploration:** high uncertainty or distant chemistry.
- **Diversity:** representatives from distinct clusters/scaffolds.
- **Multi-objective:** favorable potency, ADMET, novelty, and feasibility.

Active learning is most useful when new labels are produced in consistent assays and the model is updated quickly enough to influence the next experimental cycle.

---

## 9. A rigorous end-to-end workflow

### Step 1 — Define the decision, not merely the endpoint

Examples:

- “Select 100 purchasable compounds for a biochemical screen with at least 20 scaffold families.”
- “Predict pIC50 for analogues within the current lead series.”
- “Reject compounds with high hERG risk while preserving target potency.”

The deployment population, assay, selection budget, and cost of false positives/negatives determine the right split and metric.

### Step 2 — Acquire data with provenance

Common sources include ChEMBL [41](https://www.ebi.ac.uk/chembl/), PubChem BioAssay [42](https://pubchem.ncbi.nlm.nih.gov/), BindingDB [43](https://www.bindingdb.org/), TDC [14](https://tdcommons.ai/), PDBbind, and internal assays. Record database version, download date, query, target identifiers, assay fields, and exclusion rules.

### Step 3 — Curate chemistry and assays

- Parse and validate structures.
- Remove mixtures and unsupported organometallics if the featurizer cannot represent them.
- Standardize aromaticity, charges, tautomer policy, salts, and fragments.
- Preserve stereochemistry when it can affect activity.
- Canonicalize parent structures and deduplicate.
- Harmonize endpoint units and transforms.
- Resolve or flag conflicting replicates.
- Keep provenance and assay context.

### Step 4 — Freeze the external test design early

Choose the split that mimics use:

- **Temporal split:** train on earlier data, test on later measurements.
- **Series/project split:** hold out medicinal-chemistry series.
- **Cluster split:** hold out structurally dissimilar clusters.
- **Scaffold split:** better than random in many settings but not necessarily sufficient.
- **Drug/target-cold split:** for DTI generalization.
- **External dataset:** different laboratory, source, or campaign.

Do not inspect test labels during feature choice, threshold selection, or hyperparameter tuning.

### Step 5 — Build multiple representations

At minimum compare:

1. ECFP/Morgan bits or counts;
2. a compact interpretable descriptor set;
3. an expanded RDKit/Mordred/PaDEL descriptor panel after leakage-safe cleaning;
4. task-specific features such as PLEC or docking terms when structures exist.

### Step 6 — Establish simple and strong baselines

Include:

- class prevalence or mean/median predictor;
- nearest-neighbor or similarity search;
- linear/logistic regression;
- RF;
- linear and/or RBF SVM/SVR;
- XGBoost and optionally LightGBM/CatBoost.

A sophisticated model should outperform a chemically meaningful nearest-neighbor baseline on the intended test.

### Step 7 — Tune inside the training data

Use nested cross-validation or an inner validation split. All learned preprocessing belongs inside the pipeline:

- imputation;
- variance/correlation filtering;
- scaling;
- feature selection;
- oversampling or undersampling;
- calibration;
- hyperparameter optimization.

### Step 8 — Use decision-relevant metrics

#### Classification

- PR-AUC or average precision for rare actives;
- ROC-AUC as a secondary ranking metric;
- balanced accuracy, MCC, sensitivity, specificity;
- precision/recall at the experimental budget;
- enrichment factor, BEDROC, hit rate, or recall in the top 0.1–5% for virtual screening;
- Brier score and reliability diagrams for probability calibration.

#### Regression

- MAE and RMSE;
- \(R^2\), Spearman, and Kendall correlation;
- error by chemical-similarity or applicability-domain bin;
- top-k rank quality if selection rather than global prediction is the goal;
- coverage and interval width for uncertainty methods.

### Step 9 — Define the applicability domain

The OECD describes a QSAR applicability domain as the response and chemical-structure space in which the model makes predictions with a stated reliability. Its validation principles require a defined endpoint, unambiguous algorithm, defined applicability domain, appropriate goodness-of-fit/robustness/predictivity measures, and mechanistic interpretation where possible [15](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/q-sar-assessment-framework-guidance-for-the-regulatory-assessment-of-quantitative-structure-activity-relationship-models-and-predictions-second-edition_cc89955e/bbdac345-en.pdf).

Useful domain checks include:

- nearest-neighbor Tanimoto similarity;
- distance or leverage in descriptor space;
- local training density;
- conformal prediction;
- ensemble disagreement;
- target/assay membership and mechanistic constraints;
- response-range and feature-range checks.

### Step 10 — Interpret at both global and local levels

- Global permutation importance or SHAP summary.
- Local explanations for shortlisted compounds.
- Map fingerprint bits back to atomic environments.
- Compare explanations across folds, seeds, RF, and XGBoost.
- Check whether proposed fragments are confounded with a chemical series, assay protocol, or nuisance property.
- Treat interpretation as hypothesis generation, not proof of mechanism.

### Step 11 — Select a diverse, testable batch

Do not simply take the top 100 near-identical analogues. Cluster candidates, apply uncertainty and domain criteria, remove artifacts, and include exploration compounds when the budget permits.

### Step 12 — Validate prospectively and update

A practical validation hierarchy is:

1. frozen external retrospective set;
2. orthogonal computational model;
3. biochemical binding/activity assay;
4. counter-screens and interference controls;
5. cell target engagement and phenotype;
6. ADME/toxicity assays;
7. in vivo PK/PD where justified.

Report both successes and failures; negative prospective data are valuable training information.

---

## 10. Validation, leakage, interpretation, and uncertainty

### 10.1 The largest risk is often leakage, not algorithm choice

Common leakage modes include:

- exact or near-duplicate compounds across splits;
- salts, tautomers, stereoisomers, or replicate measurements split independently;
- feature filtering or scaling before the split;
- oversampling before cross-validation;
- selecting descriptors with all labels, then cross-validating;
- tuning on the test set or repeatedly consulting a public leaderboard;
- target-family or compound leakage in DTI pair splits;
- temporal information leaking from future measurements;
- assay IDs, plate IDs, or metadata acting as shortcuts.

### 10.2 Random splits usually measure interpolation among analogues

Random splits are useful for debugging and estimating performance on future random samples from the same chemical mixture. They usually do not answer whether a model will discover new chemotypes. MoleculeNet explicitly warned that random splitting is often inappropriate for chemistry [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/).

Scaffold splitting is a useful baseline but not a guarantee of dissimilarity. The 2024 “Scaffold Splits Overestimate Virtual Screening Performance” study showed that different scaffolds can still be highly similar and that UMAP cluster splits produced substantially lower performance than scaffold splits on its NCI-60 tests [16](https://arxiv.org/abs/2406.00873). A 2025 evaluation similarly found scaffold-based splits among the less challenging splitters compared with stronger out-of-distribution designs [44](https://pubs.acs.org/doi/10.1021/acs.jcim.5c00475).

### 10.3 Class imbalance changes the right metric

In virtual screening, actives may be far below 1%. A classifier that predicts everything inactive can have excellent accuracy. Use PR-AUC, top-k precision/recall, enrichment, and hit rate. Class weighting, balanced RF, and XGBoost's positive-class weighting are useful; SMOTE can be useful but must occur inside training folds and may create chemically unrealistic interpolations in descriptor space.

### 10.4 Activity cliffs limit smooth generalization

Close analogues can differ sharply in potency because of stereochemistry, binding mode, solvation, conformation, or assay variability. Similarity-based models can average across the cliff. Report errors against nearest-neighbor similarity and explicitly analyze matched molecular pairs.

### 10.5 Model explanations can be unstable

The 2023 gradient-boosting benchmark found that different boosting implementations could rank molecular features differently, even when predictive performance was comparable [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/). RF importance also changes under correlated descriptors. Robust practice includes:

- stability across folds and seeds;
- grouped descriptors or substructures;
- held-out permutation importance;
- comparison across algorithms;
- medicinal-chemistry plausibility checks;
- experimental perturbation of the proposed motif when feasible.

### 10.6 Calibration and uncertainty are separate from accuracy

A model can rank well but produce poor probabilities. Conversely, calibrated uncertainty cannot repair systematic domain shift. Useful tools include:

- cross-validated Platt or isotonic calibration;
- Venn–Abers probability estimation;
- conformal classification/regression;
- quantile regression forests or boosted quantile losses;
- bootstrapped ensembles;
- similarity/distance-based domain flags;
- separate aleatoric and epistemic uncertainty studies where data permit.

Conformal validity depends on exchangeability; chemical-series or temporal shift can violate that assumption. Report empirical coverage on deployment-relevant splits.

### 10.7 Benchmark scores age

Leaderboards change as data, splits, code, and submissions change. The ADMETboost paper and current website present different historical rank counts, although the underlying model remains useful [33](https://link.springer.com/article/10.1007/s00894-022-05373-8) [45](https://ai-druglab.smu.edu/admet). Record the exact benchmark version and date.

### 10.8 Reproducibility checklist

- Dataset snapshot, source query, and license.
- Standardization and deduplication code.
- Endpoint definition and assay filters.
- Exact split identifiers.
- Featurizer and software versions.
- Random seeds.
- Full hyperparameter search space and optimization budget.
- Fitted preprocessing pipeline.
- Final model and environment/container.
- Calibration and applicability-domain method.
- Per-compound predictions for the frozen test set.
- Failed runs and excluded records.
- Prospective selection rule and assay outcomes.

---

## 11. Open-source software

### 11.1 Important distinction

- **Open source:** source code is available under an explicit license that permits use, study, modification, and redistribution subject to its terms.
- **Open access/free website:** a service can be free to use while its backend is proprietary.
- **Open model:** weights/parameters and inference code are available; training data may still have restrictions.
- **Open data:** data reuse depends on the dataset's own license, even if the software is open source.

Licenses and transitive dependencies should be reviewed for commercial use. “Open-source core” does not imply every plug-in, descriptor package, pretrained model, or dataset has the same license.

### 11.2 Foundational libraries

| Tool | RF | SVM/SVR | Gradient boosting | Drug-discovery role | License / caveat |
|---|:---:|:---:|:---:|---|---|
| **RDKit** [18](https://www.rdkit.org/docs/Overview.html) | Via integrations | Via integrations | Via integrations | Structure parsing/standardization, descriptors, ECFP/Morgan and other fingerprints, similarity, scaffolds, 2D/3D utilities | BSD-3-Clause; feature engine rather than a complete validated QSAR workflow |
| **Mordred** [19](https://github.com/mordred-descriptor/mordred) | Features | Features | Features | Large 2D/3D molecular-descriptor calculator | BSD-3-Clause; original project is older, so assess maintained forks and reproducibility |
| **PaDEL-Descriptor / wrappers** [20](https://github.com/ecrl/padelpy) | Features | Features | Features | Descriptor and fingerprint generation used by many QSAR papers | Original software is old; wrapper licenses do not necessarily replace the original component's terms |
| **scikit-learn** [21](https://scikit-learn.org/stable/) | Yes | Yes | Classical/Histogram GB | Pipelines, preprocessing, CV, metrics, RF, SVC/SVR, gradient boosting, calibration, permutation importance | BSD-3-Clause; best general Python baseline framework |
| **LIBSVM / LIBLINEAR** [25](https://github.com/cjlin1/libsvm) | No | Yes | No | Reference SVC/SVR/one-class SVM and scalable linear methods | BSD-3-Clause; used by scikit-learn and CPSign-related workflows |
| **XGBoost** [22](https://github.com/dmlc/xgboost) | No | No | Yes | Optimized regularized GBDT for QSAR, ADMET, DTI, ranking, and rescoring | Apache-2.0 |
| **LightGBM** [23](https://github.com/microsoft/LightGBM) | Includes RF-like mode but primarily GBDT | No | Yes | Fast large-scale sparse/tabular molecular models | MIT; leaf-wise growth needs regularization |
| **CatBoost** [24](https://catboost.ai/) | No | No | Yes | Ordered boosting and categorical metadata handling | Open source; check repository license/version for deployment |
| **SHAP** [46](https://github.com/shap/shap) | Explain | Explain | Explain | Local/global post-hoc explanations and feature-attribution analysis | MIT; explanations are model associations, not causal mechanisms |

### 11.3 Domain-focused frameworks and applications

| Tool | Algorithms relevant here | Main use | Interface | License/status notes |
|---|---|---|---|---|
| **DeepChem + MoleculeNet** [26](https://github.com/deepchem/deepchem) [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/) | Wraps scikit-learn models; MoleculeNet included RF and XGBoost baselines | Molecular datasets, featurizers, splitters, metrics, classical and deep models | Python, tutorials | DeepChem MIT; strong research framework, not an automatic guarantee of correct study design |
| **DeepMol** [27](https://github.com/BioSystemsUM/DeepMol) | scikit-learn RF/SVM/GB plus deep models | Modular and automated molecular preprocessing, representation, model optimization, explanation | Python, notebooks, Docker | BSD-2-Clause; active commits observed in 2026 |
| **ATOM Modeling PipeLine (AMPL)** [28](https://github.com/ATOMScience-org/AMPL) | RF, XGBoost, neural models | End-to-end curation, featurization, model tuning, prediction, uncertainty, analysis | Python, CLI, notebooks, Docker | MIT; active in 2026; current README explicitly lists RF and XGBoost, not SVM |
| **QSARtuna** [29](https://github.com/MolecularAI/QSARtuna) | RF, SVR/SVC, XGBoost, linear models | Optuna-based descriptor/algorithm/hyperparameter search, production build, uncertainty/explainability features | Python, JSON CLI, notebooks | Apache-2.0 according to its publication; version 4.0.1 repository observed in 2026 |
| **ZairaChem** [30](https://github.com/ersilia-os/zaira-chem) | AutoML ensemble including RF and boosted trees | Low-resource automated QSAR/QSPR and virtual-screening cascade | CLI | GPL-3.0; demonstrated in an African drug-discovery centre [47](https://pmc.ncbi.nlm.nih.gov/articles/PMC10504240/) |
| **QSPRpred** [48](https://github.com/CDDLeiden/QSPRpred) | Unified scikit-learn integration; XGBoost and other models | Reproducible QSPR/QSAR and proteochemometric workflows, serialization, benchmarking | Python, CLI, tutorials | MIT; peer-reviewed 2024; active package |
| **ChemML** [49](https://github.com/hachmannlab/chemml) | scikit-learn integrations; AutoML supports XGBoost/LightGBM | Chemical/material descriptors, ML workflows, optimization, explanation | Python | BSD-3-Clause; broader computational chemistry scope |
| **KNIME Analytics Platform + RDKit nodes** [50](https://www.knime.com/downloads) [51](https://www.knime.com/rdkit) | RF, SVM, gradient boosting/XGBoost nodes | Visual no-code/low-code curation, descriptor generation, model training, validation, deployment workflows | Desktop visual workflow | KNIME core GPLv3; RDKit nodes GPLv3; enterprise components and third-party nodes can have different terms |
| **Flame** [52](https://github.com/phi-grib/flame) | RF, SVM, PLS, XGBoost, conformal methods | Build, host, version, and deploy QSAR-like models | Python CLI, GUI, web service | GPL-3.0; designed for production model hosting [53](https://link.springer.com/article/10.1186/s13321-021-00509-z) |
| **QSAR-Co-X** [32](https://github.com/ncordeirfcup/QSAR-Co-X) | SVC, RF, classical GB, MLP, kNN, NB | Multi-target/multi-condition classification QSAR with feature selection and applicability-domain analysis | Python/Tkinter standalone | GPL-3.0; peer-reviewed 2021; check newer v2 repository and dependency age |
| **CPSign** [31](https://github.com/arosbio/cpsign) | LIBSVM/LIBLINEAR as principal learners; extensions possible | SVM-based conformal classification/regression and Venn–Abers probabilities | Java CLI/API; deployable REST services | Dual licensing (GPLv3 with additional terms or commercial); REST-service repo is GPL-3.0—review terms carefully |
| **ODDT** [34](https://github.com/oddt/oddt) | RF-Score variants and other ML scoring functions | CADD pipelines, docking integration, descriptors, protein–ligand scoring | Python | BSD-3-Clause; highly relevant historically, but assess maintenance and dependency compatibility |
| **RF-Score-VS binary** [35](https://github.com/oddt/rfscorevs_binary) | RF | Ready-to-use structure-based virtual-screening rescoring | CLI binary/source | BSD-3-Clause; retrospective model trained on specific benchmarks; domain shift matters |
| **OPERA** [36](https://github.com/NIEHS/OPERA) | Endpoint-dependent models including SVM, kNN, consensus, and other QSAR approaches | Physicochemical, environmental, ADME, endocrine, and toxicity predictions with applicability-domain/accuracy information | GUI, CLI, embeddable libraries | MIT; NIEHS repository showed 2026 security update and v2.9.x source; transparent QMRFs and model data |
| **openOCHEM** [37](https://github.com/openochem/openochem) | Multiple methods; documented RF plus extensible learners/consensus | Database, descriptor calculation, QSAR/QSPR model building and publishing at scale | Self-hosted web platform; public OCHEM site | Core released under AGPL-3.0; some integrated packages/models have separate licenses; substantial infrastructure |
| **Ersilia Model Hub** [54](https://github.com/ersilia-os/ersilia) | Model-dependent; catalog includes classical and modern ML | Fetch, serve, and run pretrained drug-discovery models, especially infectious/neglected diseases | CLI, per-model services, online catalog | Hub GPL-3.0; every model has its own repository, metadata, dependencies, and possibly a different data/model license |
| **QSPRmodeler** [55](https://github.com/rafalbachorz/qsprmodeler) | XGBoost, RF, SVM, bagging, neural nets, ridge | Molecular predictive analytics, hyperparameter optimization, classification/regression | Python/config files | MIT; smaller project, so independently verify maintenance and tests |

### 11.4 Specialized examples worth knowing

- **RF-Score / RF-Score-VS:** structure-based affinity prediction and virtual-screening rescoring.
- **deltaVinaXGB:** XGBoost-based protein–ligand scoring, but with legacy dependencies [40](https://github.com/jenniening/deltaVinaXGB).
- **ADMET_XGBoost:** code behind ADMETboost [38](https://github.com/smu-tao-group/ADMET_XGBoost).
- **OPERA pKa:** open SVM/XGBoost/DNN comparison and deployed SVM-based pKa workflow [56](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0384-1).
- **Automated KNIME QSAR workflow:** public curation, SAR, modeling, and virtual-screening workflows [57](https://github.com/LabMolUFG/automated-qsar-framework).
- **QITB:** browser-local RF/XGBoost QSAR, described below.

---

## 12. Open-source or open-access websites

The following services were reachable during this research unless marked as self-hosted. Availability is not guaranteed indefinitely.

| Website | Algorithms/concept | What it does | Source openness and important caveat |
|---|---|---|---|
| **QSAR in the Browser (QITB)** — [qsar.syedzayyan.com](https://qsar.syedzayyan.com/) | RF and XGBoost classification/regression | Loads ChEMBL or user data, performs visualization and lightweight QSAR entirely in the browser | AGPL-3.0 source [58](https://github.com/syedzayyan/qsar-in-browser); local computation helps privacy; suited to exploratory/lightweight work rather than regulated production. Peer-reviewed in 2026 [59](https://doi.org/10.1021/acs.jcim.6c01010) |
| **ADMETboost** — [ai-druglab.smu.edu/admet](https://ai-druglab.smu.edu/admet) | XGBoost over multiple fingerprints/descriptors | Predicts 22 ADMET endpoints from a SMILES string | GPL-3.0 training/inference code [38](https://github.com/smu-tao-group/ADMET_XGBoost); validate input and domain; do not treat color-coded output as experimental safety evidence |
| **OCHEM** — [ochem.eu](https://ochem.eu/) | Multiple QSAR learners; documented RF and consensus workflows | Stores experimental data, calculates descriptors, creates/applies/publishes models | Public service plus AGPL-3.0 openOCHEM core [37](https://github.com/openochem/openochem); individual algorithms/descriptors may have separate licenses |
| **EPA CompTox Chemicals Dashboard** — [comptox.epa.gov/dashboard](https://comptox.epa.gov/dashboard/) | Surfaces OPERA and other computational predictions | Searchable chemical, assay, exposure, and predicted-property resource | Government web resource; OPERA code/models are open source. Prediction provenance and model applicability must be inspected. The site exposed over 1.3 million chemical records at the research date [60](https://comptox.epa.gov/dashboard/) |
| **Therapeutics Data Commons (TDC)** — [tdcommons.ai](https://tdcommons.ai/) | Benchmark infrastructure, not one learner | AI-ready datasets, tasks, splitters, metrics, leaderboards, and oracles spanning therapeutic development | Open Python library and public benchmarks [14](https://tdcommons.ai/); dataset licenses differ; public leaderboards can be overfit through repeated submissions |
| **Ersilia Model Hub** — [ersilia.io/tools](https://ersilia.io/tools/) | Model-dependent, including classical ML models | Browse/fetch/serve pretrained models for activity, ADMET, representation, and infectious-disease discovery | Open-source hub; verify every model card, training domain, license, and maintenance state [54](https://github.com/ersilia-os/ersilia) |
| **MoleculeNet through DeepChem** — [DeepChem MoleculeNet loaders](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html) | Includes conventional RF/XGBoost-style baselines and modern models | Standard public molecular-property datasets, featurization, split, and metric conventions | Use through DeepChem; the historical standalone MoleculeNet site may not be reliable. Treat it as a benchmark, not an ADMET oracle [13](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/) |
| **Flame web stack** — [backend](https://github.com/phi-grib/flame), [API](https://github.com/phi-grib/flame_API), [frontend](https://github.com/phi-grib/flameWeb2) | RF, SVM, XGBoost, conformal methods | Self-hosted graphical model development and prediction service | GPL-3.0; appropriate when data must remain inside an organization; requires local deployment and validation |
| **CPSign prediction services** — [GitHub](https://github.com/arosbio/cpsign_predict_services) | SVM + conformal/Venn–Abers | Self-hosted REST services and optional molecule-drawing UI for CPSign models | Service code GPL-3.0; base CPSign is dual-licensed with additional terms |

### What these websites should and should not be used for

**Appropriate:**

- hypothesis generation;
- rapid comparison of models;
- educational or exploratory QSAR;
- cross-checking a local model;
- obtaining benchmark data;
- prioritizing compounds for experiments.

**Not appropriate without additional evidence:**

- declaring a compound safe or effective;
- replacing required laboratory or regulatory testing;
- extrapolating to unsupported chemistry;
- selecting a clinical dose;
- interpreting a predicted fragment importance as a biological mechanism.

---

## 13. Recommended tool stacks

### 13.1 Best transparent Python baseline

**RDKit + pandas + scikit-learn + XGBoost + LightGBM + SHAP**

Use when the team can code and wants full control. Benchmark:

1. Morgan counts/bits + RF;
2. scaled descriptors + RBF-SVM/SVR;
3. Morgan + descriptors + XGBoost;
4. LightGBM for scale;
5. calibrated/conformal wrappers;
6. cluster/time/external validation.

### 13.2 Best research framework for mixed classical and deep models

**DeepChem/MoleculeNet** or **DeepMol**

Use when comparing classical models with graph networks under shared loaders, splitters, and metrics. DeepMol adds higher-level pipeline automation and model explanation.

### 13.3 Best end-to-end pharmaceutical modeling pipeline

**AMPL**

Use for reproducible curation, molecular featurization, RF/XGBoost training, hyperparameter optimization, prediction, uncertainty, and analysis. Its examples include scaffold-based and external holdout validation.

### 13.4 Best AutoML-oriented QSAR options

- **QSARtuna:** explicit algorithm/descriptor search and Optuna tuning; RF, SVR, and XGBoost are directly relevant.
- **ZairaChem:** low-resource automated ensemble modeling and demonstrated deployment in a drug-discovery centre.
- **DeepMol:** customizable AutoML and broader framework integration.

Automation does not remove the need to predefine the external test and inspect leakage.

### 13.5 Best reproducibility/transferability framework

**QSPRpred**

Use when standardized model serialization, repeatable workflows, applicability analysis, and integration of different model families are priorities.

### 13.6 Best visual workflow

**KNIME Analytics Platform + RDKit nodes + scikit-learn/XGBoost integrations**

Use when medicinal chemists and data scientists need auditable drag-and-drop workflows. Lock node versions, export workflows, and document extension licenses.

### 13.7 Best SVM uncertainty workflow

**CPSign**

Use when SVM-based QSAR plus conformal intervals/prediction sets or Venn–Abers probabilities are central. Review the dual license before commercial deployment.

### 13.8 Best open structure-based RF rescoring stack

**ODDT + RF-Score/RF-Score-VS**, optionally compared with Vina, smina, and a modern independent scoring function.

Do not use a generic pretrained scoring function without testing target-family shift, docking-pose sensitivity, and similarity to its training complexes.

### 13.9 Best open ADMET cross-check

Use at least two independent sources:

- **ADMETboost** for XGBoost predictions;
- **OPERA/CompTox** for transparent models, applicability-domain information, and QMRFs;
- a locally trained project-specific model if sufficient assay-consistent data exist.

Agreement increases confidence only if models are genuinely independent; disagreement is a reason to investigate, not average blindly.

### 13.10 Best lightweight browser tool

**QITB**

Use for exploratory RF/XGBoost QSAR when installation is undesirable or data should remain in the local browser. Export data and settings for reproducibility.

---

## 14. Practical starting ranges for model development

These are **search-space starting points**, not universal optimal settings. Tune them inside training data and adapt to sample size, representation, imbalance, and compute budget.

### 14.1 Random Forest

| Parameter | Starting search |
|---|---|
| Number of trees | 500, 1,000, 2,000; increase until OOB/CV performance and importance stabilize |
| Maximum features per split | `sqrt`, `log2`, or fractions such as 0.1, 0.25, 0.5 |
| Minimum samples per leaf | 1, 2, 5, 10, 20; larger values regularize noisy QSAR data |
| Maximum depth | `None` plus bounded values such as 8, 16, 32 |
| Bootstrap | Compare `True`; consider class-balanced bootstraps for rare actives |
| Class weights | `balanced`, `balanced_subsample`, or assay-cost-driven custom weights |
| Criterion | Gini/entropy/log-loss for classification; squared/absolute error for regression as supported |

Diagnostics:

- learning curve versus tree count;
- OOB versus chemical-cluster CV;
- calibration curve;
- feature-importance stability;
- error versus nearest-neighbor similarity.

### 14.2 SVM/SVR

| Parameter | Starting search |
|---|---|
| Kernel | Linear and RBF; add validated Tanimoto/min–max kernels when appropriate |
| \(C\) | Log grid from \(10^{-3}\) to \(10^{3}\) |
| RBF \(\gamma\) | `scale` plus log grid such as \(10^{-6}\) to \(10^{1}\), adjusted for feature scale |
| SVR \(\varepsilon\) | Values tied to assay noise and transformed endpoint, e.g. 0.01–0.5 p-units |
| Class weights | `balanced` plus decision-cost-driven alternatives |
| Probability | Prefer post-hoc cross-validated calibration; do not optimize only for ROC-AUC if probabilities drive decisions |

Preprocessing:

- standardize continuous descriptors inside each fold;
- consider sparse-safe scaling for fingerprint/count matrices;
- remove constant features inside the training fold;
- do not perform supervised feature selection before splitting.

### 14.3 XGBoost / LightGBM / CatBoost

| Parameter family | Starting search |
|---|---|
| Learning rate | 0.01–0.2, coupled with tree count |
| Trees/iterations | Up to several thousand with early stopping |
| Tree depth / leaves | Shallow-to-moderate; e.g. XGBoost depth 3–10; constrain LightGBM leaves and minimum leaf data |
| Row subsampling | 0.5–1.0 |
| Column subsampling | 0.3–1.0 for wide descriptor/fingerprint matrices |
| Minimum child/leaf size | Increase for small/noisy datasets |
| Minimum split gain | Tune to suppress weak splits |
| L1/L2 regularization | Include zero and log-spaced positive values |
| Positive-class weight | Begin near negative/positive ratio, then tune for the decision metric |
| Early stopping | Use an inner validation set or nested CV; never the frozen external test |

The 2023 molecular benchmark recommends tuning as many relevant boosting parameters as feasible; under restricted compute, learning rate, minority-class weight, and minimum split gain were among high-impact parameters [11](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/).

### 14.4 Recommended metrics by task

| Task | Primary metrics | Secondary checks |
|---|---|---|
| Rare-active virtual screening | Precision/recall or hit rate at fixed budget, EF1%/EF0.1%, PR-AUC, BEDROC | ROC-AUC, diversity and novelty of selected hits |
| Balanced classification | MCC, balanced accuracy, ROC-AUC | Calibration, per-class sensitivity/specificity |
| Potency regression | MAE/RMSE and rank correlation | \(R^2\), top-k recall, error by chemistry/domain |
| ADMET regression | Endpoint-specific MAE/RMSE or Spearman per benchmark | Calibration/interval coverage, clinically meaningful error bins |
| DTI | AUPR under realistic negatives and entity-cold splits | AUROC, top-k recall by drug/target, calibration |
| Conformal prediction | Empirical coverage at requested confidence | Interval/set size and coverage under chemical shift |

---

## 15. Research gaps and future directions

### 15.1 Better out-of-distribution benchmarks

Random and scaffold splits often overstate real prospective performance. Temporal, project/series, target-cold, and structure-cluster benchmarks need wider use. Hidden test sets and single-use evaluation servers can reduce leaderboard overfitting.

### 15.2 Reliable uncertainty under chemical shift

Conformal prediction provides formal coverage under exchangeability, but deployment chemistry is often non-exchangeable. Research is needed on shift-aware conformal methods, local coverage, domain-conditional calibration, and decision policies that combine uncertainty with chemical diversity.

### 15.3 Assay-aware modeling

Pooling measurements across laboratories, constructs, species, modalities, and protocols can create a large but incoherent endpoint. Models that explicitly represent assay context may help, but metadata can also become a shortcut. Carefully designed multi-task and hierarchical models are needed.

### 15.4 Prospective and negative-result publication

The literature disproportionately reports successful retrospective benchmarks and positive virtual screens. Prospective studies with preregistered selection criteria, full screened lists, negative assay results, counter-screens, and cost accounting would provide more realistic evidence.

### 15.5 Interpretation that survives retraining

A fragment highlighted by one XGBoost fit may disappear with another split or implementation. Stable explanation requires resampling, grouped chemical features, causal/experimental follow-up, and medicinal-chemistry review.

### 15.6 Hybrid models

RF/SVM/GB can consume learned embeddings from graph neural networks, protein language models, docking models, or experimental omics. This separates representation learning from a strong tabular learner and can be effective in small-data settings. However, embeddings can import hidden training leakage and licensing restrictions.

### 15.7 Multi-objective decision support

Drug discovery does not optimize a single score. Future workflows should present Pareto fronts, uncertainty, diversity, and experimental cost rather than collapse potency, safety, PK, and synthesis into an opaque scalar.

### 15.8 Federated and privacy-preserving learning

Pharmaceutical data are fragmented across organizations. Federated classical models, secure aggregation, and shared public benchmarks may improve models without centralizing sensitive structures and assays. Privacy claims must be evaluated against model inversion and membership-inference risks.

### 15.9 Regulatory-grade reporting

Open code helps but is insufficient. Regulatory use requires a defined endpoint, algorithm, domain, performance, mechanistic interpretation where possible, traceable input preparation, and a fit-for-purpose prediction report under the OECD framework [15](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/q-sar-assessment-framework-guidance-for-the-regulatory-assessment-of-quantitative-structure-activity-relationship-models-and-predictions-second-edition_cc89955e/bbdac345-en.pdf).

---

## 16. Conclusions

Random Forests, SVM/SVR, and gradient boosting are not obsolete alternatives to deep learning. They are foundational methods for real drug-discovery datasets because they work well with fingerprints, descriptors, docking terms, network features, and modest assay collections; they are computationally efficient; and their software ecosystems are mature.

Their most defensible roles are:

- **RF:** robust first nonlinear baseline, QSAR/ADMET modeling, and RF-based docking rescoring.
- **SVM/SVR:** high-dimensional small-to-medium data, chemistry-aware kernels, virtual screening, and conformal prediction.
- **Gradient boosting:** accuracy-focused structured-data modeling at scale, ADMET prediction, DTI, and flexible feature fusion.

The central lesson is that **data curation, representation, split design, applicability domain, and prospective validation dominate the credibility of the result**. A model should be selected as a complete, versioned pipeline under a test that reproduces its intended use. Open-source software makes this possible, but openness does not itself confer biological validity.

For a new project, the recommended starting point is to train **RF, scaled SVM/SVR, and XGBoost on both fingerprints and curated descriptors**, evaluate them with a cluster or temporal split plus a frozen external set, calibrate or conformalize the selected model, inspect domain and explanation stability, choose a diverse test batch, and close the loop with prospective experiments.

---

## 17. Glossary

- **ADMET:** Absorption, Distribution, Metabolism, Excretion, and Toxicity.
- **Applicability domain (AD):** Chemical-structure and response space in which a model is expected to make predictions with stated reliability.
- **AUPR/PR-AUC:** Area under the precision–recall curve; informative when positives are rare.
- **AUROC/ROC-AUC:** Area under the receiver-operating-characteristic curve.
- **BEDROC:** Early-recognition metric that places extra weight near the top of a ranked list.
- **Calibration:** Agreement between predicted probabilities and observed frequencies.
- **Cold split:** Test entities—drugs, targets, or both—not represented during training.
- **ECFP/Morgan fingerprint:** Circular molecular representation based on local atom environments.
- **EF:** Enrichment factor; concentration of actives near the top of a ranked screen relative to random selection.
- **GBDT/GBM:** Gradient-boosted decision trees / gradient boosting machine.
- **MCC:** Matthews correlation coefficient, useful for imbalanced classification.
- **OOB:** Out-of-bag; bootstrap-excluded samples used internally by a bagged ensemble.
- **pIC50:** Negative base-10 logarithm of molar IC50.
- **PLEC:** Protein–ligand extended-connectivity fingerprint encoding contacts in a complex.
- **QSAR/QSPR:** Quantitative structure–activity/property relationship.
- **RF:** Random Forest.
- **SVC/SVM:** Support Vector Classifier / Support Vector Machine.
- **SVR:** Support Vector Regression.
- **Virtual screening:** Computational prioritization of compounds for experimental testing.

---

## 18. References

1. Breiman, L. **Random Forests.** *Machine Learning* 45, 5–32 (2001). DOI: [10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324).
2. Cortes, C.; Vapnik, V. **Support-Vector Networks.** *Machine Learning* 20, 273–297 (1995). DOI: [10.1007/BF00994018](https://doi.org/10.1007/BF00994018).
3. Friedman, J. H. **Greedy Function Approximation: A Gradient Boosting Machine.** *Annals of Statistics* 29, 1189–1232 (2001). DOI: [10.1214/aos/1013203451](https://doi.org/10.1214/aos/1013203451).
4. Svetnik, V. et al. **Random Forest: A Classification and Regression Tool for Compound Classification and QSAR Modeling.** *J. Chem. Inf. Comput. Sci.* 43, 1947–1958 (2003). DOI: [10.1021/ci034160g](https://doi.org/10.1021/ci034160g).
5. Rodríguez-Pérez, R.; Bajorath, J. **Evolution of Support Vector Machine and Regression Modeling in Chemoinformatics and Drug Discovery.** *J. Comput.-Aided Mol. Des.* 36, 355–362 (2022). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9325859/).
6. Ballester, P. J.; Mitchell, J. B. O. **A Machine Learning Approach to Predicting Protein–Ligand Binding Affinity with Applications to Molecular Docking.** *Bioinformatics* 26, 1169–1175 (2010). [Article](https://academic.oup.com/bioinformatics/article/26/9/1169/199938).
7. Wójcikowski, M.; Ballester, P. J.; Siedlecki, P. **Performance of Machine-Learning Scoring Functions in Structure-Based Virtual Screening.** *Scientific Reports* 7, 46710 (2017). [Article](https://www.nature.com/articles/srep46710).
8. Franke, L.; Byvatov, E.; Werz, O.; Steinhilber, D.; Schneider, P.; Schneider, G. **Extraction and Visualization of Potential Pharmacophore Points Using Support Vector Machines: Application to Ligand-Based Virtual Screening for COX-2 Inhibitors.** *J. Med. Chem.* 48, 6997–7004 (2005). DOI: [10.1021/jm050619h](https://doi.org/10.1021/jm050619h).
9. Tang, H.; Wang, X. S.; Huang, X. P.; Roth, B. L.; Butler, K. V.; Kozikowski, A. P.; Jung, M.; Tropsha, A. **Novel Inhibitors of Human Histone Deacetylase Identified by QSAR Modeling, Virtual Screening, and Experimental Validation.** *J. Chem. Inf. Model.* 49, 461–476 (2009). DOI: [10.1021/ci800366f](https://doi.org/10.1021/ci800366f).
10. Li, L. et al. **Target-Specific Support Vector Machine Scoring in Structure-Based Virtual Screening.** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3092157/).
11. Boldini, D. et al. **Practical Guidelines for the Use of Gradient Boosting for Molecular Property Prediction.** *J. Cheminformatics* 15, 73 (2023). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10464382/).
12. Sheridan, R. P. et al. **Extreme Gradient Boosting as a Method for Quantitative Structure–Activity Relationships.** *J. Chem. Inf. Model.* 56, 2353–2360 (2016). [Article](https://pubs.acs.org/doi/10.1021/acs.jcim.6b00591).
13. Wu, Z. et al. **MoleculeNet: A Benchmark for Molecular Machine Learning.** *Chemical Science* 9, 513–530 (2018). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5868307/).
14. Huang, K. et al. **Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development.** NeurIPS Datasets and Benchmarks (2021). [TDC](https://tdcommons.ai/) and [paper](https://zitniklab.hms.harvard.edu/publications/papers/TDC-neurips21-main.pdf).
15. OECD. **(Q)SAR Assessment Framework: Guidance for the Regulatory Assessment of (Q)SAR Models and Predictions, Second Edition.** (2024). [PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/q-sar-assessment-framework-guidance-for-the-regulatory-assessment-of-quantitative-structure-activity-relationship-models-and-predictions-second-edition_cc89955e/bbdac345-en.pdf).
16. Guo, Q.; Hernandez-Hernandez, S.; Ballester, P. J. **Scaffold Splits Overestimate Virtual Screening Performance.** (2024). [arXiv](https://arxiv.org/abs/2406.00873).
17. Hägg, G. M. et al. **Open-Source Machine Learning in Computational Chemistry.** *J. Chem. Inf. Model.* (2023). [Article](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00643).
18. **RDKit: Open-Source Cheminformatics.** [Documentation](https://www.rdkit.org/docs/Overview.html) and [source](https://github.com/rdkit/rdkit).
19. **Mordred Molecular Descriptor Calculator.** [Source](https://github.com/mordred-descriptor/mordred).
20. **PaDELPy / PaDEL-Descriptor wrapper.** [Source](https://github.com/ecrl/padelpy).
21. **scikit-learn.** [Documentation](https://scikit-learn.org/stable/).
22. **XGBoost.** [Source](https://github.com/dmlc/xgboost).
23. **LightGBM.** [Source](https://github.com/microsoft/LightGBM).
24. **CatBoost.** [Website](https://catboost.ai/) and [source](https://github.com/catboost/catboost).
25. Chang, C.-C.; Lin, C.-J. **LIBSVM: A Library for Support Vector Machines.** [Source](https://github.com/cjlin1/libsvm).
26. **DeepChem.** [Source](https://github.com/deepchem/deepchem) and [documentation](https://deepchem.readthedocs.io/).
27. **DeepMol.** [Source](https://github.com/BioSystemsUM/DeepMol); peer-reviewed description [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11622685/).
28. **ATOM Modeling PipeLine (AMPL).** [Source](https://github.com/ATOMScience-org/AMPL); paper [10.1021/acs.jcim.9b01053](https://doi.org/10.1021/acs.jcim.9b01053).
29. **QSARtuna.** [Source](https://github.com/MolecularAI/QSARtuna); paper [10.1021/acs.jcim.4c00457](https://doi.org/10.1021/acs.jcim.4c00457).
30. **ZairaChem.** [Source](https://github.com/ersilia-os/zaira-chem); deployment paper [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10504240/).
31. McShane, S. A. et al. **CPSign: Conformal Prediction for Cheminformatics Modeling.** *J. Cheminformatics* (2024). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214261/) and [source](https://github.com/arosbio/cpsign).
32. Halder, A. K.; Cordeiro, M. N. D. S. **QSAR-Co-X: An Open Source Toolkit for Multitarget QSAR Modelling.** *J. Cheminformatics* (2021). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8048082/) and [source](https://github.com/ncordeirfcup/QSAR-Co-X).
33. Tian, H.; Ketkar, R.; Tao, P. **ADMETboost: A Web Server for Accurate ADMET Prediction.** *J. Mol. Model.* 28, 408 (2022). [Article](https://link.springer.com/article/10.1007/s00894-022-05373-8).
34. Wójcikowski, M. et al. **Open Drug Discovery Toolkit (ODDT).** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4475766/) and [source](https://github.com/oddt/oddt).
35. **RF-Score-VS binary.** [Source](https://github.com/oddt/rfscorevs_binary).
36. **OPERA: Open Structure–Activity/Property Relationship App.** [Source](https://github.com/NIEHS/OPERA); model paper [10.1186/s13321-018-0263-1](https://doi.org/10.1186/s13321-018-0263-1).
37. **openOCHEM.** [Source](https://github.com/openochem/openochem); public platform [OCHEM](https://ochem.eu/).
38. **ADMET_XGBoost.** [Source](https://github.com/smu-tao-group/ADMET_XGBoost).
39. Xuan, P. et al. **Gradient Boosting Decision Tree-Based Method for Predicting Interactions Between Target Genes and Drugs.** *Frontiers in Genetics* 10, 459 (2019). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6555260/).
40. **deltaVinaXGB.** [Source](https://github.com/jenniening/deltaVinaXGB).
41. **ChEMBL.** [Website](https://www.ebi.ac.uk/chembl/).
42. **PubChem.** [Website](https://pubchem.ncbi.nlm.nih.gov/).
43. **BindingDB.** [Website](https://www.bindingdb.org/).
44. **Evaluating Machine Learning Models for Molecular Property Prediction: Performance and Robustness on Out-of-Distribution Data.** (2025). [Article](https://pubs.acs.org/doi/10.1021/acs.jcim.5c00475).
45. **ADMETboost live web interface.** [Website](https://ai-druglab.smu.edu/admet).
46. **SHAP.** [Source](https://github.com/shap/shap).
47. Turon, G. et al. **First Fully-Automated AI/ML Virtual Screening Cascade Implemented at a Drug Discovery Centre in Africa.** *Nature Communications* 14, 5736 (2023). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10504240/).
48. van den Maagdenberg, H. W. et al. **QSPRpred: A Flexible Open-Source QSPR Modelling Tool.** *J. Cheminformatics* 16, 128 (2024). [Article](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00908-y) and [source](https://github.com/CDDLeiden/QSPRpred).
49. **ChemML.** [Source](https://github.com/hachmannlab/chemml) and [documentation](https://hachmannlab.github.io/chemml/).
50. **KNIME Analytics Platform.** [Download/source information](https://www.knime.com/downloads).
51. **RDKit Nodes for KNIME.** [Extension page](https://www.knime.com/rdkit).
52. **Flame backend.** [Source](https://github.com/phi-grib/flame).
53. Pastor, M.; Gómez-Tamayo, J. C.; Sanz, F. **Flame: An Open Source Framework for Model Development, Hosting, and Usage in Production Environments.** *J. Cheminformatics* 13, 31 (2021). [Article](https://link.springer.com/article/10.1186/s13321-021-00509-z).
54. **Ersilia Model Hub.** [Website](https://ersilia.io/tools/) and [source](https://github.com/ersilia-os/ersilia).
55. **QSPRmodeler.** [Source](https://github.com/rafalbachorz/qsprmodeler).
56. Mansouri, K. et al. **Open-Source QSAR Models for pKa Prediction Using Multiple Machine Learning Approaches.** *J. Cheminformatics* (2019). [Article](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0384-1).
57. **Automated Framework for Developing Predictive Machine-Learning Models for Data-Driven Drug Discovery.** [KNIME workflows](https://github.com/LabMolUFG/automated-qsar-framework).
58. **QSAR in the Browser source.** [GitHub](https://github.com/syedzayyan/qsar-in-browser).
59. Masud, S. Z. et al. **QSAR in the Browser: An Interactive Cheminformatics Web Application.** *J. Chem. Inf. Model.* 66, 7805–7812 (2026). DOI: [10.1021/acs.jcim.6c01010](https://doi.org/10.1021/acs.jcim.6c01010).
60. **EPA CompTox Chemicals Dashboard.** [Website](https://comptox.epa.gov/dashboard/).

---

**End of report.**
