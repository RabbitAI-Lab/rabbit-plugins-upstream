## Description:

Guides CloudRobo asset management, including repository and catalog discovery, asset and version operations, marketplace searches, and local-to-OBS import and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to discover, manage, and transfer CloudRobo assets and versions with CLI or SDK guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Asset changes, deletions, and imports or exports can affect cloud data.

Mitigation: Preview with dry-run where supported and obtain explicit confirmation before mutating operations.

Risk: AK/SK credentials grant access to assets and OBS storage.

Mitigation: Use least-privilege credentials stored in environment variables or protected configuration; do not hardcode secrets.

Risk: Disabling SSL verification or logging traffic may expose sensitive data.

Mitigation: Keep SSL verification enabled and use traffic logging only temporarily with protected logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-asset)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Asset validation rules](references/validation-rules.md)
- [API paths](references/api-paths.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CloudRobo CLI commands return JSON; import and export transfer asset files.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
