## Description:

Helps agents manage and diagnose Huawei Cloud GaussDB for MySQL and GaussDB for openGauss instances with read-only query and analysis actions plus confirmed lifecycle operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and cloud engineers use this skill to inspect Huawei Cloud GaussDB instances, analyze deployment and security posture, and prepare confirmed operational commands for provisioning, backup, scaling, permission changes, and decommissioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad Huawei Cloud authority for GaussDB lifecycle operations, including instance creation, permission changes, and deletion.

Mitigation: Use least-privilege, preferably temporary credentials; run read-only checks first; and require explicit confirmation before any mutating operation.

Risk: JSON request files for instance creation may contain database administrator passwords.

Mitigation: Protect request files during use, avoid committing them, and delete or rotate them after verification.

Risk: The documented installer pattern fetches the latest KooCLI installer at runtime.

Mitigation: Review the helper script and installer source before use, and pin or verify the CLI version in controlled environments.

Risk: Convenience use of broad managed policies such as GaussDB FullAccess can exceed the authority needed for a specific task.

Mitigation: Start from the least-privilege IAM policies in the artifact references and broaden access only temporarily when the cloud console requires it.

## Reference(s):

- [KooCLI Installation and Authentication Guide](references/cli-installation-guide.md)
- [IAM Policies - GaussDB Least Privilege](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command previews, JSON-oriented CLI results, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only actions may auto-execute; mutating actions require preview and explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
