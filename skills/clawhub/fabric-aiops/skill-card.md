## Description:

Helps network operators inspect controller-managed fabrics, diagnose uplink and configuration issues, and perform supported device and network changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operations engineers use this skill to inspect Meraki, Catalyst Center, CloudVision, UniFi, and ACI controller data, investigate fabric health, and carry out supported remediation with appropriate controller permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated operations can change live network-controller state without an internal read-only mode or approval gate.

Mitigation: Start with read-only, least-privilege controller credentials; require explicit human authorization before enabling write-capable credentials or applying changes.

Risk: Controller secrets and local audit data may be exposed on shared machines or through broadly visible environments.

Mitigation: Protect or relocate ~/.fabric-aiops and keep the master password out of broadly visible environment settings.

Risk: Some controller operations cannot be undone after execution.

Mitigation: Review the target and dry-run output before a write, and account for audit and undo limits before rebooting devices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage (declared in skill metadata)](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline commands and structured controller results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Controller results can include ranked health findings and audit or undo information.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
