## Description:

Inspects Oracle Linux Virtualization Manager and oVirt 4.5 environments and provides ranked health, capacity, and troubleshooting findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers use this skill to inspect OLVM and oVirt 4.5 inventory, review engine activity, and troubleshoot engine, host, storage, and VM health through read-only reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engine credentials and local credential and audit files are sensitive; credential encryption and audit enforcement were not verified from executable package code.

Mitigation: Use a dedicated read-only engine account and protect the master password and local files; verify these controls in the reviewed release before relying on them.

Risk: Installation and MCP launch commands may not pin the package to a reviewed release.

Mitigation: Pin standalone installation and MCP launch commands to a reviewed release.

Risk: Disabling TLS certificate verification weakens protection for engine connections.

Mitigation: Keep certificate verification enabled and configure the engine CA and FQDN.

## Reference(s):

- [Project homepage (metadata link)](https://github.com/AIops-tools/OLVM-AIops)
- [ClawHub release page](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured JSON and concise text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory and diagnostic findings are ranked and read-only.]

## Skill Version(s):

0.7.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
