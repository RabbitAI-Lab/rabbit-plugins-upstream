## Description:

Alibaba Cloud OSS (alibabacloud.com). Use this skill for ANY Alibaba Cloud OSS request — reading, creating, updating, and deleting data. Whenever a task involves Alibaba Cloud OSS, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Alibaba Cloud OSS through an OOMOL-connected account, including bucket discovery, object listing, metadata checks, downloads, uploads, deletes, and pre-signed URL generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A pre-signed URL can grant upload or delete authority without being labeled as a write or destructive action.

Mitigation: Require explicit confirmation of the bucket, object key, operation, expiry, and recipient before generating pre-signed URLs for upload or delete.

Risk: Write or destructive OSS actions can change or remove cloud data.

Mitigation: Confirm the exact payload and expected effect with the user before running upload, overwrite, or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-aliyun-oss)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Alibaba Cloud OSS](https://www.alibabacloud.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas and run Alibaba Cloud OSS actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
