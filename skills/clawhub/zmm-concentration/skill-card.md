## Description:

Revenue concentration checkup for owner-operators that assesses dependence on top customers, channels, and products, estimates runway if the largest customer leaves, and produces risk and do-not-touch lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators and small-business leaders use this skill to understand whether revenue is concentrated in a small number of customers, channels, or products. The skill guides data collection, calculates concentration and runway, checks churn warning signs, and recommends concrete risk controls without defaulting to blanket diversification advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read shared memory that contains private business notes.

Mitigation: Review the skill before installation in environments with sensitive memory, and inspect or clear skill memory when the runtime supports it.

Risk: Revenue concentration analysis can involve sensitive customer names, revenue lists, and customer-risk observations.

Mitigation: Use anonymized customer labels and avoid storing raw revenue lists or real customer names.

## Reference(s):

- [理论底座 · 集中度](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concentration)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with tables and action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include memory-backed calibration notes and should avoid exposing real customer names when anonymization is appropriate.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
