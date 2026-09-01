## Description:

詹明明·这个月钱去哪了 helps owner-operators attribute revenue changes to customer count, per-customer volume, and price while flagging slow erosion hidden by monthly noise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business owners and operators use this skill to explain why revenue rose or fell from ledgers, order books, payment records, or platform exports before choosing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request sensitive revenue, order, customer, or payment details.

Mitigation: Share the minimum figures needed for attribution, remove unnecessary identifiers where practical, and confirm memory retention settings before use.

Risk: Broad revenue-related phrases could activate the skill unintentionally.

Mitigation: Invoke it with explicit commands such as /zmm-revenue when possible and stop if the current task is not revenue attribution.

Risk: Attribution quality depends on the user's accounting basis and supplied figures.

Mitigation: Confirm whether revenue means signed, shipped, or collected money, and mark missing or approximate data in the report.

## Reference(s):

- [理论底座 · 营收归因](references/理论底座.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown revenue attribution report with concise next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for sensitive revenue or order details and may retain concise memory notes when OpenClaw memory is enabled.]

## Skill Version(s):

0.2.1 (source: server release evidence; SKILL.md frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
