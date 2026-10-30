## Description:

Helps building operations agents inspect facility systems and diagnose HVAC and metering issues across BACnet, Modbus, IO-Link, BAS, and optional MQTT, with approval-gated equipment commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Facility operators and building automation engineers use this skill to discover and read equipment points, review alarms and trends, analyze energy usage, and investigate operational issues. Authorized operators can propose equipment changes through dry-run and named-approval safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Equipment commands can change building settings and affect active systems.

Mitigation: Keep dry-run defaults, require named human approval before writes, and restrict network access to authorized systems.

Risk: Installing an external package or connecting to facility networks can introduce supply-chain or access risks.

Mitigation: Verify the pip package source before installation and connect only to authorized building systems.

## Reference(s):

- [iaiops-building ClawHub release](https://clawhub.ai/zw008/skills/iaiops-building)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Configuration guidance]

**Output Format:** [Markdown guidance and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first; equipment commands default to dry run and require named approval.]

## Skill Version(s):

0.32.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
