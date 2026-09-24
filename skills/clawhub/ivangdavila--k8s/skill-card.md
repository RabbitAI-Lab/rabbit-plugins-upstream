## Description:

Debugs Kubernetes workloads and reviews manifests across pods, probes, resources, rollouts, Services, storage, RBAC, networking, autoscaling, nodes, control-plane health, GPU scheduling, backup, and restore workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and platform engineers use this skill to troubleshoot Kubernetes incidents, review deployment YAML, and plan safer cluster operations. It is useful for diagnosing workload failures, networking issues, rollout problems, resource sizing, access controls, storage, node operations, and production readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide powerful kubectl workflows that affect live infrastructure.

Mitigation: Use least-privilege Kubernetes credentials and require explicit confirmation before node debugging, deletes, drains, force operations, or other state-changing commands.

Risk: Cluster debugging can expose secret-prone output such as environment variables, kubeconfig details, Secret manifests, and command logs.

Mitigation: Avoid full environment dumps unless necessary, strip credential values before saving notes, and store only pointers such as environment variables, file paths, keychain entries, or vault locations.

Risk: The skill keeps local operational memory about clusters and incidents.

Mitigation: Protect the local Clawic data directories, limit shared-machine access, and periodically delete stale operational notes.

Risk: Debug images and ephemeral containers can broaden access during an incident.

Mitigation: Prefer approved, digest-pinned debug images and review the namespace, target pod, and expected blast radius before running debug commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/k8s)
- [Clawic Kubernetes skill page](https://clawic.com/skills/k8s)
- [Kubernetes skill definition](artifact/SKILL.md)
- [kubectl incident toolkit](artifact/commands.md)
- [Kubernetes security guidance](artifact/security.md)
- [Manifest review guidance](artifact/manifests.md)
- [Production readiness guidance](artifact/production.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and Kubernetes YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose state-changing Kubernetes commands; user review and explicit confirmation are expected before destructive operations.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
