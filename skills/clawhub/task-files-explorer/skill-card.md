## Description:

Task Files Explorer helps agents deploy a zero-dependency local file dashboard for task download and archive files, with search, filters, sorting, inline previews, and per-task grouping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when they need a persistent task-file explorer served through a platform preview URL instead of relying on the default file preview popup. It is intended for file browsing and preview workflows, not for projects where a web application already owns port 3000.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a persistent preview service for task files.

Mitigation: Enable it only with clear operator opt-in, document how to stop and uninstall it, and remove PID files, logs, boot hooks, watcher files, and background processes when no longer needed.

Risk: Preview URLs may expose task files if access controls are not understood or configured.

Mitigation: Confirm preview URL access controls before deployment, limit exposed roots to the intended task-file directories, and avoid serving sensitive files.

Risk: The boot-hook template can auto-run project startup commands.

Mitigation: Review and remove automatic install, database push, and dev-server startup blocks unless the project explicitly requires them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/task-files-explorer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deployment and control instructions for a local file explorer service.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
