## Description:

Use this skill to manage vSphere Kubernetes Service environments, including Supervisor compatibility checks, vSphere Namespace lifecycle, TKC cluster creation, scaling, upgrades, deletion, kubeconfig retrieval, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to operate VKS-enabled vSphere environments through agent-guided CLI or MCP workflows. It supports Kubernetes namespace and TKC cluster administration, compatibility checks, storage and Harbor lookups, and kubeconfig retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing operations can create, update, scale, upgrade, or delete live VKS namespaces and TKC clusters.

Mitigation: Use dry-run previews where supported, require explicit approval for writes, double-confirm destructive actions, and review audit logs after production changes.

Risk: Kubeconfig retrieval can expose short-lived bearer tokens if content is printed into an agent conversation or logs.

Mitigation: Write kubeconfig output to a local file path, do not display token-bearing content in chat, and require explicit approval before retrieving production kubeconfigs.

Risk: Administrative credentials and relaxed TLS settings can increase exposure if configured carelessly.

Mitigation: Use least-privilege vCenter accounts, inject passwords from a secret manager when possible, keep local credential files permission-restricted, and prefer TLS verification over verify_ssl:false.

Risk: Unsupported or unverified vSphere versions can lead to incorrect cluster operations.

Mitigation: Run compatibility and preflight checks before lifecycle actions and treat vSphere 9 or VCF 9 environments as requiring additional validation.

## Reference(s):

- [VMware VKS homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, YAML plans, and tool-use recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local file paths for kubeconfig exports; kubeconfig tokens should not be printed into chat logs.]

## Skill Version(s):

1.9.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
