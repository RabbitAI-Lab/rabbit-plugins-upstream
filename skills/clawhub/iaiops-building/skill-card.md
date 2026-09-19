## Description:

Building edition of iaiops for facility automation over BACnet/IP, Modbus, IO-Link, MQTT, and BAS supervisory-controller APIs, with read-first workflows and approval-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facility engineers, and authorized building-automation operators use this skill to discover and read building systems, inspect HVAC and BAS data, diagnose data quality or alarm patterns, and prepare tightly controlled changes. It is intended for authorized environments where write-capable tools remain dry-run unless change approval and rollback are in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can interact with live building automation and HVAC systems, including high-impact write paths.

Mitigation: Use it only on authorized facility systems and keep write tools in dry-run mode unless a real MOC approval and rollback path are in place.

Risk: Installing the `iaiops[building]` package is a supply-chain trust decision.

Mitigation: Install in an isolated, least-privileged environment and pin and verify the package before use.

Risk: Live HVAC or BAS commands may affect operating equipment if change controls are bypassed.

Mitigation: Require explicit approval, preserve rollback or undo information, and avoid safety-critical points unless the site authorization and procedure explicitly permit the action.

## Reference(s):

- [Packaged skill source](artifact/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and structured tool recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only diagnostics, point snapshots, trend summaries, change-control recommendations, and dry-run write plans.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
