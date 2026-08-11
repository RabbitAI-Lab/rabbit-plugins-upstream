## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，并与同类产品客观对比，产出可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Insurance, compliance, and product teams use this skill to check insurance product terms, compare similar products, and prepare a structured explanation draft for customer-facing discussions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance product names, comparison terms, or related query details are sent to Cue's external service.

Mitigation: Confirm organizational approval before use and avoid customer personal data, confidential internal assessments, or non-public business information unless that sharing is permitted.

Risk: Generated insurance term analysis could be incomplete or misleading if Cue service results or external data sources are stale, unavailable, or incorrect.

Mitigation: Review the generated report under ~/cue-reports against primary policy documents and regulatory sources before using it in customer-facing or compliance-sensitive contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue service](https://cuecue.cn)
- [Example Cue report](https://cuecue.cn/share/1c3d67d8bc4c)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with command-line invocation and optional document conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated report is written locally under ~/cue-reports and may be converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
