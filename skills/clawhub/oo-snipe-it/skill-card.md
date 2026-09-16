## Description:

This skill supports Snipe-IT requests for searching and reading data through an OOMOL-connected account instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and retrieve Snipe-IT inventory data through an OOMOL-connected account. It supports read-oriented tasks such as getting the current user and listing categories, companies, hardware assets, status labels, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute unreviewed code.

Mitigation: Use a reviewed, signed, version-pinned oo CLI installation method and confirm setup commands before running them.

Risk: The skill depends on OOMOL as the Snipe-IT connector provider.

Mitigation: Install only when the user accepts OOMOL handling the connector flow and verify the Snipe-IT connection before use.

Risk: Using the connector beyond the listed read-only actions could affect Snipe-IT data.

Mitigation: Limit routine use to the documented get, list, and search actions; require explicit user confirmation for any action tagged write or destructive.

## Reference(s):

- [ClawHub Snipe-IT Skill Page](https://clawhub.ai/oomol/skills/oo-snipe-it)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Snipe-IT Homepage](https://snipeitapp.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; documented normal actions are read-only get, list, and search operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
