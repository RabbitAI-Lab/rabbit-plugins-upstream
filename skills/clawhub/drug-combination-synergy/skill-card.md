## Description:

分析药物组合机制、协同证据与联合开发策略。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Drug-discovery researchers and scientific teams use this skill to compare two-drug combinations, assess literature and ADMET evidence, form synergy hypotheses, and plan follow-up experiments. It supports research planning and report generation, not clinical decision-making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scientific claims, DOI metadata, ADMET predictions, and experimental recommendations may be incomplete or misleading if used without review.

Mitigation: Review all generated evidence summaries, citations, ADMET results, and experimental plans before relying on them; use the skill for research planning rather than clinical advice.

Risk: The workflow depends on referenced pharma, chemical, patent, translational-medicine, and office tools being available and appropriate for the environment.

Mitigation: Install and run the skill only where those tools are expected, and verify returned tool data before including it in reports.

## Reference(s):

- [ClawHub skill release: drug-combination-synergy](https://clawhub.ai/yuanzhian-patsnap/skills/drug-combination-synergy)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown analysis and tables, with an optional Word report (.docx) when the required office toolchain is available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ADMET comparisons, mechanism matrices, testable hypotheses, staged experimental designs, DOI-indexed citations, and safety warnings driven by ADMET results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
