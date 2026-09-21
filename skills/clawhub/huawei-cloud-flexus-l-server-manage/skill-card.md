## Description:

Manages Huawei Cloud Flexus L server lifecycle: create, renew, and unsubscribe instances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and cloud administrators use this skill to inspect Huawei Cloud Flexus L regions, images, and specifications, then create, renew, or unsubscribe Flexus L instances. It is intended for managed cloud lifecycle workflows where billing impact, credentials, and resource IDs are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles billing and destructive Huawei Cloud lifecycle operations, including instance creation, renewal, and unsubscribe actions.

Mitigation: Use dry-run previews first, verify exact resource IDs and billing impact, and avoid the --confirm shortcut until the intended action has been reviewed.

Risk: The security summary reports that this version disables TLS verification while performing privileged cloud operations.

Mitigation: Do not use this version for privileged operations unless TLS verification is fixed; review network trust before installation.

Risk: The skill requires credentials and may be configured with broad Huawei Cloud permissions.

Mitigation: Use a dedicated least-privilege Huawei Cloud user or temporary credentials, pass secrets through environment variables, and avoid exposing access keys or tokens in conversation or logs.

## Reference(s):

- [Skill release page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-manage)
- [API Reference](references/api-reference.md)
- [IAM Permissions Guide](references/iam-policies.md)
- [Permission Guide](references/permission-guide.md)
- [Flexus L System Images and Specifications Reference](references/image-specs-guide.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Huawei Cloud Flexus L Instance Purchase API](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html)
- [Huawei Cloud IAM Authentication Guide](https://support.huaweicloud.com/api-iam/iam_01_0001.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, resource identifiers, region/image/spec selections, and confirmation prompts for billing or destructive operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
