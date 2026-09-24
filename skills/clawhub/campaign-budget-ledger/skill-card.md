## Description:

Forecast scenario amounts and record budget planning scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners and business teams use this skill to forecast campaign budget scenario amounts and record selected scenario amounts in a planning ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scenario amount could be recorded to the planning ledger before the user has confirmed it.

Mitigation: Ask for explicit confirmation before appending a scenario amount, especially for sensitive or business-critical campaign budgets.

Risk: Users may misunderstand where appended ledger entries are stored.

Mitigation: Explain the ledger append action and storage destination before recording selected scenario amounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/campaign-budget-ledger)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured object fields for amount and recorded_amount]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Forecast output includes currency and minor_units; recorded output includes scenario_id, currency, minor_units, display_amount, and budget_band.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
