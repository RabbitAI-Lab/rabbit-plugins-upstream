## Description:

Alibaba Cloud OSS (alibabacloud.com). Use this skill for Alibaba Cloud OSS requests, including reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Alibaba Cloud OSS action schemas, list buckets and objects, inspect metadata, download objects, upload objects, generate pre-signed URLs, and manage OSS objects through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends mutable remote installer scripts for the oo CLI.

Mitigation: Prefer a pinned, signed, or checksum-verified oo CLI installation method before using the skill.

Risk: The skill can perform write and destructive Alibaba Cloud OSS operations.

Mitigation: Review the live action schema and confirm exact write or delete payloads before approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-oss)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Alibaba Cloud OSS homepage](https://www.alibabacloud.com)
- [Alibaba Cloud OSS icon](https://static.oomol.com/logo/third-party/alibabacloud.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns structured connector responses when actions run with --json.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
