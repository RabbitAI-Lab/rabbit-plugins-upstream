## Description:

Helps agents manage document knowledge bases and retrieve source-backed excerpts through semantic search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leonrard](https://clawhub.ai/user/leonrard)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to upload and organize documents, search a knowledge base, and cite relevant excerpts when answering user questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document uploads and search queries are sent to a fixed external service over unencrypted HTTP.

Mitigation: Use only non-sensitive documents unless you control and trust the service; avoid automatic uploads or searches until the endpoint supports HTTPS and configurable destinations.

Risk: Knowledge-base and file deletion can permanently remove content without an explicit confirmation step.

Mitigation: Require explicit user confirmation before any delete operation.

## Reference(s):

- [Knowledge Base Manager on ClawHub](https://clawhub.ai/leonrard/skills/knowledge-base-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with source-attributed search excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results can include source filenames and similarity scores.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
