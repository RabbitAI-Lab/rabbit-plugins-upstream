## Description:

Helps agents operate Alibaba Cloud OSS through OOMOL and the oo CLI for reading, creating, updating, and deleting bucket and object data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Alibaba Cloud OSS action schemas, list buckets and objects, view object metadata, download objects, upload content, generate pre-signed URLs, and delete objects through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute remote oo CLI installer scripts.

Mitigation: Manually verify or install the oo CLI through trusted documentation before running installer commands.

Risk: The connected Alibaba Cloud OSS account can perform uploads, deletes, overwrites, and generate pre-signed URLs that grant write or delete access.

Mitigation: Require explicit user confirmation for the exact payload, target bucket or object, and URL permission scope before running state-changing or destructive actions.

Risk: The skill operates through the user's OOMOL-connected Alibaba Cloud OSS account.

Mitigation: Use only with OOMOL and Alibaba Cloud OSS accounts that the user intends the agent to operate.

## Reference(s):

- [Alibaba Cloud OSS homepage](https://www.alibabacloud.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-oss)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; write, overwrite, delete, and write-capable pre-signed URL actions require explicit confirmation.]

## Skill Version(s):

1.0.6 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
