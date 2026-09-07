## Description:

Build defensible molecular ML for drug discovery - QSAR, virtual screening, ADMET, toxicity, binding affinity, drug-target models - with Random Forest, SVM/SVR, and Gradient Boosting, plus dataset analysis, inductive conformal prediction, multi-model consensus, diversity-aware batch selection, and cheminformatics-aware interpretation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Developers, data scientists, and cheminformatics practitioners use this skill to curate molecular datasets, build leakage-resistant QSAR or screening workflows, compare classical ML models, calibrate uncertainty, select diverse candidate batches, and produce reproducible drug-discovery reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loading untrusted model.joblib files can execute unsafe Python deserialization behavior.

Mitigation: Use --trust-model only with model bundles you created or otherwise trust.

Risk: CSV outputs derived from untrusted inputs may be unsafe when opened in spreadsheet software.

Mitigation: Treat generated CSV files as untrusted data before opening them in Excel, LibreOffice, or similar tools.

Risk: Model scores may be mistaken for evidence of binding, efficacy, safety, mechanism, or clinical utility.

Mitigation: Use outputs as computational decision support and require appropriate prospective experiments before making discovery or safety claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/classical-ml-drug-discovery)
- [Workflow](references/WORKFLOW.md)
- [Algorithm Guide](references/ALGORITHM_GUIDE.md)
- [Validation Protocol](references/VALIDATION_PROTOCOL.md)
- [Failure Modes](references/FAILURE_MODES.md)
- [Open Source Tools](references/OPEN_SOURCE_TOOLS.md)
- [Research Report](references/RESEARCH_REPORT.md)
- [Drug Discovery Report Template](templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md)
- [Project Brief Template](templates/PROJECT_BRIEF.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python CLI workflows, JSON/CSV output descriptions, and report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only workflow; reads user-supplied paths and writes requested output files.]

## Skill Version(s):

1.4.5 (source: server release metadata; artifact frontmatter reports 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
