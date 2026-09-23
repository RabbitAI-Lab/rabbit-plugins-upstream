## Description:

AI KEY·大客户会不会跑 helps owner-operators assess customer, channel, and product revenue concentration, estimate runway if the largest customer leaves, and produce risk and prohibited-action lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators and 2B business leaders use this skill to turn customer, channel, and product revenue data into a concentration risk checkup, a largest-customer runway estimate, and concrete actions to avoid or prioritize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and reuse sensitive customer names, revenue amounts, payment behavior, and channel dependence across sessions.

Mitigation: Use anonymized customer labels where possible, avoid highly confidential accounts unless memory use is explicitly controlled, and review outputs before sharing.

## Reference(s):

- [理论底座 · 集中度](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-concentration)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with tables, risk lists, and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write skill memory; reports should avoid real customer names when anonymization is enabled.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter lists 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
