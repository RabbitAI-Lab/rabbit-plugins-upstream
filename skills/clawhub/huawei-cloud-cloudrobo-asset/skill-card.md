## Description:

Manage the full lifecycle of CloudRobo assets, including repository and catalog queries, asset and version CRUD, batch deletion, tag management, Action CRUD, permission checks, marketplace search, official and community asset listing, lineage, and local-to-OBS import and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to manage Huawei CloudRobo asset repositories, catalogs, versions, tags, marketplace discovery, permissions, lineage, and import/export workflows through CLI and SDK-oriented guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles cloud AK/SK credentials and CloudRobo configuration files.

Mitigation: Use least-privileged credentials, protect ~/.cloudrobo/config.yaml, and install only from a trusted CloudRobo client package source.

Risk: Delete, batch-delete, import, export, and Action mutation workflows can change or remove cloud assets.

Mitigation: Require explicit user confirmation before mutation commands and prefer dry-run options when available.

Risk: Disabling TLS verification can expose CloudRobo traffic and credentials.

Mitigation: Keep TLS verification enabled and use CLOUDROBO_VERIFY_SSL=false only for isolated debugging.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-asset)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [API Paths](references/api-paths.md)
- [IAM Policies](references/iam-policies.md)
- [Validation Rules](references/validation-rules.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash commands, JSON examples, and Python SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CloudRobo CLI commands, SDK method patterns, API path references, validation checks, and workflow recovery guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
