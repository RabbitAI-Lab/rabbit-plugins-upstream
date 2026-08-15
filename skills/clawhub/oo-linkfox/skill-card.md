## Description:

LinkFox (linkfox.com). Use this skill for ANY LinkFox request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce operators use this skill to let an agent retrieve LinkFox-connected marketplace, advertising, store, campaign, order, sourcing, and product compliance information through OOMOL-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve commerce, advertising, store, order, campaign, and report data from an OOMOL-connected LinkFox account.

Mitigation: Install it only when that account access is expected, and confirm the requested LinkFox action before running account-scoped commands.

Risk: First-time setup may require installing the oo CLI and connecting a LinkFox account.

Mitigation: Review the oo CLI installer before setup and use the connection flow only after an authentication or connection error requires it.

Risk: Future LinkFox actions tagged write or destructive, or actions that could change account state, may have side effects.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running those actions.

## Reference(s):

- [LinkFox homepage](https://www.linkfox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub LinkFox skill page](https://clawhub.ai/oomol/skills/oo-linkfox)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
