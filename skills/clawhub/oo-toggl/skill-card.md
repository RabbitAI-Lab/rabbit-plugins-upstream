## Description:

Toggl Track lets an agent read, create, update, stop, and delete Toggl Track projects, tasks, tags, workspaces, users, and time entries through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate Toggl Track workflows, including reading workspace data, creating or updating projects and time entries, stopping running entries, and deleting records after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that could be unsafe if run without verifying the installation source.

Mitigation: Use a verified oo CLI installation method or review the installer source before executing setup commands.

Risk: Create, update, stop, and delete actions can change or remove Toggl Track data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Toggl Track homepage](https://toggl.com/track/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Toggl Track Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-toggl)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
