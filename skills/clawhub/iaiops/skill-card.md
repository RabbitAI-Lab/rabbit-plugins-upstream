## Description:

Vendor-neutral, governed industrial and OT routing skill for selecting iaiops edition skills and MCP profiles for PLCs, controllers, machine tools, IIoT brokers, diagnostics, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial/OT engineers use this skill to route industrial protocol, PLC, SCADA, historian, fab equipment, building systems, and downtime analysis requests to the appropriate iaiops edition skill and MCP profile. It is intended to keep tool exposure scoped while preserving read-first behavior and approval-gated writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial-control routing could select the wrong domain or protocol profile, especially around substation and energy use cases.

Mitigation: Review routing instructions before use and select the separate iaiops-energy package for substation or energy protocols when applicable.

Risk: Write-capable OT operations could affect production control systems if used without proper controls.

Mitigation: Keep write operations dry-run by default, require explicit approval, and confirm the intended MCP profile before any production action.

Risk: Advisory troubleshooting output could be mistaken for verified operational fact.

Mitigation: Treat AI conclusions as advisory and require cited signal evidence or an insufficient-evidence result for operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown guidance with inline configuration values and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes agent tasks to edition skills and MCP profiles; write operations are described as dry-run and approval-gated.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
