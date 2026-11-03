## Description:

Use this skill to manage vSphere Kubernetes Service (VKS) Supervisor clusters, vSphere Namespaces, and Tanzu Kubernetes Cluster (TKC) lifecycles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

vSphere administrators and platform engineers use this skill to inspect VKS compatibility and manage Supervisor namespaces and TKC clusters. It can also retrieve Harbor and storage information and write a kubeconfig file when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Namespace and TKC changes can disrupt running workloads or remove resources.

Mitigation: Review the operation preview and its blast radius; proceed with disruptive changes only after the user approves them.

Risk: Exported kubeconfigs contain bearer tokens that act as the configured vCenter account until they expire.

Mitigation: Retrieve them only on explicit request, write them to an owner-only file, report the file path rather than its contents, and delete the file when no longer needed.

Risk: Optional HTTPS serving can expose shared privileged access.

Mitigation: Expose only the needed tools to trusted users, restrict network access, and keep TLS verification enabled.

## Reference(s):

- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Project homepage](https://github.com/vmware-skills/VMware-VKS)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-vks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured operation results, with shell command examples when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write kubeconfig files on explicit request; keep bearer tokens out of chat.]

## Skill Version(s):

3.4.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
