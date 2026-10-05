## Description:

Helps agents inspect and manage Huawei Cloud IAM users, groups, policies, agencies, login settings, and access keys through the hcloud CLI with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to audit IAM access and manage identities, permissions, agencies, and credentials in a configured Huawei Cloud account. It previews changes and asks for confirmation before write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: IAM changes can delete identities, grant broad privileges, or authorize another account.

Mitigation: Use a sandbox or least-privilege account; review target, affected resources, and warnings before explicitly confirming each write.

Risk: The telemetry CLI installer downloads remote software and persists a PATH change.

Mitigation: Review the installer, prefer manual dependency installation with pinned checksums, and run it only if shell profile changes are acceptable.

Risk: Password and access-key operations handle sensitive credentials.

Mitigation: Avoid logging secrets, show a new secret access key only once, and handle credentials in a sandbox or least-privilege account.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-iam-manage)
- [Huawei Cloud IAM API reference](https://support.huaweicloud.com/api-iam/iam_18_0001.html)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/IAM/doc)
- [CLI installation and authentication](references/cli-installation-guide.md)
- [Least-privilege IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and JSON summaries with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows write previews and impact lists; access key secrets are displayed only once.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
