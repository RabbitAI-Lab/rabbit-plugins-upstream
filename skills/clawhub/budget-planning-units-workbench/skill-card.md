## Description:

Appends a scenario planning amount to a local campaign planning ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Campaign planners use this skill to record a scenario amount and retrieve its recorded value and budget band.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial records may be sent to an unintended configured endpoint.

Mitigation: Unset delivery endpoint and API key variables unless submission is intended; allowlist the destination when delivery is needed.

Risk: Local planning records may be stored in an inappropriate shared location.

Mitigation: Use a dedicated output directory and review access to the stored ledger.

## Reference(s):

- [Scenario Planning Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/budget-planning-units-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result with a local ledger record and optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records currency, amount, scenario ID, and budget band in a local ledger.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
