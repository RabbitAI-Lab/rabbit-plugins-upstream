# Open-Source Software and Web Resources

**Status context:** assembled for this skill's 1.0.4 release in August 2026. Recheck availability,
license, package version, and model card before use.

## Core libraries

| Tool | URL | Relevant capability | License/caveat |
|---|---|---|---|
| RDKit | https://github.com/rdkit/rdkit | Structure handling, Morgan/ECFP, descriptors, scaffolds | BSD-3-Clause |
| scikit-learn | https://scikit-learn.org | RF, SVC/SVR, classical/histogram GB, CV, calibration, metrics | BSD-3-Clause |
| LIBSVM | https://github.com/cjlin1/libsvm | Kernel SVC/SVR and one-class SVM | BSD-3-Clause |
| XGBoost | https://github.com/dmlc/xgboost | Regularized scalable GBDT | Apache-2.0 |
| LightGBM | https://github.com/microsoft/LightGBM | Fast histogram/leaf-wise GBDT | MIT |
| CatBoost | https://github.com/catboost/catboost | Ordered boosting and categorical variables | Open source; verify current license |
| Mordred | https://github.com/mordred-descriptor/mordred | Large molecular descriptor set | BSD-3-Clause; original project is old |
| PaDELPy | https://github.com/ecrl/padelpy | Python wrapper for PaDEL descriptors/fingerprints | Wrapper MIT; inspect original component terms |
| SHAP | https://github.com/shap/shap | Post-hoc model explanations | MIT; attribution is not causality |

## Molecular ML frameworks

| Tool | URL | RF | SVM | GB | Purpose and caveat |
|---|---|:---:|:---:|:---:|---|
| DeepChem | https://github.com/deepchem/deepchem | ✓ | via sklearn | ✓ | Datasets, features, splitters, classical/deep models; MIT |
| DeepMol | https://github.com/BioSystemsUM/DeepMol | ✓ | ✓ | ✓ | Modular/AutoML molecular workflows; BSD-2-Clause |
| AMPL | https://github.com/ATOMScience-org/AMPL | ✓ | — in current model list | XGBoost | End-to-end pharmaceutical modeling; MIT |
| QSARtuna | https://github.com/MolecularAI/QSARtuna | ✓ | ✓ | XGBoost | Optuna-based descriptor/model search; Apache-2.0 per publication |
| ZairaChem | https://github.com/ersilia-os/zaira-chem | ✓ | model-dependent | ✓ | Low-resource automated QSAR; GPL-3.0 |
| QSPRpred | https://github.com/CDDLeiden/QSPRpred | via sklearn | via sklearn | XGBoost | Reproducible QSPR/QSAR/PCM; MIT |
| ChemML | https://github.com/hachmannlab/chemml | via integrations | via integrations | XGBoost/LightGBM AutoML | Broader chemistry ML; BSD-3-Clause |
| KNIME + RDKit nodes | https://www.knime.com/rdkit | ✓ | ✓ | ✓ | Visual workflow; core/nodes GPLv3, extensions vary |
| Flame | https://github.com/phi-grib/flame | ✓ | ✓ | XGBoost | Model development and hosting; GPL-3.0 |
| QSAR-Co-X | https://github.com/ncordeirfcup/QSAR-Co-X | ✓ | SVC | classical GB | Multi-target classification; GPL-3.0 |
| CPSign | https://github.com/arosbio/cpsign | — | ✓ | extensions possible | Conformal/Venn–Abers; dual GPLv3-with-additional-terms/commercial |
| ODDT | https://github.com/oddt/oddt | RF-Score | — | — | Structure-based CADD/scoring; BSD-3-Clause, assess maintenance |
| OPERA | https://github.com/NIEHS/OPERA | endpoint-dependent | pKa and endpoint models | endpoint-dependent | Transparent property/ADMET/tox QSAR; MIT |
| openOCHEM | https://github.com/openochem/openochem | ✓ | integrations vary | integrations vary | Self-hosted web QSAR environment; AGPL-3.0 core, dependencies vary |
| Ersilia | https://github.com/ersilia-os/ersilia | model-dependent | model-dependent | model-dependent | Pretrained drug-discovery model hub; model-level licenses vary |
| QSPRmodeler | https://github.com/rafalbachorz/qsprmodeler | ✓ | ✓ | XGBoost | Small Python QSPR/QSAR project; MIT, verify maintenance |

## Specialized scoring and prediction

| Tool | URL | Use | Caveat |
|---|---|---|---|
| RF-Score-VS | https://github.com/oddt/rfscorevs_binary | RF-based structure-screen rescoring | Historical pretrained domain and docking assumptions |
| deltaVinaXGB | https://github.com/jenniening/deltaVinaXGB | XGBoost protein–ligand scoring | Legacy pinned dependencies and modified Vina |
| ADMET_XGBoost | https://github.com/smu-tao-group/ADMET_XGBoost | Code behind ADMETboost | Historical TDC version; no universal safety guarantee |
| Automated KNIME QSAR framework | https://github.com/LabMolUFG/automated-qsar-framework | Curation, SAR, modeling, VS workflow | Inspect node versions and data query |

## Live/open web interfaces

| Service | URL | Model concept | Data/privacy note |
|---|---|---|---|
| QSAR in the Browser | https://qsar.syedzayyan.com | RF and XGBoost in-browser QSAR | Computation stays in browser; AGPL source |
| ADMETboost | https://ai-druglab.smu.edu/admet | XGBoost, 22 ADMET endpoints | Input SMILES sent to server; validate structure/domain |
| OCHEM | https://ochem.eu | Data, descriptors, RF/other model building | Uploaded data reach server unless self-hosted |
| EPA CompTox Dashboard | https://comptox.epa.gov/dashboard | OPERA and other predictions | Public government resource; inspect prediction provenance |
| TDC | https://tdcommons.ai | Datasets, splitters, metrics, leaderboards | Dataset licenses differ; benchmark is not a predictor |
| Ersilia tools | https://ersilia.io/tools | Pretrained model catalog | Inspect each model repository and card |
| Flame stack | https://github.com/phi-grib/flame | Self-hosted RF/SVM/XGBoost web modeling | Local deployment protects proprietary structures |
| CPSign REST services | https://github.com/arosbio/cpsign_predict_services | SVM conformal/Venn–Abers service | Self-hosted; review dual base license |

## Public data sources

| Source | URL | Typical use | Critical caution |
|---|---|---|---|
| ChEMBL | https://www.ebi.ac.uk/chembl/ | Curated target bioactivity | Assay, construct, units, confidence, duplicates |
| PubChem BioAssay | https://pubchem.ncbi.nlm.nih.gov | Primary/confirmatory screens | “Inactive” semantics and assay artifacts vary |
| BindingDB | https://www.bindingdb.org | Kd/Ki/IC50 binding records | Endpoint types and conditions differ |
| TDC | https://tdcommons.ai | Benchmark-ready therapeutics datasets | Version and public-test overfitting |
| MoleculeNet/DeepChem | https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html | Standard molecular benchmarks | Historical tasks are not a deployment domain |
| PDBbind | http://www.pdbbind.org.cn | Complex structures and affinities | Redundancy, target overlap, measurement heterogeneity |
| ZINC | https://zinc.docking.org | Purchasable/virtual compounds | Availability and protonation/conformer preparation |

## Selection guidance

- Need full control: RDKit + scikit-learn + XGBoost/LightGBM.
- Need shared benchmark infrastructure: DeepChem/MoleculeNet or TDC.
- Need AutoML: QSARtuna, DeepMol, or ZairaChem.
- Need reproducible model packaging: AMPL or QSPRpred.
- Need visual workflow: KNIME + RDKit.
- Need local web deployment: Flame or openOCHEM.
- Need SVM uncertainty: CPSign.
- Need docking rescoring: ODDT/RF-Score-VS plus an independent scorer.
- Need open endpoint predictions: OPERA/CompTox; cross-check with ADMETboost.
- Need browser-only exploration: QITB.

A free or open-source tool is not automatically validated for the user's endpoint. Audit training data,
split, applicability domain, model version, and license before acting on predictions.
