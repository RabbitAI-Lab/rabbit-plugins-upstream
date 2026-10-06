## Description:

Converts a supplied campaign amount into minor currency units; it does not forecast scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners and developers use this local helper to convert supplied USD, CNY, or EUR major and minor units into a single minor-unit amount. It does not model budgets or forecast scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The name and description suggest forecasting, but the skill only converts supplied amounts to minor units.

Mitigation: Use it only for amount normalization; use a separate forecasting tool for scenario projections.

Risk: README guidance about output directories and SQLite may imply persistence that this release does not perform.

Mitigation: Expect a local JSON result, not a saved business artifact.

## Reference(s):

- [Campaign Budget Forecaster on ClawHub](https://clawhub.ai/wxt-ai/skills/budget-planning-units-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns amount with currency and minor_units; no forecasting or scenario modeling.]

## Skill Version(s):

1.1.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
