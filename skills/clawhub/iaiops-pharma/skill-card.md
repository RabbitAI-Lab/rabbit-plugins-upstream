## Description:

Pharmaceutical-manufacturing edition of iaiops for GMP drug and biologics plants, covering BACnet/IP BMS and EMS, Modbus water systems, HART-IP transmitters, OPC-UA plant systems, and pharmaceutical checks for cleanroom pressure cascades, particle counts, and PW/WFI water quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, OT engineers, and validation teams use this skill to guide read-first pharmaceutical plant monitoring across BMS, EMS, water, transmitter, DCS, SCADA, and related GMP workflows. It helps agents reason about cleanroom pressure cascades, particle limits supplied by the site, PW/WFI checks, data quality, readiness, investigations, and change-control evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release claims read-only behavior while documenting a high-risk BACnet write tool for operational equipment.

Mitigation: Require either a truly read-only profile with bacnet_write_property removed or machine-disabled, or deploy it as a controlled MOC/write-capable integration with server-side authorization, allowlists, audit logs, and pinned dependencies.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operational guidance; BACnet write behavior requires controlled MOC treatment or removal before production OT/BMS deployment.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
