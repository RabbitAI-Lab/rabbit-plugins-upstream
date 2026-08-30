## Description:

Helps agents manage vSphere Kubernetes Service environments, including Supervisor compatibility, vSphere Namespace lifecycle, TKC cluster lifecycle, kubeconfig retrieval, Harbor registry checks, and storage usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Platform engineers, vSphere administrators, and developers use this skill to inspect and operate vSphere Kubernetes Service resources through agent-guided CLI or MCP workflows. It supports namespace, TKC cluster, kubeconfig, Harbor registry, compatibility, and storage-usage tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live access tokens or local vCenter secrets could be exposed during kubeconfig or credential handling.

Mitigation: Avoid printing kubeconfigs in chat, export kubeconfigs only to protected paths, use least-privilege service accounts, and inject passwords from a secret manager where possible.

Risk: Production vSphere Kubernetes administration can affect running workloads if write operations are approved without review.

Mitigation: Review the skill before production installation, use policy and audit controls, keep dry-run previews for create operations, and require explicit approval for state-changing actions.

Risk: Disabling TLS verification can weaken trust in connections to vCenter.

Mitigation: Prefer `verify_ssl: true` with a trusted vCenter CA in production environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce kubeconfig file paths and operational plans; credentials and tokens should not be printed in agent conversation.]

## Skill Version(s):

1.8.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
