## Description:

Build defensible molecular ML for drug discovery — QSAR, virtual screening, ADMET, toxicity, binding affinity, drug-target models — with Random Forest, SVM/SVR, and Gradient Boosting, plus dataset analysis, inductive conformal prediction, multi-model consensus, diversity-aware batch selection, and cheminformatics-aware interpretation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

Apache 2.0

## Use Case:

Drug-discovery practitioners, cheminformatics developers, and research teams use this skill to curate molecular activity data, train leakage-aware classical ML models, audit validation design, screen libraries, estimate uncertainty, and prepare reproducible reports for experimental follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Python model bundles such as joblib or pickle files can execute code when loaded if they come from an untrusted source.

Mitigation: Use an isolated Python environment and do not pass --trust-model for joblib files you did not create or verify.

Risk: Optional external chemistry services may receive proprietary structures, labels, or assay context.

Mitigation: Keep work local by default and use external services only when the data owner has approved sharing.

Risk: Model scores can be mistaken for evidence of binding, efficacy, safety, mechanism, or clinical utility.

Mitigation: Treat predictions as decision support, report applicability domain and uncertainty, and require appropriate prospective experiments before discovery claims.

Risk: Third-party ML and cheminformatics packages may have separate license terms for commercial deployments.

Mitigation: Review package, model, and data-source licenses before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/classical-ml-drug-discovery)
- [Research report](references/RESEARCH_REPORT.md)
- [Algorithm guide](references/ALGORITHM_GUIDE.md)
- [Validation protocol](references/VALIDATION_PROTOCOL.md)
- [Open-source tools](references/OPEN_SOURCE_TOOLS.md)
- [RDKit](https://github.com/rdkit/rdkit)
- [scikit-learn](https://scikit-learn.org)
- [XGBoost](https://github.com/dmlc/xgboost)
- [Therapeutics Data Commons](https://tdcommons.ai/)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [BindingDB](https://www.bindingdb.org/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; bundled CLI commands can produce CSV, JSON, reports, and model artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first workflow; optional external chemistry services require explicit permission before sharing proprietary structures or labels.]

## Skill Version(s):

1.3.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
