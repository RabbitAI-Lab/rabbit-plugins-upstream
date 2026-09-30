## Description:

Append a scenario planning amount to a local ledger and return its recorded details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners use this skill to record a supplied scenario amount, review its budget band, and retain a local planning ledger entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied amount and bundled campaign data are stored in a local SQLite file.

Mitigation: Choose a dedicated output directory and install only if local storage of those details is acceptable.

## Reference(s):

- [Scenario Planning Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/budget-planning-units-workbench)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with recorded_amount and a local effect receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local SQLite scenario ledger in the selected output directory; does not confirm an external business action.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
