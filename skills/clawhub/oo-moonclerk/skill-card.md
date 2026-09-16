## Description:

MoonClerk (moonclerk.com). Use this skill for ANY MoonClerk request: searching and reading data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve MoonClerk customers, payment forms, and payments through the OOMOL oo CLI after connecting their MoonClerk account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners for the oo CLI.

Mitigation: Use official, versioned, verifiable installation steps before running installer scripts.

Risk: The skill reads MoonClerk account data through OOMOL as an intermediary.

Mitigation: Connect MoonClerk only when the user intends the agent to read that account data and scopes are appropriate.

## Reference(s):

- [MoonClerk Skill Page](https://clawhub.ai/oomol/skills/oo-moonclerk)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [MoonClerk Homepage](https://moonclerk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MoonClerk connector actions return data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
