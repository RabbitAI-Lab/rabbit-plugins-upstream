## Description:

Forecast a scenario amount.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external campaign planners use this skill to forecast a concise campaign budget amount from a planning note with currency, major units, and minor units.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The returned amount may not match the user's intended business logic because the skill describes the output shape but does not define a detailed forecasting formula.

Mitigation: Verify the returned currency and minor_units against the campaign planning note and applicable budget logic before relying on the result.

## Reference(s):

- [Campaign Budget Forecaster on ClawHub](https://clawhub.ai/wxt-ai/skills/budget-planning-units-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured amount object with currency and minor_units]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the requested amount field concisely; no file, credential, network, persistence, or execution behavior is disclosed.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
