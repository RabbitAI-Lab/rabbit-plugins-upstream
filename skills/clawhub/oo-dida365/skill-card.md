## Description:

Dida365 lets an agent read, create, update, complete, move, and delete Dida365 projects, tasks, and habit data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Dida365 task, project, and habit workflows from a connected OOMOL account. It supports both read-only lookups and state-changing actions that require confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions can run a remote install script on the user's machine.

Mitigation: Review the setup steps before installing, prefer a verified documented source with version and integrity checks, and only run setup after an actual missing-CLI or authentication failure.

Risk: Write and destructive actions can change, move, or delete Dida365 projects, tasks, and habit check-ins.

Mitigation: Confirm the exact target item, payload, and expected effect with the user before running actions marked write or destructive.

## Reference(s):

- [Dida365 homepage](https://dida365.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dida365)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may read or change Dida365 account data depending on the selected action.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
