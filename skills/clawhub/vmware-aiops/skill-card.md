## Description:

Guides an agent through VMware vSphere and ESXi VM lifecycle, deployment, guest operations, cluster and alarm management, and read-only infrastructure investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and platform engineers use the skill to investigate vSphere and ESXi environments and manage VM lifecycle, deployment, clusters, alarms, and guest operations through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security assessment is suspicious with medium confidence and incomplete coverage; it cites VMware administration capabilities alongside undocumented setup and configuration behavior and broad write access.

Mitigation: Review assistant configuration and external-model setup before installation, and use a dedicated least-privilege VMware account with write safeguards appropriate to the environment.

Risk: Guest operations can run commands and transfer files, while configured webhooks may contain operational details such as host names, IP addresses, and user names.

Mitigation: Use least-privilege guest credentials, send notifications only to trusted configured endpoints, and avoid sharing unredacted diagnostics.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities reference](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Investigation protocol](artifact/references/investigation-protocol.md)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, API Calls, Shell commands, Configuration instructions, Files]

**Output Format:** [Natural-language guidance, VMware tool calls and structured results, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the configured VMware environment; supported actions can change VM and cluster state, run guest commands, and transfer files.]

## Skill Version(s):

2.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
