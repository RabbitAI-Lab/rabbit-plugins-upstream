## Description:

Use this skill to manage vSphere Kubernetes Service Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle, kubeconfig access, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to operate VMware VKS environments, including compatibility checks, namespace management, TKC cluster creation and lifecycle changes, kubeconfig export, Harbor checks, and storage usage review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles vCenter and Kubernetes management credentials, including kubeconfigs with bearer tokens.

Mitigation: Use least-privilege service accounts, run kubeconfig retrieval only on explicit request, write credentials to owner-only short-lived files, and delete exported kubeconfigs when no longer needed.

Risk: Kubeconfig export and setup workflows can overwrite local files, including existing kubeconfig paths.

Mitigation: Choose explicit temporary output paths, avoid overwriting ~/.kube/config, and review file destinations before exporting credentials.

Risk: Disabling TLS verification can expose infrastructure access to interception outside managed private-CA exceptions.

Mitigation: Keep TLS verification enabled for CA-signed environments and allow verification bypass only under a documented private-CA exception.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Publisher Profile](https://clawhub.ai/user/zw008)
- [Project Homepage](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct explicit kubeconfig requests to owner-only output files and should report paths instead of credential contents.]

## Skill Version(s):

1.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
