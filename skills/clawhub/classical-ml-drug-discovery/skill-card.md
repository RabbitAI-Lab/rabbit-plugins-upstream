## Description:

End-to-end, evidence-aware drug-discovery skill for building and auditing molecular QSAR, virtual-screening, ADMET, toxicity, binding-affinity, and drug-target models with Random Forests, Support Vector Machines/Regression, and Gradient Boosting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Developers, researchers, and computational drug-discovery teams use this skill to plan, audit, train, compare, and report classical molecular machine-learning workflows for QSAR, virtual screening, ADMET/toxicity, binding-affinity, and drug-target modeling. It supports local decision support and candidate prioritization, not proof of binding, efficacy, safety, mechanism, or clinical utility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loading an untrusted model.joblib can execute code because joblib uses pickle-compatible deserialization.

Mitigation: Use --trust-model only for model bundles you created or otherwise trust, and verify checksums before loading.

Risk: Drug-discovery predictions can be mistaken for evidence of binding, efficacy, safety, mechanism, or clinical utility.

Mitigation: Treat outputs as computational decision support and require appropriate biochemical, cellular, ADME/toxicity, and prospective validation before acting on candidates.

Risk: Proprietary structures or assay labels may leave the local environment if optional external websites or data services are used.

Mitigation: Keep the bundled CLI local-only by default and obtain explicit authorization before sending confidential data to any third-party service.

Risk: Dependency or license drift can affect reproducibility and commercial use.

Mitigation: Install in an isolated environment, pin production dependencies, retain an environment lock file, and review dependency licenses.

## Reference(s):

- [Classical ML Drug Discovery Skill](https://clawhub.ai/orionshaowswmw/skills/classical-ml-drug-discovery)
- [Research Report](references/RESEARCH_REPORT.md)
- [Algorithm Guide](references/ALGORITHM_GUIDE.md)
- [Validation Protocol](references/VALIDATION_PROTOCOL.md)
- [Open-Source Software and Web Resources](references/OPEN_SOURCE_TOOLS.md)
- [Drug-Discovery Report Template](templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md)
- [Project Brief Template](templates/PROJECT_BRIEF.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command examples, plus local JSON, CSV, model, and Markdown report artifacts when the bundled CLI is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local CLI can produce data_audit.json, curated_data.csv, metrics.json, split_assignments.csv, test_predictions.csv, feature_importance.csv, model.joblib, predictions.csv, and model_card.md.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
