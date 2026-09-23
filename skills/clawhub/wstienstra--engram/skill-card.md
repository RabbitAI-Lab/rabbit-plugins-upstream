## Description:

Engram gives OpenClaw agents a local associative memory graph over workspace content, with CLI tools for recall, message context, task tracking, migration, backup, hygiene, and uninstall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wstienstra](https://clawhub.ai/user/wstienstra)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Engram to give an OpenClaw workspace persistent local memory, retrieve concise context for incoming messages, and maintain a task ledger backed by local SQLite storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Engram keeps persistent local memory state and has broad enough shell and file access to influence a workspace over time.

Mitigation: Install only in a trusted workspace and review the skill before deployment.

Risk: Task evidence strings run through the shell with the user's privileges.

Mitigation: Treat evidence commands as code, and never store evidence commands from untrusted text.

Risk: Migration, rewire, cron setup, logs, backups, and battery reports can affect or expose sensitive workspace data.

Mitigation: Review migration reports and rewire changes before applying them, avoid unattended rewire approval, and handle Engram outputs as sensitive workspace data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wstienstra/skills/engram)
- [Measurement methodology](docs/measurement.md)
- [README](README.md)
- [Skill documentation](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text and Markdown with shell command examples; local CLI output includes short context blocks, recall results, migration reports, and maintenance summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against workspace files and SQLite state; optional localhost Ollama use is user-enabled.]

## Skill Version(s):

1.2.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
