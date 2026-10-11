## Description:

Guides developers in setting up branch-aware Neon Object Storage and building S3-compatible file upload and download flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure Neon buckets and branch-scoped credentials, implement file uploads and downloads, and troubleshoot object storage alongside their database branches.

### Deployment Geography for Use:

Neon projects in aws-us-east-2, aws-us-east-1, aws-eu-central-1, or aws-ap-southeast-1.

## Known Risks and Mitigations:

Risk: Branch-scoped S3 credentials may be written to local environment files.

Mitigation: Keep environment files out of source control and protect credentials.

Risk: Bucket or object changes and deletes can affect stored files.

Mitigation: Test on preview branches and review delete commands before execution.

Risk: Suggested SDK installation modifies project dependencies.

Mitigation: Review dependency changes before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/andrelandgraf/skills/neon-object-storage)
- [Neon Object Storage overview](https://neon.com/docs/storage/overview.md)
- [Neon Object Storage getting started](https://neon.com/docs/storage/get-started.md)
- [Neon storage authentication](https://neon.com/docs/storage/authentication.md)
- [Neon S3 compatibility](https://neon.com/docs/storage/s3-compatibility.md)
- [Files SDK documentation](https://files-sdk.dev)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Branch-aware S3 setup and file-operation examples]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
