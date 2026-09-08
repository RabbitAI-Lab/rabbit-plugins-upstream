## Description:

This skill guides agents through the 2Ryun China-site REST APIs for document management, knowledge-base search, webpage generation and publishing, notes, and asset uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iguoguo](https://clawhub.ai/user/iguoguo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect agents to the 2Ryun China site for managing documents, querying structured knowledge, generating and publishing pages, creating notes, and uploading assets. The skill also guides agents on when user content should or should not be added to the knowledge base.

### Deployment Geography for Use:

China site (www.2ryun.wiki); overseas users are directed to the 2ryun.com version.

## Known Risks and Mitigations:

Risk: The skill can help an agent manage a 2Ryun account and publish, share, upload, update, or delete remote content.

Mitigation: Use a narrowly scoped API key where possible and require explicit confirmation before uploads, publishing, sharing, updates, or deletes.

Risk: Documents or uploaded assets may become publicly accessible after publishing or upload workflows.

Mitigation: Confirm the intended audience and sensitivity of documents or assets before making them public.

## Reference(s):

- [2Ryun REST API technical specification](artifact/2ryun-api-spec-cn.md)
- [ClawHub skill page](https://clawhub.ai/iguoguo/skills/2ryun-skill-cn)
- [Server-resolved source repository](https://github.com/iguoguo/2Ryun-skill-cn)
- [2Ryun overseas skill reference](https://github.com/iguoguo/2Ryun-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Configuration]

**Output Format:** [Markdown with inline curl commands, REST endpoint descriptions, JSON request/response examples, and user-facing URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public URLs after publish or upload operations; actions require a 2Ryun API key.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
