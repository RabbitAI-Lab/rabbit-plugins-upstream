## Description:

Enables agents to operate AWS S3 through OOMOL's oo CLI, including listing buckets and objects, fetching metadata, downloading objects, uploading objects, deleting objects, and generating presigned URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform AWS S3 read, write, metadata, download, and presigned URL tasks through an OOMOL-connected AWS S3 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload, delete, overwrite, and generate presigned URLs that may expose or modify S3 data.

Mitigation: Require explicit approval with the bucket, key, operation, payload, and URL permission details before running write, destructive, or presigned URL actions.

Risk: The connected AWS credential's S3 permissions determine the scope of data the skill can access or change.

Mitigation: Use least-privilege AWS credentials and review visible buckets and objects before approving state-changing operations.

Risk: First-time setup may involve running a remote installer command.

Mitigation: Verify the installation source independently or use a safer installation method before running the installer.

## Reference(s):

- [ClawHub AWS S3 skill page](https://clawhub.ai/oomol/skills/oo-aws-s3)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [AWS S3 homepage](https://aws.amazon.com/s3/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI plus a connected AWS S3 credential; state-changing actions require explicit approval.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
