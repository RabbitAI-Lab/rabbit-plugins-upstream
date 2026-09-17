## Description:

ShipEngine (shipengine.com). Use this skill for ANY ShipEngine request: searching and reading data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ShipEngine through an OOMOL-connected account. It supports calculating and estimating shipping rates, retrieving rates, listing connected carriers, parsing addresses, and validating mailing addresses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly.

Mitigation: Review the installer path before installation and prefer a pinned, verified release or trusted package manager.

Risk: Using the connector requires OOMOL-mediated access to ShipEngine account data and may consume billing credits.

Mitigation: Connect ShipEngine only after confirming the account, scopes, and billing impact are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shipengine)
- [ShipEngine Homepage](https://www.shipengine.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
