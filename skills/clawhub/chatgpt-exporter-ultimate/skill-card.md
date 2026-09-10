## Description:

Exports a user's ChatGPT conversation history through a browser relay or bookmarklet into local JSON and Markdown files, with index-only mode as the default and explicit consent required before full-content export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create local backups or reviewable copies of their own ChatGPT conversation history. It can produce an index-only export by default, or full plaintext conversation files after explicit consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles very sensitive ChatGPT history and can store it as plaintext on disk.

Mitigation: Review before installing, use index-only mode unless full content is necessary, keep exports short-lived, and delete local exports when finished.

Risk: The authoritative security summary reports a verified local symlink flaw that can redirect exported data outside the approved private folder.

Mitigation: Avoid reusing export directories that may contain unexpected files or symlinks until the nested-symlink write issue is fixed.

Risk: Best-effort redaction may not catch all secrets or sensitive content in exported conversations.

Mitigation: Treat exported files as sensitive even when redaction is enabled, and review them before sharing with people, tools, or other agents.

## Reference(s):

- [ChatGPT Exporter on ClawHub](https://clawhub.ai/globalcaos/skills/chatgpt-exporter-ultimate)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [OpenClaw fork repository](https://github.com/globalcaos/clawdbot-moltbot-openclaw)
- [TinkerClaw issues](https://github.com/globalcaos/tinkerclaw/issues)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON and Markdown files with status text and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Index-only mode writes titles, ids, and timestamps by default; full-content mode writes plaintext conversation files after explicit confirmation.]

## Skill Version(s):

1.9.1 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
