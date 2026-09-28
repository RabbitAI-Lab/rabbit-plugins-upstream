## Description:

Helps campaign planners forecast scenario amounts and format selected amounts as planning records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners use this skill to forecast an amount from a supplied planning note or return a formatted planning record for a selected amount.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A returned planning record may be mistaken for a persisted ledger entry.

Mitigation: Treat the returned record as a planning output; confirm and save it separately if a durable ledger entry is needed.

## Reference(s):

- [Campaign Budget Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/campaign-budget-ledger)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Structured amount objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an amount with currency and minor units, or a planning record with scenario ID, display amount, and budget band.]

## Skill Version(s):

2.1.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
