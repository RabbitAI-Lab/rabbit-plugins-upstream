## Description:

Provides local associative memory and task tracking for OpenClaw workspaces through commands for storing, migrating, and retrieving information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wstienstra](https://clawhub.ai/user/wstienstra)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users can use Engram to migrate workspace notes into a local memory graph, retrieve relevant context, and track ongoing tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports default Ollama network activity.

Mitigation: Review the effective Ollama settings and disable Ollama if it is not needed.

Risk: Task evidence commands run through the shell with the agent's privileges.

Mitigation: Only add evidence commands you wrote and reviewed; do not use commands supplied by untrusted sources.

Risk: The security scan flags changes to memory, scheduled tasks, and files, including possible state changes during preview runs.

Mitigation: Use a disposable workspace for an initial run, inspect affected files and scheduled tasks, and keep backups before applying changes.

## Reference(s):

- [Engram on ClawHub](https://clawhub.ai/wstienstra/skills/engram)
- [Measurement methodology](docs/measurement.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Retrieved context text, Markdown reports, shell commands, and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved content depends on the local workspace and its stored memories.]

## Skill Version(s):

1.2.3 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
