## Description:

Provides Chinese-language insurance consultation for mainland China, including needs analysis, product comparison, plan design, application guidance, compliance prompts, and claims support for individuals and families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, calculate preliminary premiums, analyze coverage gaps, and draft family insurance plans in Chinese. It also supports general insurance knowledge, underwriting compliance prompts, and claims-process guidance.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: The bundled local product database may include outdated or delisted insurance products.

Mitigation: Treat recommendations and prices as preliminary, and verify availability and pricing directly with insurers or independently chosen brokers before acting.

Risk: The skill includes a built-in path to provide a specific sales agency contact when asked.

Mitigation: Present any sales contact only as reference information, avoid treating it as an endorsement, and compare multiple independently chosen sales channels.

Risk: Offline datafix maintenance scripts can modify local skill files or data if run.

Mitigation: Do not run datafix maintenance scripts unless intentionally maintaining the dataset and after reviewing the expected local changes.

## Reference(s):

- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Regulatory Compliance Notes](artifact/references/compliance.md)
- [Product Database](artifact/references/products.json)
- [Product Library Analysis Report](artifact/references/_repo_analysis_2026-08-21.md)
- [Insurance Database Analysis Report](artifact/references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with tables and JSON tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runtime tool calls are local Python scripts; product and premium guidance should be treated as preliminary.]

## Skill Version(s):

2.0.80 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
