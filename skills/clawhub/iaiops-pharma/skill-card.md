## Description:

Pharmaceutical-manufacturing edition of iaiops for GMP drug and biologics plants, covering BACnet/IP BMS and EMS, Modbus PW/WFI systems, HART-IP transmitters, OPC-UA DCS and SCADA systems, and pharma-specific checks for cleanroom pressure cascades, particle limits, and water quality procedures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation engineers, validation teams, and plant reliability teams use this skill to guide read-first investigation of pharmaceutical manufacturing environments across BMS, EMS, water, DCS, SCADA, and cross-protocol operational data. It helps structure cleanroom, PW/WFI, alarm, asset, data quality, and change-control workflows while requiring site-confirmed limits and relationships for GMP-sensitive judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as read-only while documenting a BACnet write path and outbound publishing or export tools.

Mitigation: Before connecting to OT networks, confirm write and publishing behavior in the installed implementation, disable or gate write paths, enforce dry-run defaults, and require site approval controls.

Risk: Use in real plant or GMP environments can expose sensitive OT systems and credentials.

Mitigation: Install in an isolated environment with pinned dependencies, least-privilege protocol credentials, destination allowlists, and site-approved network access.

Risk: GMP-sensitive judgments can be wrong if site-confirmed limits, topology, or context are missing.

Mitigation: Require validated plant limits, cleanroom door relationships, and process context from the site; report missing inputs instead of treating them as passing conditions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-pharma)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline commands and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and workflow-oriented; plant-specific GMP limits, topology, credentials, and approval controls must be supplied by the user or site.]

## Skill Version(s):

0.28.0 (source: evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
