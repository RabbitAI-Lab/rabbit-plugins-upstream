## Description:

Product Fruits helps agents search and read Product Fruits knowledge-base articles and categories through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list Product Fruits knowledge-base articles and categories and retrieve localized category or article content without handling raw Product Fruits tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that can execute unreviewed code on the user's machine.

Mitigation: Prefer a documented, versioned oo CLI installer with integrity checks, and confirm any install or authentication step before an agent performs it.

Risk: Use depends on OOMOL and Product Fruits access through the oo CLI.

Mitigation: Install only when comfortable with OOMOL and Product Fruits account access through the connector, and confirm connection or scope changes before use.

## Reference(s):

- [ClawHub Product Fruits Skill](https://clawhub.ai/oomol/skills/oo-product-fruits)
- [Product Fruits Homepage](https://productfruits.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, HTML, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses; article content may be returned as Markdown or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Product Fruits connector actions through the oo CLI; setup and authentication steps may require user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
