## Description:

Analyzes reported company insider transactions from live SEC and stored Form 3/4/5 records while preserving filing coverage, amendments, and interpretation limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to prepare sourced briefs about reported insider transactions for selected companies and dates, including owner roles, transaction codes, share quantities, and estimated reported consideration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and company or SEC lookup queries are sent to Crawlora; queries may consume credits.

Mitigation: Use a scoped key if available, restrict query scope, and review credit limits before use.

Risk: Incomplete filing coverage or misread transaction codes can make an insider-activity summary misleading.

Mitigation: Check source filings and coverage, preserve amendments and security types, and use the brief as filing-analysis support rather than trading advice.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/sec-insider-transaction-analysis)
- [SEC and dataset endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown brief with coverage ledger, transaction table, formulas, and source citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes amendment and duplicate flags, unknowns, and limits on filing coverage and economic interpretation.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
