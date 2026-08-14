## Description:

fabric-aiops helps agents inspect and operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network, including fabric health summaries, uplink RCA, network health scoring, template drift checks, audited writes, and undo support where available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Network operators, SREs, and infrastructure engineers use this skill to inspect controller-backed network fabric state, diagnose WAN and fleet health issues, and perform limited audited remediation through supported controller APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live infrastructure changes without an in-tool approval or read-only gate.

Mitigation: Use read-only controller accounts by default, enable write-capable accounts only for planned maintenance, and rely on controller permissions as the enforcement boundary.

Risk: Write-capable controller credentials expose sensitive network administration access to the agent environment.

Mitigation: Protect ~/.fabric-aiops and FABRIC_AIOPS_MASTER_PASSWORD as sensitive material, and store controller secrets only through the encrypted secret workflow.

Risk: Unsupported platform operations or unverified controller behavior could lead to incomplete or incorrect operational conclusions.

Mitigation: Treat unsupported-operation responses as hard limits, prefer documented flagship analyses for multi-step diagnosis, and validate against live controller results before operational reliance.

Risk: Reboot and other high-risk remediation actions can affect production devices and may not have a safe inverse.

Mitigation: Use dry-run previews where available, require operator confirmation for destructive CLI actions, and reserve irreversible actions for reviewed maintenance windows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and structured controller-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide live controller reads and writes; write operations should be reviewed, dry-run where supported, and constrained by controller account permissions.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
