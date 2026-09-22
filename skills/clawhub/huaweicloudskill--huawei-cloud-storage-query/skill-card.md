## Description:

Queries Huawei Cloud storage resources across EVS, OBS, SFS Turbo, and CBR using read-only local Python scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to inspect Huawei Cloud storage inventory, configuration, quotas, policies, backups, snapshots, and object metadata without making write changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and API clients may disable TLS verification while Huawei Cloud credentials are present.

Mitigation: Enable TLS certificate verification before routine use and run setup or query operations in an isolated environment.

Risk: Dependency installation can fetch or execute network code during environment preparation.

Mitigation: Pin and hash dependencies, avoid trusted-host package installs, and review setup behavior before installing.

Risk: Cloud query credentials may expose sensitive storage metadata if overprivileged.

Mitigation: Use least-privilege, read-only Huawei Cloud credentials and avoid logging or returning secret environment variable values.

## Reference(s):

- [OBS Python Script Usage Guide](references/obs/guide.md)
- [SFS Python Script Usage Guide](references/sfs/guide.md)
- [EVS Python Script Usage Guide](references/evs/guide.md)
- [CBR Python Script Usage Guide](references/cbr/guide.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-storage-query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown responses with script execution guidance and JSON or tabular query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query outputs depend on Huawei Cloud credentials, region, project scope, and selected service script.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
