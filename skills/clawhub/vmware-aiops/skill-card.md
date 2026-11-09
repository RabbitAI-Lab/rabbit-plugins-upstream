## Description:

Manages VMware vSphere and ESXi virtual machine lifecycle, deployment, guest operations, clusters, alarms, and infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to inspect VMware environments and manage VM lifecycle, deployment, guest operations, clusters, alarms, and investigations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious with medium confidence; six of seven components were fully inspected, and obfuscated text in the capabilities reference could not be fully evaluated.

Mitigation: Review the incomplete scan and flagged tool-use guidance before installation; use least-privilege vCenter and guest accounts, and inspect operation previews before confirming state changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities and safety details](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Investigation protocol](artifact/references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured tool calls, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational plans and result summaries.]

## Skill Version(s):

2.4.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
