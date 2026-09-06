## Description:

Build defensible molecular ML workflows for drug discovery, including QSAR, virtual screening, ADMET, toxicity, binding-affinity, and drug-target modeling with Random Forest, SVM/SVR, Gradient Boosting, dataset analysis, conformal uncertainty, consensus modeling, diversity-aware selection, and cheminformatics-aware interpretation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Developers, computational chemists, and ML practitioners use this skill to curate molecular datasets, train and compare classical QSAR or screening models, assess leakage, uncertainty, and applicability domain, and produce reproducible decision-support reports for experimental prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loading untrusted `.joblib` or pickle model bundles can execute code.

Mitigation: Use an isolated Python environment and load only model bundles you created or otherwise trust.

Risk: Proprietary structures or assay labels may be sensitive.

Mitigation: Keep data local by default and use external services only after separate approval.

Risk: Model scores may be mistaken for evidence of binding, efficacy, safety, mechanism, or clinical utility.

Mitigation: Present outputs as computational decision support and require appropriate prospective or orthogonal validation before making scientific claims.

Risk: Third-party packages, models, datasets, and web tools can carry separate licensing or usage restrictions.

Mitigation: Review dependency, model, dataset, and service terms before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/classical-ml-drug-discovery)
- [WORKFLOW.md](references/WORKFLOW.md)
- [ALGORITHM_GUIDE.md](references/ALGORITHM_GUIDE.md)
- [VALIDATION_PROTOCOL.md](references/VALIDATION_PROTOCOL.md)
- [FAILURE_MODES.md](references/FAILURE_MODES.md)
- [OPEN_SOURCE_TOOLS.md](references/OPEN_SOURCE_TOOLS.md)
- [RESEARCH_REPORT.md](references/RESEARCH_REPORT.md)
- [DRUG_DISCOVERY_REPORT_TEMPLATE.md](templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md)
- [PROJECT_BRIEF.md](templates/PROJECT_BRIEF.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and generated JSON, CSV, model, and report artifacts from the bundled command-line workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline local workflow; reads user-supplied files and writes requested output directories; no API keys required.]

## Skill Version(s):

1.4.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
