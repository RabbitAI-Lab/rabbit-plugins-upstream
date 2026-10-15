## Description:

Helps manage vSphere Kubernetes Service Supervisor namespaces and Tanzu Kubernetes clusters, including compatibility checks, cluster lifecycle operations, and access setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers and developers use this skill to check VKS readiness, manage vSphere namespaces and TKC clusters, and obtain cluster access when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Namespace or cluster changes can affect live workloads.

Mitigation: Use a least-privilege VMware account and expose write operations only when needed; confirm changes before applying them.

Risk: Exported kubeconfigs contain temporary bearer-token access.

Mitigation: Export only on explicit request to an owner-only file, never print the token, and delete the file when finished.

Risk: Disabling TLS verification can expose credentials and management traffic.

Mitigation: Keep TLS verification enabled.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-VKS)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a path to an exported kubeconfig on explicit request; do not display its bearer token.]

## Skill Version(s):

3.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
