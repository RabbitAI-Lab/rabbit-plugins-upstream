## Description:

Use when the user wants to import documents, build a knowledge base, search structured knowledge, generate websites from content, or publish sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iguoguo](https://clawhub.ai/user/iguoguo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage 2Ryun documents, notes, knowledge-base search, website generation, publishing, and media attachments through the 2Ryun REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload, delete, extract, and publish user content through a 2Ryun API key.

Mitigation: Confirm the exact files, documents, and public visibility before upload, delete, import, extraction, or publish actions.

Risk: Sensitive, personal, business, or regulated content could be exposed through uploads, knowledge extraction, or public publishing.

Mitigation: Avoid using the skill with sensitive or regulated material unless the user has reviewed the exposure risk and explicitly approves the action.

## Reference(s):

- [Server-resolved GitHub import: iguoguo/2Ryun-skill](https://github.com/iguoguo/2Ryun-skill)
- [2Ryun API specification](2ryun-api-spec.md)
- [2Ryun platform](https://2ryun.com)
- [ClawHub release page](https://clawhub.ai/iguoguo/skills/2ryun-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, API calls, configuration]

**Output Format:** [Markdown with inline shell commands and REST API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public URLs after publishing generated pages, sites, or uploaded assets.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
