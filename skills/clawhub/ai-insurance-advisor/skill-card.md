## Description:

Provides China mainland insurance need analysis, product comparison, premium calculation, plan design, insurance knowledge answers, and compliance reminders using local reference files and Python helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to structure insurance needs, compare local product data, estimate premiums, design coverage plans, and receive insurance knowledge and compliance reminders. Outputs should be treated as informational and verified with licensed insurance professionals before purchase or sale.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: The skill can provide regulated insurance sales recommendations.

Mitigation: Use outputs as informational only and require review by licensed insurance professionals before customers rely on recommendations.

Risk: Static product data may be outdated, unavailable, or priced differently from official insurer calculations.

Mitigation: Verify product availability, terms, and premiums with official insurer or licensed intermediary sources before quoting or purchasing.

Risk: The artifact includes a mandatory sales-channel recommendation flow that security evidence flags as unsupported.

Mitigation: Review and, if necessary, disable or revise channel-promotion behavior before deployment in customer-facing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance product database](artifact/references/products.json)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [National Financial Regulatory Administration](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static insurance product, knowledge, and compliance references; product availability and pricing require independent verification.]

## Skill Version(s):

2.0.114 (source: server release metadata; artifact frontmatter lists 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
