## Description:

Classical ML Drug Discovery helps agents plan, build, audit, interpret, and report molecular machine-learning workflows for QSAR, virtual screening, ADMET, toxicity, binding-affinity, and drug-target modeling with Random Forests, SVM/SVR, and Gradient Boosting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, researchers, and drug-discovery teams use this skill to curate molecular datasets, train leakage-aware classical ML baselines, assess applicability domain and calibration, screen compound libraries, and produce reproducible decision-support reports. It is intended for computational prioritization and audit support, not as laboratory, clinical, or regulatory proof.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loading an untrusted joblib model can execute malicious code.

Mitigation: Only use --trust-model with model files created by the user or obtained from a trusted source, and verify checksums before loading.

Risk: Proprietary molecular structures, targets, or assay labels may leave the machine if optional external services are used.

Mitigation: Keep data local by default and send it to third-party web services only with explicit authorization.

Risk: Dependency and package-license choices can affect commercial deployment.

Mitigation: Install in an isolated Python environment, pin or lock production dependencies, use trusted package channels, and review dependency licenses for commercial use.

Risk: Model predictions can be mistaken for experimental evidence.

Mitigation: Use the skill as computational decision support and require appropriate biochemical, cellular, ADME/toxicity, and prospective validation before acting on candidates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/classical-ml-drug-discovery)
- [Research Report](references/RESEARCH_REPORT.md)
- [Algorithm Guide](references/ALGORITHM_GUIDE.md)
- [Validation Protocol](references/VALIDATION_PROTOCOL.md)
- [Open-Source Tools](references/OPEN_SOURCE_TOOLS.md)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [PubChem BioAssay](https://pubchem.ncbi.nlm.nih.gov)
- [BindingDB](https://www.bindingdb.org)
- [Therapeutics Data Commons](https://tdcommons.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, plus local CSV, JSON, Markdown, and model artifacts from the bundled CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI is local-only, reads user-supplied paths, and writes audit, training, prediction, metrics, split, feature-importance, and model-card files to user-selected outputs.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
