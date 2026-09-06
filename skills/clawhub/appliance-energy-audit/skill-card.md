## Description:

Use when you want to know which appliances actually drive your electric bill, whether a bill spike is explained by your usage, if standby/vampire draw is worth addressing, whether replacing an old fridge/dryer/AC pays back, or when modeling tiered utility rates - builds a ranked cost-per-appliance table from watts, duty cycle, and usage hours, reconciles it against your real bill, and computes replacement payback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Home energy users, landlords, tenants, and energy-focused developers use this skill to estimate appliance-level electricity costs, reconcile a model against utility bill kWh, identify standby draw, and evaluate replacement payback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Appliance inventories and utility bill kWh can reveal household habits.

Mitigation: Process user-provided appliance and bill data locally where possible and avoid sharing household inventories or bills unless necessary.

Risk: Energy and payback estimates can be wrong when appliance age, duty cycle, usage hours, or rate assumptions are inaccurate.

Mitigation: Calibrate estimates against actual bill kWh and verify major purchase decisions with measured usage or professional energy advice.

## Reference(s):

- [Energy Model](references/energy-model.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and tabular or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are estimates based on user-provided appliance data, utility rates, and optional bill calibration.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
