## Description:

iaiops is a vendor-neutral industrial and OT router skill that helps agents select the appropriate edition skill and MCP profile for PLCs, controllers, machine tools, IIoT brokers, diagnostics, and downtime analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and OT operators use this skill to route industrial automation tasks to the right iaiops edition skill and MCP profile. It is suited for read-first troubleshooting, protocol selection, site readiness checks, and guided investigation planning across supported industrial and facility protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes agents toward industrial and OT MCP profiles and downstream edition packages that may interact with real equipment.

Mitigation: Use only reviewed profiles and review downstream packages before using the skill on real equipment.

Risk: Write-capable profiles could affect production control systems if enabled without controls.

Mitigation: Do not enable writes against production equipment unless approvals, dry-run behavior, double confirmation, rollback, and downstream tool behavior have been independently verified.

Risk: The separate iaiops-energy package is referenced for energy protocols and is outside this artifact.

Mitigation: Pin or internally mirror the separate iaiops-energy package before installation, as recommended by the server security guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration selections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Router skill; the provided artifact contains no bundled executable code.]

## Skill Version(s):

0.28.0 (source: server evidence release.version and user changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
