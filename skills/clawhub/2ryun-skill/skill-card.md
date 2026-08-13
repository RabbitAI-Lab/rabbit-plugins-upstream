## Description:

Use when the user wants to import documents, build a knowledge base, search structured knowledge, generate websites from content, or publish sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iguoguo](https://clawhub.ai/user/iguoguo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with the 2Ryun REST API for document management, knowledge-base search, knowledge graphs, website generation, publishing, and lightweight notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload documents to 2Ryun, which may expose sensitive content to a third-party service.

Mitigation: Use only non-sensitive documents unless the user has explicitly approved uploading the content to 2Ryun.

Risk: The skill can publish generated pages or sites publicly.

Mitigation: Require explicit user confirmation before publishing any document, generated page, or site.

Risk: The skill can delete remote documents and notes.

Mitigation: Require explicit user confirmation before deleting documents or notes.

## Reference(s):

- [Server-resolved source repository](https://github.com/iguoguo/2Ryun-skill)
- [2Ryun API specification](https://github.com/iguoguo/2Ryun/blob/main/docs/2ryun-api-spec.md)
- [ClawHub skill page](https://clawhub.ai/iguoguo/skills/2ryun-skill)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls, configuration]

**Output Format:** [Markdown guidance with inline shell commands and REST API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, update, publish, or delete remote 2Ryun documents, notes, generated pages, and sites when used with a valid API key.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
