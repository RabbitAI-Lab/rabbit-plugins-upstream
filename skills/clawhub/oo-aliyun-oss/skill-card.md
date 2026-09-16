## Description:

Use this skill to operate Alibaba Cloud OSS through the OOMOL-connected oo CLI for reading, creating, updating, and deleting storage data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Alibaba Cloud OSS connector schemas and run bucket or object actions through the oo CLI, including listing, metadata lookup, downloads, uploads, presigned URL generation, and deletion. The skill is intended for users with an OOMOL account and connected Alibaba Cloud OSS credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute downloaded scripts.

Mitigation: Avoid running the documented curl|bash or irm|iex installer unless the oo CLI installer source has been independently trusted and verified.

Risk: Alibaba Cloud OSS uploads, deletes, and presigned URLs can modify storage data or expose object access.

Mitigation: Require explicit confirmation of the exact bucket, object, payload, URL operation, and expected effect before running write, destructive, or presigned URL actions.

Risk: Connector actions operate with OOMOL-connected Alibaba Cloud OSS permissions.

Mitigation: Use only an OOMOL account and Alibaba Cloud OSS credentials scoped to resources and actions the user is comfortable exposing to connector execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-oss)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Alibaba Cloud OSS homepage](https://www.alibabacloud.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
