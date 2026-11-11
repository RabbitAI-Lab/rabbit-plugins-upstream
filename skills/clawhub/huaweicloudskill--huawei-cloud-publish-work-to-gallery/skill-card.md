## Description:

Publish a user's work to the Huawei Cloud University Operations Platform gallery or an activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to prepare and publish a project to the Huawei Cloud University Operations Platform gallery or an activity. It guides project selection, authorization, presentation materials, activity selection, and submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and account access may be exposed through credential files or diagnostic output during authorization and publishing.

Mitigation: Use an isolated, non-administrator environment, protect credential files, remove secret-printing diagnostics, and do not upload credentials with project files.

Risk: Automatic setup can change the local environment and downloads executable dependencies.

Mitigation: Verify downloaded executables and keep setup confined to one Python environment.

Risk: Shared temporary files and archive symlink handling can affect the integrity of data prepared for upload.

Mitigation: Use a trusted temporary-file environment, address archive symlink handling before real submissions, and inspect the final upload contents.

Risk: IAM delegation and a persistent tunnel can grant or retain access beyond a single publishing step.

Mitigation: Review and explicitly approve the IAM delegation and any lasting tunnel before use.

## Reference(s):

- [Huawei Cloud gallery platform](https://gallery.developer.huaweicloud.com)
- [API specification](artifact/references/api-spec.md)
- [IAM policies](artifact/references/iam-policies.md)
- [Self-verification and publishing](artifact/references/self-verify-publish.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [API error codes](artifact/references/error-codes.md)
- [Work preparation](artifact/references/work-preparation.md)
- [DevBridge tunnel guidance](artifact/references/devbridge-tunnel.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, JSON parameters, and generated cover and detail archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user choices and, for publishing, interactive authorization; produces a cover image and a ZIP of project details before submission.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
