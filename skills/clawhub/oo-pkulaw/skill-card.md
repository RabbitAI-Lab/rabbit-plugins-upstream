## Description:

PKULaw (mcp.pkulaw.com) helps agents search and read PKULaw legal data through the OOMOL PKULaw connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and legal research agents use this skill to discover PKULaw tools, search laws, regulations, provisions, and judicial cases, and retrieve authoritative law article text. The skill is intended for schema-first use through the oo CLI after the user has connected PKULaw in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer pipelines that execute downloaded scripts.

Mitigation: Review the setup path before installing, and prefer pinned, signed, or independently verified distributions before running installer commands.

Risk: Live connector tools may expose actions whose effects depend on the current PKULaw service schema.

Mitigation: Inspect the live action schema before building payloads, confirm user intent for write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pkulaw)
- [PKULaw Homepage](https://mcp.pkulaw.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, connector actions return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
