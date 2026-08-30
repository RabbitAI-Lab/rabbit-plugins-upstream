## Description:

AWS S3 helps agents operate Amazon S3 through OOMOL's aws_s3 connector for listing buckets and objects, reading metadata, downloading, uploading, generating pre-signed URLs, and deleting objects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill when an agent needs to inspect or change AWS S3 data through an OOMOL-connected account. It supports read workflows, object upload, pre-signed URL generation, and guarded object deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: S3 buckets may contain sensitive or business-critical data, and the skill can read, upload, generate URLs for, or delete objects.

Mitigation: Review the target bucket, object key, payload, and intended effect before write, URL-generation, or destructive actions.

Risk: Pre-signed URL generation is sensitive because it can grant access outside the agent session.

Mitigation: Allow URL generation only when the object, permission type, recipient, and expiration are clear.

Risk: The security summary flags one URL-generation action as under-scoped compared with the skill's own safety rules.

Mitigation: Treat pre-signed URL requests as approval-gated and verify the live connector schema before constructing the payload.

Risk: The skill depends on the OOMOL connector and oo CLI setup flow.

Mitigation: Approve setup commands such as installing the oo CLI only when OOMOL is trusted as the connector provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aws-s3)
- [AWS S3 homepage](https://aws.amazon.com/s3/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
