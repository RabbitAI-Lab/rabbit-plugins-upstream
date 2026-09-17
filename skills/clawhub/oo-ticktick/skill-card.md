## Description:

TickTick (ticktick.com). Use this skill for ANY TickTick request - reading, creating, updating, and deleting data. Whenever a task involves TickTick, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage TickTick tasks, projects, habits, check-ins, filters, completions, and task moves through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute changing code on the user's machine.

Mitigation: Independently verify the oo CLI installer or use a trusted installation path before running setup commands.

Risk: OOMOL acts as an intermediary for TickTick actions.

Mitigation: Install only when the user accepts this intermediary and has connected the intended TickTick account.

Risk: Write and destructive actions can create, update, move, complete, or delete TickTick data.

Mitigation: Require explicit user confirmation for the exact payload and target before running write or destructive actions.

## Reference(s):

- [TickTick homepage](https://ticktick.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ticktick)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live TickTick connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
