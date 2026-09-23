## Description:

文件管理整理 helps an agent organize files and folders by proposing naming conventions, folder structures, file search strategies, desktop and downloads cleanup, and critical-document inventory practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through file organization tasks such as renaming plans, folder restructuring, document retrieval, cleanup workflows, and critical-document tracking. It is most appropriate when the agent has scoped access to the folders being organized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require broad local file access for organization tasks.

Mitigation: Limit agent access to narrow working folders and review proposed changes before allowing execution.

Risk: Moves, renames, archival, or deletion actions can cause data loss or make files harder to find.

Mitigation: Require a preview plan, keep backups, avoid permanent deletion, and retain a move or rename log.

Risk: Callback URLs or API keys could expose file metadata or content to destinations the user does not trust.

Mitigation: Do not provide callback URLs or API keys unless the destination is trusted and the data flow is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include previewable plans before file moves, renames, deletion, or archival actions.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
