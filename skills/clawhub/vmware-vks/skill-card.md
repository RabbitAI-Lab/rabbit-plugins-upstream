## Description:

Manages vSphere Kubernetes Service environments by checking compatibility and handling Supervisor namespaces and Tanzu Kubernetes clusters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform administrators use this skill to inspect VKS compatibility and manage vSphere Namespaces and Tanzu Kubernetes clusters, including lifecycle operations and access retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marked the skill suspicious because it handles powerful credentials and identified incomplete analysis, instruction-scope concerns, and an unpinned setup command.

Mitigation: Review the unscanned referenced content and pin the setup dependency before installation, as advised by the security guidance.

Risk: Kubeconfig exports contain a bearer token that acts as the configured vCenter account until it expires.

Mitigation: Retrieve a kubeconfig only when explicitly needed, write it to an owner-only file, keep it out of chat, and remove it when finished.

Risk: Deleting a namespace or TKC cluster can destroy resources and disrupt running workloads.

Mitigation: Review the reported blast radius and affected workloads before confirming a delete.

## Reference(s):

- [Project homepage](https://github.com/vmware-skills/VMware-VKS)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text and structured responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report live environment data and proposed changes; kubeconfig retrieval returns a bearer token that should be saved to a protected file.]

## Skill Version(s):

3.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
