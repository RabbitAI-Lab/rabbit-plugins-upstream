## Description:

Helps agents set up and use S3-compatible object storage that branches alongside a Neon database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to configure branch-scoped buckets, store and retrieve application files, and connect uploads to database records using Neon Object Storage.

### Deployment Geography for Use:

Available in aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1 regions.

## Known Risks and Mitigations:

Risk: Storage setup or deletion commands may create, modify, or remove buckets and objects.

Mitigation: Review planned changes and confirm the target branch before running bucket or object delete commands.

Risk: Pulling branch-scoped S3 credentials locally may write secrets to an environment file.

Mitigation: Prefer runtime injection where practical and keep local environment files out of source control.

## Reference(s):

- [Neon Object Storage overview](https://neon.com/docs/storage/overview.md)
- [Neon Object Storage getting started](https://neon.com/docs/storage/get-started.md)
- [Neon storage authentication](https://neon.com/docs/storage/authentication.md)
- [Neon S3 compatibility](https://neon.com/docs/storage/s3-compatibility.md)
- [Files SDK documentation](https://files-sdk.dev)
- [ClawHub skill release](https://clawhub.ai/andrelandgraf/skills/neon-object-storage)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide bucket setup, object operations, and branch-scoped credential configuration.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
