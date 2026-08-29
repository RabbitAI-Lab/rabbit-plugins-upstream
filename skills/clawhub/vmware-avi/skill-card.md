## Description:

Helps agents operate VMware AVI / NSX Advanced Load Balancer and AKO environments by inspecting load-balancing state, troubleshooting ingress and sync issues, and preparing approved traffic or configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure, platform, and SRE teams use this skill to inspect AVI virtual services, pools, certificates, service engines, AKO pods, Helm configuration, ingress mappings, and Kubernetes-to-Controller sync state, and to prepare approved operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and, with approval, modify AVI/AKO infrastructure that may affect live application delivery.

Mitigation: Use least-privilege AVI and Kubernetes credentials, require explicit approval for writes, and review proposed changes before execution.

Risk: Controller passwords and Kubernetes access material are sensitive and may be exposed if stored or passed carelessly.

Mitigation: Keep ~/.vmware-avi/.env chmod 600, prefer a secret manager for production credentials, and avoid placing real passwords directly in shell commands.

Risk: Disabling TLS verification or using curl -k can hide certificate and interception problems in production validation.

Mitigation: Use valid TLS certificates in production and reserve TLS bypass settings for controlled lab environments only.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-avi)
- [VMware AVI Homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI Capabilities](references/capabilities.md)
- [VMware AVI CLI Reference](references/cli-reference.md)
- [VMware AVI Setup Guide](references/setup-guide.md)
- [Operating vmware-avi with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational observations, troubleshooting steps, approval-gated change plans, and tool-result summaries.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
