## Description:

专注对单个亚马逊 ASIN 进行全方位数据驱动的深度拆解，通过四步流水线整合 Keepa、Sorftime 与 SIF 数据，输出涵盖价格、BSR、评论、Deal、流量结构和生命周期等维度的 11 章节 HTML 深度报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and market analysts use this skill to analyze one competitor ASIN across supported Amazon marketplaces and produce a data-backed competitor report. It combines product history, sales trends, traffic keywords, traffic source structure, quantitative analysis, and report generation into a guided workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes account login and billing-related behavior.

Mitigation: Install only in a trusted environment and review any plan, order, or payment action before proceeding.

Risk: The package can upload files to public URLs.

Mitigation: Avoid uploading private or sensitive data; publish files only when public access is intended.

Risk: The package depends on LINKFOX_* endpoint and credential variables.

Mitigation: Lock or verify LINKFOX_* endpoint variables before use and provide credentials only for the intended LinkFox account.

Risk: The package may submit feedback or telemetry.

Mitigation: Review feedback behavior before installation and avoid automatic feedback submission for private data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-amazon-single-competitor-analysis)
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [Primary Skill Instructions](artifact/SKILL.md)
- [Competitor Reverse Analysis Workflow](artifact/skills/competitor-reverse-analysis/SKILL.md)
- [S1 Data Collection](artifact/skills/competitor-reverse-analysis/references/steps/S1.md)
- [S2 Product Snapshot](artifact/skills/competitor-reverse-analysis/references/steps/S2.md)
- [S3 Quantitative Analysis](artifact/skills/competitor-reverse-analysis/references/steps/S3.md)
- [S4 Report Generation](artifact/skills/competitor-reverse-analysis/references/steps/S4.md)
- [Report Layout Reference](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance, files]

**Output Format:** [HTML report file with a concise text or Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ASIN and Amazon marketplace; generated metrics should come from script output or returned API data, with unavailable sections marked as no data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
