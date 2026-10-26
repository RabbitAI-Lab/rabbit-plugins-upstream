## Description:

Guides pharmaceutical plant monitoring and diagnostics across BACnet, Modbus, HART-IP, and OPC-UA, including cleanroom and pharmaceutical-water checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical operations and validation teams use this skill to investigate cleanroom conditions, pharmaceutical-water quality, equipment health, and plant data across industrial protocols. Site-approved quality limits and room relationships must be supplied for the relevant checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only claims, a BACnet write operation can change plant systems, including sensitive cleanroom or life-safety equipment.

Mitigation: Treat the skill as write-capable; permit writes only with explicit site authorization and approval gates, and block cleanroom or life-safety writes unless site procedures allow them.

Risk: Incorrect site limits or missing room relationships could lead to misleading cleanroom or water-quality assessments.

Mitigation: Supply site-approved limits and declared room relationships; have qualified staff review results and investigate ungraded or unevaluable checks.

## Reference(s):

- [iaiops-pharma on ClawHub](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with structured findings and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should identify missing limits or readings rather than treating them as passing checks.]

## Skill Version(s):

0.32.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
