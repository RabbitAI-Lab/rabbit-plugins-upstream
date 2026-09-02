## Description:

Pharmaceutical-manufacturing edition of iaiops for GMP drug and biologics plants, covering BACnet/IP BMS and EMS data, Modbus PW/WFI skids and analyzers, HART-IP transmitters, OPC-UA plant systems, and pharma-specific checks for cleanroom pressure cascades, particle limits, and pharma water procedures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and validation teams use this skill to guide agents working with pharmaceutical manufacturing operations, including cleanroom monitoring, pharma water checks, OT asset readiness, deterministic verification, PLC program change baselines, and cross-protocol industrial diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence says the skill claims a read-only posture while documenting a BACnet write function for industrial control systems.

Mitigation: Use only where write tools are disabled or governed by site authorization, named approval, audit logging, dry-run review, undo planning, and change-control procedures before any write action.

Risk: Pharmaceutical manufacturing, cleanroom, and GMP environments can be affected by incorrect operational guidance or unsafe control changes.

Mitigation: Require qualified site review before installation or use in GMP or cleanroom environments, and treat the skill output as guidance that must be validated against site procedures and approved quality standards.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, configuration examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk labels, dry-run guidance, approval steps, status classifications, and cited operational observations.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
