## Description:

InfoLobby lets an agent read, query, create, update, and delete InfoLobby workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with InfoLobby workspaces, tables, and records while relying on OOMOL account connections for access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing actions can create or update InfoLobby records.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can remove InfoLobby records.

Mitigation: Confirm the target record and obtain explicit user approval before running delete actions.

Risk: The skill operates through the user's connected InfoLobby account.

Mitigation: Install and use it only when the user intends to grant an agent access to that InfoLobby account.

## Reference(s):

- [ClawHub InfoLobby skill page](https://clawhub.ai/oomol/skills/oo-infolobby)
- [InfoLobby homepage](https://infolobby.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
