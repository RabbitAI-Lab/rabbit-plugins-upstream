## Description:

vmware-vks helps agents manage vSphere Kubernetes Service environments, including Supervisor checks, vSphere Namespaces, TKC cluster lifecycle tasks, kubeconfig retrieval, Harbor registry checks, and storage usage review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and VMware operators use this skill to inspect VKS readiness and manage vSphere Namespaces and Tanzu Kubernetes clusters through CLI or MCP workflows. It is intended for environments where an agent may need to plan, preview, and execute Kubernetes cluster lifecycle operations against configured vCenter targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer VMware VKS/TKC resources and may affect namespaces, clusters, and running workloads.

Mitigation: Use a least-privilege vCenter account and review each write preview or blast-radius summary before approving execution.

Risk: Kubeconfig retrieval returns live bearer-token credentials for Supervisor or TKC access.

Mitigation: Fetch kubeconfigs only on explicit request, write them to short-lived owner-only files, report only the path, and avoid printing tokens into chat.

Risk: Local .env files, exported kubeconfigs, and audit logs can contain sensitive operational data or credentials.

Mitigation: Keep these files owner-only, rotate or delete them according to retention policy, and avoid long-lived exported kubeconfig files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [VMware VKS homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](artifact/references/capabilities.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration snippets, and structured MCP tool recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct credential exports to owner-only files and should report file paths rather than secret material.]

## Skill Version(s):

1.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
