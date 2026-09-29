## Description:

Converts a supplied campaign budget amount in USD, CNY, or EUR into minor units rather than predicting an amount from a scenario.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners and their agents use this skill to convert a supplied budget amount into minor units for planning workflows. It does not estimate a budget from free-form scenario details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The forecast wording may imply predictive budgeting, although the skill only converts a supplied amount.

Mitigation: Provide an explicit currency and amount; do not treat the converted result as a budget estimate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/budget-planning-units-identifier)
- [Skill README](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON object containing amount.currency and amount.minor_units]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied amounts; does not save a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
