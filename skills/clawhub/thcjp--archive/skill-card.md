## Description:

智能内容归档 captures webpages, videos, tweets, PDFs, images, and notes as searchable Markdown archive snapshots with summaries, metadata, semantic tags, and context-aware resurfacing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge workers, researchers, and project teams use this skill to archive external content into local Markdown snapshots and later retrieve related items through natural-language search or contextual resurfacing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the release as suspicious because it uses broad file and command authority for an archive workflow.

Mitigation: Review the skill before installing and constrain command execution to explicit archive or archive-search tasks where the agent platform supports tool scoping.

Risk: Archiving private or authenticated URLs may store sensitive content locally and may involve LLM or API processing.

Mitigation: Avoid private sources unless local storage and downstream processing are acceptable, and keep archive directories access-controlled.

Risk: The security evidence notes unrelated activation wording that could make the skill run outside archiving contexts.

Mitigation: Use the skill only for explicit archive, retrieval, or archive-search requests and revise activation wording before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/archive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown archive files with frontmatter metadata, plus text search results and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archive items are stored under $HOME/archive/items and may include summaries, key points, tags, project metadata, source URLs, and retrieval context.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
