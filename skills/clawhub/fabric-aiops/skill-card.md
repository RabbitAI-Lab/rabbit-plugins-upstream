## Description:

fabric-aiops helps agents operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network with read workflows, health analysis, and guarded remediation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, SREs, and developers use this skill to inspect managed network fabrics, diagnose WAN and fleet health issues, detect configuration drift, and run controlled remediation through supported controller APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute write operations against production network infrastructure.

Mitigation: Use read-only controller credentials by default and enable write-capable credentials only under an external change-control process.

Risk: The package source is installed remotely and should be trusted before use.

Mitigation: Review the package source and release metadata before installation, and restrict deployment to environments where the publisher and dependency path are acceptable.

Risk: Exported master passwords can become long-lived operational secrets.

Mitigation: Avoid long-lived FABRIC_AIOPS_MASTER_PASSWORD exports and prefer short-lived, scoped execution contexts for non-interactive runs.

Risk: The included verification status says the platform API paths have not yet been exercised against live controllers.

Mitigation: Run fabric-aiops doctor and validate workflows in a low-risk or read-only environment before relying on live remediation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured command guidance for network-fabric operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include controller-derived analysis, dry-run remediation previews, audit-oriented guidance, and explicit unsupported-platform messages.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
