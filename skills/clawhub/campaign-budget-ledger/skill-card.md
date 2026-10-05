## Description:

Forecast a campaign scenario amount and optionally append it to a local planning ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners and developers use this skill to calculate a scenario amount from a supplied planning note and, when requested, record the amount in a local planning ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downstream runs write campaign planning data to a local SQLite file.

Mitigation: Use a dedicated output directory and handle the ledger as local business data.

Risk: A local ledger entry could be mistaken for an external business action.

Mitigation: Treat the receipt as confirmation of a local write only; verify external actions separately.

## Reference(s):

- [Campaign Budget Ledger release](https://clawhub.ai/wxt-ai/skills/campaign-budget-ledger)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and optional local SQLite ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream runs return an effect receipt and write within the caller-specified output directory.]

## Skill Version(s):

3.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
