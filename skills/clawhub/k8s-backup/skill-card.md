## Description: <br>
Kubernetes backup and restore with Velero. Use when creating backups, restoring applications, managing disaster recovery, or migrating workloads between clusters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and platform engineers use this skill to create, inspect, restore, and schedule Velero backups for Kubernetes workloads during operations, migration, and disaster recovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restore or schedule actions may affect the wrong Kubernetes cluster or namespace if the active context or namespace mappings are incorrect. <br>
Mitigation: Verify the active Kubernetes context, target cluster, namespace mappings, backup name, and included resources before running restore or schedule steps. <br>
Risk: Velero backups and restores may include Kubernetes Secrets and other sensitive configuration. <br>
Mitigation: Decide explicitly whether Secrets should be included or restored, and protect Velero backup storage with access controls appropriate for credential-bearing data. <br>
Risk: Powerful restore examples can change live cluster state. <br>
Mitigation: Inspect backup status and restore details before proceeding, and monitor restore completion after execution. <br>


## Reference(s): <br>
- [Kubernetes Skills on ClawHub](https://clawhub.ai/rohitg00/skills/k8s-backup) <br>
- [Publisher profile](https://clawhub.ai/user/rohitg00) <br>
- [Related skill: k8s-multicluster](../k8s-multicluster/SKILL.md) <br>
- [Related skill: k8s-incident](../k8s-incident/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python-style tool-call examples and Kubernetes YAML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
