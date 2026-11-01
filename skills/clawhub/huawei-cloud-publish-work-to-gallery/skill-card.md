## Description:

Publishes a user's project to the Huawei Cloud University Operations Platform gallery or an activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to prepare and submit a local project to the Huawei Cloud University Operations Platform gallery or an activity. It guides the user through the required choices and asks for confirmation before submitting the work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publishing workflow can expose local project files or cloud credentials.

Mitigation: Use narrowly scoped credentials in a private temporary directory, avoid printing secrets in diagnostics, and inspect the packaged archive before submission.

Risk: Dependency setup and remote helper binaries may introduce unsafe or unverified components.

Mitigation: Use an isolated non-admin environment and a corrected release with contained dependency setup and verified downloads.

Risk: Process cleanup or an active tunnel can disrupt other programs or leave access open.

Mitigation: Use ownership-checked process cleanup and stop any tunnel when it is no longer needed.

## Reference(s):

- [Huawei Cloud Gallery API Specification](references/api-spec.md)
- [IAM Policies](references/iam-policies.md)
- [Work Preparation Guide](references/work-preparation.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Huawei Cloud Gallery Platform](https://gallery.developer.huaweicloud.com)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Files]

**Output Format:** [Markdown guidance and status text, with generated cover images and a project detail archive]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can submit a selected project to the gallery after user confirmation.]

## Skill Version(s):

2026.10.15.001 (source: artifact frontmatter; ClawHub release: 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
