## Description:

Vendor-neutral, governed industrial/OT routing for selecting iaiops edition skills and MCP profiles for PLC, controller, machine-tool, IIoT, building, fab, and cross-protocol troubleshooting tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, OT engineers, and site reliability teams use this routing skill to select the right iaiops edition skill and MCP profile for industrial protocol diagnostics, OEE and downtime analysis, asset inventory, readiness checks, and governed read-first troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial/OT device writes can affect production systems when an edition skill exposes write-capable tools.

Mitigation: Keep read-first workflows as the default, leave dry-run enabled for write proposals, and require named approval and documented human review before changing production control systems.

Risk: Incorrect site semantics or incomplete evidence can lead to misleading OEE, downtime, or root-cause conclusions.

Mitigation: Use the readiness and investigation planning steps first, preserve source signal references, and require site personnel to provide tag roles and process relationships instead of inferring them.

Risk: Endpoint credentials are needed for real industrial environments.

Mitigation: Configure credentials only in the documented encrypted store and install the skill only for intended industrial/OT diagnostic use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes the agent to edition skills and MCP profiles; write operations are described as gated, dry-run-first actions requiring named approval.]

## Skill Version(s):

0.23.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
