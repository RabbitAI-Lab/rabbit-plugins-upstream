## Description:

AWS S3 helps agents operate Amazon S3 through an OOMOL-connected account for reading, creating, updating, and deleting S3 data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect buckets and objects, download objects, upload content, generate presigned URLs, and delete S3 objects through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could execute unverified code.

Mitigation: Prefer a versioned, verifiable oo CLI package, or inspect and verify the downloaded installer before running it.

Risk: S3 write, delete, and presigned URL actions can change data access or remove objects.

Mitigation: Confirm the exact bucket, object key, action, and payload with the user before allowing write, destructive, or presigned URL operations.

## Reference(s):

- [ClawHub AWS S3 skill page](https://clawhub.ai/oomol/skills/oo-aws-s3)
- [AWS S3 homepage](https://aws.amazon.com/s3/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
