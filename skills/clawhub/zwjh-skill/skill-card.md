## Description:

zwjh-skill provides a local long-term memory and knowledge graph base for agents, with memory deposit, search, timeline retrieval, health auditing, backup and restore, export and migration, narrative generation, multimodal indexing, and graph visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to persist and retrieve project, customer, and personal context across sessions, organize entities and relationships, audit memory quality, and export or restore memory data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can register a persistent daily scheduled job.

Mitigation: Review the scheduler entry after setup and remove it when automatic memory processing is not desired.

Risk: The skill can ingest arbitrary files and store long-term memory data.

Mitigation: Avoid ingesting sensitive files unless intended and periodically audit stored memory content and backups.

Risk: Restore operations can overwrite or wipe existing memory data.

Mitigation: Treat restore as destructive, verify the source path, and keep a separate backup before restoring.

Risk: Optional Baidu Netdisk backup, remote update manifests, CDN-backed UI, and external LLM adapters can expand privacy boundaries beyond local processing.

Mitigation: Leave optional networked features disabled unless the user accepts those data flows and has reviewed the relevant configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/zwjh-skill)
- [Publisher profile](https://clawhub.ai/user/fyniujin)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain-text agent responses with shell commands, JSON or CSV export files, Cypher export text, and local web UI data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local SQLite data, memory files, backups, scheduled task entries, and optional web UI assets.]

## Skill Version(s):

2.3.0 (source: server release evidence, SKILL.md frontmatter, artifact/version.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
