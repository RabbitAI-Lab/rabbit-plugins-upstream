## Description:

Google Tasks (tasks.google.com). Use this skill for ANY Google Tasks request -- reading, creating, updating, and deleting data. Whenever a task involves Google Tasks, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Google Tasks schemas and manage Google Tasks through an OOMOL-connected account, including listing, creating, updating, moving, clearing, and deleting task data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands for the oo CLI, which can execute code on the user's machine.

Mitigation: Review the installer path before installing and prefer official, versioned installation documentation with integrity verification when available.

Risk: Write and destructive Google Tasks actions can create, update, move, clear, or delete user task data.

Mitigation: Confirm the exact task list, task, payload, and expected effect before allowing write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-googletasks)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Google Tasks](https://tasks.google.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include Google Tasks data returned by the googletasks connector; write and destructive actions require confirmation of the target, payload, and effect.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
