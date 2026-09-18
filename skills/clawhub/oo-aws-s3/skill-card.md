## Description:

AWS S3 helps agents operate Amazon S3 through OOMOL's `oo` CLI, including bucket and object listing, metadata inspection, object transfer, pre-signed URL generation, and confirmed write or delete actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to work with AWS S3 data through an OOMOL-connected account. It supports read workflows such as listing buckets and inspecting objects, plus user-confirmed uploads, deletes, and pre-signed URL generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer a verified, pinned installer or package-manager path before installing the `oo` CLI.

Risk: The skill can upload objects, delete objects, and generate pre-signed URLs that may expose or modify S3 data.

Mitigation: Confirm the exact bucket, key, payload, URL operation, and intended effect with the user before running write, destructive, or pre-signed URL actions.

Risk: The activation scope is broad for AWS S3 requests.

Mitigation: Use the skill only for intended S3 operations through a trusted OOMOL connection, and inspect live action schemas before constructing payloads.

## Reference(s):

- [ClawHub AWS S3 skill page](https://clawhub.ai/oomol/skills/oo-aws-s3)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [AWS S3 homepage](https://aws.amazon.com/s3/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request JSON payloads matching live connector schemas; write, destructive, and pre-signed URL actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
