## Description:

Provides read-only SEC Form 4 insider transactions, market-wide activity, cluster buys, and 10b5-1 plan context through SentiSense.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research analysts use this skill to examine insider buying and selling, screen for cluster buys, and distinguish planned sales from other Form 4 transactions. Its output is informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and query interests are sent to the SentiSense service.

Mitigation: Use a dedicated API key and share only queries you are comfortable disclosing to SentiSense.

Risk: Misreading awards, tax withholding, or planned sales as discretionary trading can mislead financial decisions.

Mitigation: Separate open-market purchases and sales from other transaction codes, label confirmed 10b5-1 plans, and avoid presenting results as investment advice.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of insider filings and activity]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SentiSense API key; free-tier results may be limited to a preview slice.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
