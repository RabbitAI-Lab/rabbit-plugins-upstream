## Description:

PlanetScale (planetscale.com). Use this skill for PlanetScale requests involving reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage PlanetScale organizations, databases, and branches through an OOMOL-connected account, including safe read actions and confirmed create or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create actions can change PlanetScale state, and delete actions can remove databases or branches.

Mitigation: Confirm the exact organization, database, branch, and payload with the user before write actions, and require explicit approval before destructive actions.

Risk: The skill operates through the user's OOMOL-connected PlanetScale account.

Mitigation: Install and use it only when the user intends Codex to manage PlanetScale through that connected account.

## Reference(s):

- [PlanetScale homepage](https://planetscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
