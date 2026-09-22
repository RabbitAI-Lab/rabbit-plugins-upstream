## Description:

Queries Huawei Cloud storage resources across EVS, OBS, SFS Turbo, and CBR using read-only local Python scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inventory and inspect Huawei Cloud storage resources, including disks, buckets, file systems, backups, policies, and quotas, without creating, modifying, or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup and network handling create avoidable credential exposure risk.

Mitigation: Use least-privilege, preferably temporary Huawei Cloud credentials and avoid running setup in sensitive environments.

Risk: The dependency setup path may introduce remote-code risk.

Mitigation: Review before installation and require fixes for TLS verification, dependency pinning, and unauthenticated get-pip.py execution before sensitive use.

## Reference(s):

- [CBR Python Script Usage Guide](references/cbr/guide.md)
- [EVS Python Script Usage Guide](references/evs/guide.md)
- [OBS Python Script Usage Guide](references/obs/guide.md)
- [SFS Python Script Usage Guide](references/sfs/guide.md)
- [ClawHub Skill Page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-storage-query)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, text]

**Output Format:** [Markdown guidance with script commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query output depends on Huawei Cloud credentials, region, project, and service-specific filters.]

## Skill Version(s):

9.9.100 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
