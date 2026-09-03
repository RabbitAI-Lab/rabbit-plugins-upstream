## Description:

Comprehensive R-based meta-analysis skill for clinical and systematic-review workflows, producing pooled statistics, forest and funnel plots, bias checks, subgroup/meta-regression outputs, network meta-analysis outputs, and reproducible R code in English or Chinese.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical researchers, pharmaceutical and CRO practitioners, clinicians, nurses, and medical students use this skill to run conversational meta-analysis and systematic-review support workflows from summary study data. The skill helps produce analysis reports, figures, and reproducible R code while routing numerical computation to a cloud R engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends meta-analysis summary data and a hostname-derived hash to cloud Coze endpoints for computation.

Mitigation: Install and run it only when cloud processing is acceptable for the data; use simulated or placeholder data and run exported R code locally for confidential, regulated, unpublished, or individual-patient data unless cloud processing has been approved.

Risk: Server security evidence reports recoverable shared bearer tokens in the release.

Mitigation: Review credential exposure before deployment, rotate or remove shared tokens where possible, and prefer per-user or environment-managed credentials.

Risk: Remote computation and reporting paths can affect confidentiality and auditability.

Mitigation: Review endpoint behavior and bug-report flows before installation, and require explicit approval before sending diagnostic reports or sensitive analysis inputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/meta-analysis)
- [English guide](https://github.com/medstatstar/meta-analysis/blob/main/README.md)
- [Chinese guide](https://github.com/medstatstar/meta-analysis/blob/main/README_zh-CN.md)
- [Advanced analysis reference](references/advanced_analysis.md)
- [Advanced API reference](references/advanced_api.md)
- [Data templates](references/data_templates.md)
- [R packages reference](references/r_packages.md)
- [Citation references](references/citations.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated report files, SVG/PNG figures, CSV tables, JSON result echoes, and reproducible R code.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary user-facing artifact is an HTML report; generated artifacts may include analysis_complete.R, results_summary.md, last_run.json, figures, and tables.]

## Skill Version(s):

2.2.30 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
