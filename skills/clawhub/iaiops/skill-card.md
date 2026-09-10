## Description:

iaiops routes industrial and OT troubleshooting requests to the appropriate edition skill and MCP profile for read-first diagnostics, asset and OEE analysis, and gated control-system writes across common plant protocols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial operations engineers, automation engineers, and site reliability teams use this skill to route OT data, diagnostics, readiness checks, and downtime investigations to the correct industry or protocol edition. It is intended for governed, read-first workflows over PLCs, controllers, machine tools, IIoT brokers, building systems, and related industrial assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A real write to a production control system could affect industrial equipment or site operations.

Mitigation: Use read-first workflows, keep dry-run enabled until reviewed, require named approval, and double-confirm any real write before execution.

Risk: Selecting the wrong edition or MCP profile could route the agent toward tools that do not match the site or protocol.

Mitigation: Verify the selected edition/profile and run readiness, doctor, or protocols_supported checks before attempting operational actions.

Risk: Inferring tag roles, process relationships, or root causes without site knowledge can produce misleading OEE or downtime conclusions.

Mitigation: Require human-provided tag roles and declared process relationships, cite observed signals, and return insufficient_evidence when support is missing.

## Reference(s):

- [iaiops skill page](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first routing guidance with dry-run and approval notes for high-impact writes.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
