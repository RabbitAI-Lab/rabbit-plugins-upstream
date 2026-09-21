## Description:

Mailcoach (mailcoach.app). Use this skill for ANY Mailcoach request - reading, creating, updating, and deleting data. Whenever a task involves Mailcoach, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mailcoach email lists and subscribers through an OOMOL-connected account, including read, write, and destructive account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes one-time setup commands that pipe remote installer scripts directly into a shell.

Mitigation: Review the oo CLI installer before running it, prefer official installation steps with integrity verification where available, and run setup only when the CLI is missing.

Risk: Mailcoach write and destructive actions can change or remove account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Mailcoach skill](https://clawhub.ai/oomol/skills/oo-mailcoach)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Mailcoach homepage](https://www.mailcoach.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas and JSON responses; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
