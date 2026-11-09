## Description:

Supports management and troubleshooting of VMware AVI (NSX Advanced Load Balancer) virtual services and AKO Kubernetes integrations, including diagnostics, analytics, certificate checks, and selected operational changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Platform and network engineers use this skill to inspect and troubleshoot AVI services and AKO, review certificates and analytics, and perform selected operations using existing AVI Controller and Kubernetes access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected AVI and AKO operations can affect live traffic, restart pods, change Helm configuration, or force synchronization.

Mitigation: Use least-privilege accounts, review the proposed impact or dry-run output, confirm changes deliberately, and verify service health afterward.

Risk: Controller passwords, Kubernetes credentials, and MCP bearer tokens can grant access to infrastructure.

Mitigation: Protect credential files with restrictive permissions or inject secrets from an approved secret manager; use read-only access where practical and keep TLS verification enabled outside isolated labs.

## Reference(s):

- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities and compatibility](references/capabilities.md)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-AVI)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Model fit self-test](https://github.com/vmware-skills/marketplace/blob/main/MODEL_FIT_SELF_TEST.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic findings and recommendations; operational changes require explicit confirmation.]

## Skill Version(s):

2.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
