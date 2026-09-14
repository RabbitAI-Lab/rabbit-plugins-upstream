## Description:

Fabric AIops helps agents operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network, including fabric health summaries, controller reads, uplink RCA, health scoring, template drift analysis, and guarded remediation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network operators, and agent builders use this skill to inspect controller-managed fabrics, triage WAN and fleet health, review configuration drift, and prepare controlled remediation steps through supported controller APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live network-controller write operations, including high-risk remediation actions that affect production devices and networks.

Mitigation: Use read-only controller credentials by default, grant write-capable credentials only in controlled maintenance contexts, and require dry-run review before state-changing operations.

Risk: The security evidence notes weak built-in write controls; authorization is enforced primarily by the connected controller account and the calling agent's policy.

Mitigation: Constrain write permissions at the controller account level and define explicit agent instructions for observe-only or maintenance-mode sessions.

Risk: The security evidence identifies an unpinned external executable package.

Mitigation: Pin the package version during installation and review updates before upgrading.

Risk: Secrets are required for controller access, and exposing the master password or inline secret values would increase compromise impact.

Mitigation: Avoid passing secrets with command-line values, keep the master password in a protected secret manager, and prefer the encrypted credential store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured controller-operation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk-tiered remediation guidance, dry-run instructions, audit and undo references, and controller-specific limitations.]

## Skill Version(s):

0.11.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
