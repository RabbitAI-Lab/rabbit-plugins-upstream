## Description:

Todoist (todoist.com). Use this skill for ANY Todoist request - reading, creating, updating, and deleting data. Whenever a task involves Todoist, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Todoist through an OOMOL-connected account, including listing, creating, updating, commenting on, and completing Todoist tasks, projects, sections, and labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can execute remote installer scripts for the oo CLI.

Mitigation: Review the official oo CLI installation method and use verified packages or checksum/signature guidance where available before running installer commands.

Risk: The skill operates Todoist through OOMOL-connected credentials and can change account data.

Mitigation: Install only if OOMOL is an acceptable intermediary, and require explicit approval before setup, login, write, or task-closing actions.

## Reference(s):

- [ClawHub Todoist skill page](https://clawhub.ai/oomol/skills/oo-todoist)
- [Todoist homepage](https://www.todoist.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Todoist connector calls that read, create, update, or close Todoist records after the agent checks the live action schema.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
