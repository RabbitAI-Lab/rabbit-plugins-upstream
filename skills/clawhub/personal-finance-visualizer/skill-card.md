## Description:

Turn user-provided personal finance records into a local interactive report with spending, income, transfers and cash movement in English or Chinese.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jasonhmy](https://clawhub.ai/user/jasonhmy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use the skill to reconcile authorized financial records and review spending, income, transfers, and cash movement in a local interactive report. It is not for bank-account actions or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial records and transaction details are sensitive.

Mitigation: Share only records you authorize the agent host to process, and account for the host's retention settings.

Risk: Report links and exported reports can expose transaction details.

Mitigation: Keep report links and exports private; export only when needed.

Risk: A local report server may remain active after review.

Mitigation: Stop the local server when you are finished reviewing the report.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jasonhmy/skills/personal-finance-visualizer)

## Skill Output:

**Output Type(s):** [HTML, Charts, Analysis, Guidance]

**Output Format:** [Interactive local HTML finance report with transaction details and concise review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report coverage and classifications depend on the records and user confirmations provided.]

## Skill Version(s):

1.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
