## Description:

Alibaba Cloud OSS helps agents manage Alibaba Cloud Object Storage Service buckets and objects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a task needs to list OSS buckets or objects, inspect object metadata, download objects, generate pre-signed URLs, upload content, or delete objects through an existing OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can install the oo CLI through curl or PowerShell.

Mitigation: Review the installer before running it and install only when Alibaba Cloud OSS management through OOMOL is intended.

Risk: OSS write, overwrite, pre-signed upload/delete URL, and delete actions can change or remove cloud objects.

Mitigation: Confirm bucket names, object keys, payloads, and intended effects with the user before approving write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-oss)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Alibaba Cloud OSS](https://www.alibabacloud.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
