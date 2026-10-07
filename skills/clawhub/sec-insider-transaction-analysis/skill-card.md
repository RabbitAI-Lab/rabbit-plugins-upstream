## Description:

Analyzes reported company insider transactions from Crawlora's live SEC and stored Form 3/4/5 data, preserving filing coverage, amendments, transaction codes, and interpretation limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Research analysts and developers use this skill to prepare evidence-based briefs on reported insider activity by company, owner role, transaction code, and date window. It distinguishes retrieved filing records from a complete transaction history and avoids treating reported activity as trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key and selected company or SEC query parameters are sent to Crawlora.

Mitigation: Use the skill only if you accept Crawlora as the data provider, and scope queries to the needed companies and dates.

Risk: Incomplete filing coverage, amendments, or ambiguous transaction codes can make reported activity misleading as a trading or legal conclusion.

Mitigation: Check underlying filings, show coverage and unknowns, and use the brief as research support rather than trading authorization or legal advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/sec-insider-transaction-analysis)
- [Crawlora SEC endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown analysis brief with a filing coverage ledger and classified transaction table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, date and scope qualifiers, calculation formulas, amendment or duplicate flags, and unknowns.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
