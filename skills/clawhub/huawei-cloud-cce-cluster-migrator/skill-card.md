## Description:

Guides migration of Kubernetes workloads, container images, persistent storage, and traffic from external clusters to Huawei Cloud CCE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Platform engineers and cluster operators use this skill to plan and carry out migrations to Huawei Cloud CCE, including workload and data transfer, verification, and traffic cutover.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cluster changes and DNS cutover can disrupt running services.

Mitigation: Require an approved migration plan before changes; verify target workloads and test ingress before traffic cutover.

Risk: Migration credentials, exported secrets, and backup data may be exposed.

Mitigation: Run from a trusted operator host with least-privilege access; protect and delete temporary kubeconfigs, secret files, backup credentials, and dumps, and avoid logging sensitive output.

Risk: Downloaded migration tools may introduce untrusted binaries.

Mitigation: Verify downloaded tool binaries before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-cluster-migrator)
- [Pre-migration readiness checklist](references/pre-migration-checklist.md)
- [Storage and persistent volume migration guide](references/storage-pv-migration-guide.md)
- [Container image synchronization guide](references/swr-image-sync-guide.md)
- [Workload backup and restore guide](references/velero-migration-guide.md)
- [Ingress and traffic cutover guide](references/traffic-cutover-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown migration plans and procedural guidance with commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires operator confirmation of migration parameters and approval before changes.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
