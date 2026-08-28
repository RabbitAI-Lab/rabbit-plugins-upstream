## Description:

Meta Analysis / 医学Meta分析 helps agents run R-based medical meta-analysis workflows, including pairwise and network meta-analysis, heterogeneity and bias checks, figures, reports, and reproducible R code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

External clinicians, clinical-trial practitioners, medical students, and developers use this skill to turn natural-language meta-analysis requests or structured study data into analysis results, visualizations, topic-selection reports, and reproducible R code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meta-analysis inputs and summary study data may be sent to listed Coze endpoints.

Mitigation: Use the skill only when cloud processing is acceptable; avoid real patient-level or confidential sponsor data unless the cloud IPD path is intentionally approved.

Risk: ClawHub security evidence reports shared credentials and under-scoped network behavior that require review.

Mitigation: Review endpoint configuration, credential handling, and outbound network scope before installing in a sensitive environment.

Risk: Downloaded PDFs should be treated as untrusted files.

Mitigation: Open or process downloaded documents in a controlled environment and prefer placeholder data plus generated R code when confidentiality matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Metadata Homepage](https://github.com/medstatstar/meta-analysis)
- [README](README.md)
- [Advanced API Reference](references/advanced_api.md)
- [PRISMA / AMSTAR-2 Compliance Pre-check](references/compliance-precheck.md)
- [Complete References](references/references.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and HTML reports with figures, CSV/JSON summaries, and reproducible R scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include generated analysis files under meta_analysis/ and output/; numerical results should be presented without rounding or rewriting.]

## Skill Version(s):

2.2.27 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
