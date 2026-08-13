## Description:

分析药物组合机制、协同证据与联合开发策略。适用于：研究两个或多个药物的互补机制、协同证据、耐药克服逻辑和组合开发策略，用于联合用药假设形成和实验优先级排序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers and drug-development analysts use this skill to compare two or more drugs, gather literature, patent, translational, and ADMET evidence, form testable synergy hypotheses, and prioritize combination-development experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated medical, ADMET, or experimental conclusions may be mistaken for validated clinical guidance.

Mitigation: Treat outputs as research support and require qualified scientific and clinical review before acting on conclusions.

Risk: The workflow depends on external pharma, chemistry, patent-search, and office tools that may be unavailable or misconfigured in the agent environment.

Mitigation: Confirm the required tools are present and review intermediate evidence before relying on generated reports.

Risk: Literature, patent, DOI, and ADMET-derived signals can be incomplete or uncertain for specific drug combinations.

Mitigation: Verify source records and prioritize experimental validation of synergy hypotheses, toxicity signals, and drug-drug interaction concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/drug-combination-synergy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis, Markdown tables, ECharts-compatible chart data, and Word document output (.docx)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DOI-linked citations, ADMET comparisons, mechanism matrices, testable hypotheses, staged experimental designs, and safety warnings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
