## Description:

Run a read-only end-of-session closeout for an OpenClaw workspace and append one closeout block to today's daily memory file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jkfaris94](https://clawhub.ai/user/jkfaris94)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to close a work session by checking repository, task, project-document, and automation hygiene, then recording outcomes, blockers, and next-start items in daily memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes persistent closeout content to workspace memory and lacks enough containment or input hardening.

Mitigation: Run it manually only in trusted workspaces, review CLOSEOUT_* values before execution, and avoid higher-privilege automation until symlink checks and input hardening are added.

## Reference(s):

- [OpenClaw](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Key-value terminal output plus a Markdown closeout block appended to daily memory.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes one closeout block to memory/YYYY-MM-DD.md and reports dirty repositories, MASTER_TODO.md status, project-document warnings, exceptions, and the memory file path.]

## Skill Version(s):

1.1.0 (source: server release metadata and README release notes)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
