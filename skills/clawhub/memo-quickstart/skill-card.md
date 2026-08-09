## Description:

记忆快速启动 helps an agent set up a local memory workflow with active session state, persistent JSON memory files, human-readable archives, and CLI commands for storing, searching, archiving, importing, and exporting memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure local, file-based memory for projects where preferences, decisions, lessons, facts, and context need to be saved and retrieved. It is intended for workflows that prefer workspace-local memory files and explicit memory maintenance commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to persist user and project information in workspace memory files by default.

Mitigation: Decide what may be stored before use, require confirmation before saving sensitive preferences or project decisions, and review memory files regularly.

Risk: The security evidence notes conflicting guidance about local-only operation, API keys, and optional cloud sync.

Mitigation: Treat cloud sync and token-related steps as optional, avoid enabling sync unless the upload destination is understood, and review import/export/sync commands before execution.

Risk: The skill asks agents to run local memory CLI commands.

Mitigation: Run only documented memory commands with reviewed arguments and avoid passing untrusted input directly into shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memo-quickstart)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON schema details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file writes and memory CLI commands for an agent to review and execute.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
