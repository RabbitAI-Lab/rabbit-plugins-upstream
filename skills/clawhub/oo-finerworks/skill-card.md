## Description:

Provides read-oriented FinerWorks actions for retrieving pricing and catalog information through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve FinerWorks price breakdowns and catalog options such as media, product, style, sizing, and framing information through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that may be run directly in a shell.

Mitigation: If the oo CLI is already installed and connected, use normal read actions only; if installation is needed, prefer official installer documentation, inspect the installer, and verify integrity before running shell commands.

Risk: Authentication or connection failures can require account setup, provider connection, or billing remediation before the skill works.

Mitigation: Run setup, connection, or billing steps only after the matching error appears, and rely on OOMOL server-side credential injection rather than handling raw tokens.

## Reference(s):

- [ClawHub FinerWorks Skill Page](https://clawhub.ai/oomol/skills/oo-finerworks)
- [FinerWorks Homepage](https://finerworks.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented FinerWorks actions; inspect live action schemas before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
