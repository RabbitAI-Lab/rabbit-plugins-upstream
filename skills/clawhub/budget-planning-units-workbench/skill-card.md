## Description:

Append a scenario planning amount.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business planning users use this skill to append a supplied scenario amount to a planning ledger and return a concise recorded amount for the current request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles budget amount data supplied in prompts.

Mitigation: Provide only the amount needed for the planning task and avoid unnecessary private financial or business context.

Risk: A recorded amount could be copied into planning workflows without review.

Mitigation: Review the scenario_id, currency, minor_units, display_amount, and budget_band before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/budget-planning-units-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON-compatible object with scenario_id, currency, minor_units, display_amount, and budget_band]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the recorded_amount field for the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
