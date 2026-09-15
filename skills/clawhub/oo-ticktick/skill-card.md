## Description:

This skill lets an agent read, create, update, complete, move, and delete TickTick tasks, projects, habits, and check-ins through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage TickTick tasks, projects, habits, check-ins, filters, completions, and moves through a connected OOMOL account. It is intended for TickTick workflows that require both read operations and user-confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may involve direct execution of remote installer scripts.

Mitigation: Install only if comfortable using OOMOL as the TickTick connector, and prefer downloading and verifying the installer before execution.

Risk: Write and destructive actions can modify or delete TickTick data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: The skill depends on the OOMOL CLI, account sign-in, a connected TickTick provider, and available OOMOL billing credits.

Mitigation: Use the documented setup guidance only after a command fails for the matching authentication, connection, CLI, or billing reason.

## Reference(s):

- [ClawHub TickTick Skill](https://clawhub.ai/oomol/skills/oo-ticktick)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [TickTick Homepage](https://ticktick.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects when run with --json.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
