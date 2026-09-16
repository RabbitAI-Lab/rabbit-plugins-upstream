## Description:

Building edition of iaiops for facility, HVAC, BMS, and building automation workflows over BACnet/IP, Modbus, IO-Link, BAS REST layers, optional MQTT, and cross-protocol diagnostics with read-first operation and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facility engineers, and building-operations teams use this skill to inspect building automation systems, collect point and trend data, diagnose dataflow or comfort issues, and draft configuration or operational guidance. Write-capable commands are documented as dry-run and MOC-gated for authorized non-life-safety points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Building automation writes can affect in-service facility equipment.

Mitigation: Keep write-capable BACnet, BAS, and MQTT actions in dry-run mode unless a documented MOC approval and double confirmation authorize changes to non-life-safety points.

Risk: Installing an unpinned external package can introduce supply-chain or version drift risk.

Mitigation: Install only a trusted, pinned release of iaiops[building], preferably with hashes or through an internal package mirror.

Risk: Monitoring credentials and write-capable credentials have different impact levels.

Mitigation: Run the skill under a dedicated least-privilege account and separate read-only monitoring credentials from write-capable credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured text with inline commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflows with bounded scans; write-capable operations are documented as dry-run and MOC-gated by default.]

## Skill Version(s):

0.28.0 (source: server release metadata; changelog source: user)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
