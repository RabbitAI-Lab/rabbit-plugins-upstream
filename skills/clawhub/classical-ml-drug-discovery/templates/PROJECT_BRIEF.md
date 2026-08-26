# Drug-Discovery Modeling Project Brief

## 1. Decision

- **Scientific question:**
- **Decision enabled by the model:**
- **Prediction mode:** classification / regression / ranking
- **Number or fraction of compounds that can be tested:**
- **Cost of a false positive:**
- **Cost of a false negative:**
- **Novelty requirement:** same-series / new scaffold / new target / other
- **Minimum acceptable evidence:** retrospective / external / prospective / other

## 2. Endpoint

- **Target/property/phenotype:**
- **Measurement type:** IC50 / Ki / Kd / EC50 / property / class / other
- **Units and transform:**
- **Species:**
- **Target construct/isoform:**
- **Assay modality and conditions:**
- **Classification threshold, if any:**
- **Censored-value policy:**
- **Replicate aggregation policy:**

## 3. Data

- **Source and version:**
- **Retrieval date and query:**
- **License/terms:**
- **Initial rows:**
- **Expected positives/negatives:**
- **Untested-versus-inactive semantics:**
- **Confidentiality classification:** public / internal / restricted
- **May data be sent to external services?** yes / no / specified services only

## 4. Structure curation

- **Largest-fragment/parent policy:**
- **Charge policy:**
- **Tautomer policy:**
- **Stereochemistry policy:**
- **Mixture/metal policy:**
- **Duplicate rule:**
- **Conflicting-label rule:**

## 5. Validation

- **Deployment population:**
- **Outer split:** random / scaffold / cluster / time / series / entity-cold / external
- **Split seed/cutoff:**
- **Inner validation:**
- **Primary metric:**
- **Secondary metrics:**
- **Nearest-neighbor baseline:**
- **Required confidence interval/repeats:**

## 6. Representations

- Morgan/ECFP settings:
- Physicochemical descriptors:
- Expanded descriptor set:
- Protein/complex/network features:
- Pretrained embeddings and provenance:

## 7. Models and tuning budget

- Random Forest search:
- SVM/SVR search:
- Gradient boosting/XGBoost search:
- Optional models:
- Maximum trials/runtime:
- Calibration method:
- Applicability-domain method:

## 8. Candidate selection

- Score threshold/top-k:
- In-domain rule:
- Uncertainty rule:
- Diversity/clustering rule:
- Physicochemical/reactive filters:
- Purchasability/synthesis rule:
- Orthogonal computational checks:
- Exploration fraction:

## 9. Prospective validation

- Primary assay:
- Counter-screens/interference controls:
- Selectivity panel:
- Cellular follow-up:
- ADME/toxicity follow-up:
- Decision gate after results:

## 10. Reproducibility

- Environment/container:
- Dataset checksum:
- Split file:
- Model artifact:
- Model card:
- Code/version control:
- Result archive:
