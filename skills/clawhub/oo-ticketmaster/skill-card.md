## Description:

Operates Ticketmaster through an OOMOL-connected account to read, create, and update Ticketmaster data with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and retrieve Ticketmaster events, venues, attractions, classifications, images, and suggestions, and to run authorized Ticketmaster season-ticketing actions after reviewing the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes one-time remote shell installation commands for the oo CLI.

Mitigation: Verify installer URLs through OOMOL's official documentation before running installation commands.

Risk: The skill can execute write-capable Ticketmaster season-ticketing commands.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect with the user before running any write action.

Risk: Ticketmaster actions are mediated through OOMOL-connected credentials.

Mitigation: Install and use the skill only when OOMOL is an acceptable intermediary for the intended Ticketmaster account activity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ticketmaster)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Ticketmaster](https://www.ticketmaster.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions and returns connector responses as JSON when actions are executed.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
