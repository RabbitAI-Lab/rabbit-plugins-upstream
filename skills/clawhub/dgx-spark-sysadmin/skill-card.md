## Description:

Administer DGX Spark hosts safely through remote access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbertucci33](https://clawhub.ai/user/cbertucci33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and system administrators use this skill to plan and verify remote administration of single- and multi-node NVIDIA DGX Spark systems, including SSH/Tailscale access, ConnectX-7 fabric setup, monitoring, rolling restarts, reboots, and coordinated platform updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote administration guidance can lead to disruptive system changes such as persistent networking edits, GUI disablement, package or firmware updates, reboots, and power-off actions.

Mitigation: Review each proposed maintenance action before approval, require explicit scope and success criteria, preserve recovery access, and use rollback checks before activation.

Risk: Credential or secret exposure could occur if passwords, private keys, Tailscale auth keys, or tokens are placed in prompts, commands, logs, or files.

Mitigation: Use only approved secret channels, transfer public keys through trusted paths, and avoid including secrets in agent-visible text or shell arguments.

Risk: Multi-node operations can leave hosts inconsistent or unavailable if both nodes are changed or rebooted together.

Mitigation: Make one state change at a time, apply rolling worker-first changes, compare before and after manifests, and treat partial multi-host success as unresolved until reconciled.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cbertucci33/skills/dgx-spark-sysadmin)
- [Server-Resolved GitHub Source](https://github.com/cbertucci33/dgx-spark-sysadmin)
- [NVIDIA DGX Spark User Guide](https://docs.nvidia.com/dgx/dgx-spark/)
- [DGX Spark OS and Component Update Guide](https://docs.nvidia.com/dgx/dgx-spark/os-and-component-update.html)
- [DGX Spark Clustering](https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html)
- [NVIDIA Connect Two Sparks Playbook](https://build.nvidia.com/spark/connect-two-sparks)
- [NVIDIA NCCL for DGX Spark Playbook](https://build.nvidia.com/spark/nccl)
- [Tailscale Linux Installation](https://tailscale.com/docs/install/linux)
- [Tailscale MagicDNS](https://tailscale.com/docs/features/magicdns)
- [Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces administrator-facing procedures, verification gates, rollback checks, and concise status reports; it should not output secrets.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
