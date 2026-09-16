## Description:

Missive (missiveapp.com) support for searching and reading Missive data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent retrieve Missive contacts, conversations, contact books, organizations, teams, and users through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review installer commands before execution and prefer a verified package, pinned release, checksum or signature verification, or manual review.

Risk: The skill enables agent access to Missive data through the user's connected OOMOL account.

Mitigation: Use the skill only when the user intends the agent to access Missive data, and rely on the listed read-oriented actions unless a future action is clearly confirmed.

## Reference(s):

- [ClawHub Missive skill page](https://clawhub.ai/oomol/skills/oo-missive)
- [Missive homepage](https://missiveapp.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema and run commands; connector results are JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
