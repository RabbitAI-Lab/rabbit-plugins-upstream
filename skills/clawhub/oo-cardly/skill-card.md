## Description:

Cardly (card.ly). Use this skill for ANY Cardly request - searching and reading data. Whenever a task involves Cardly, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access Cardly through an OOMOL-connected account, including balance lookup, credit history listing, and discovery of fonts, media, and writing styles. It also supports authenticated echo debugging through the Cardly connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly in a shell, creating a supply-chain review risk.

Mitigation: Review the setup path before installation and prefer verified official release or package-manager instructions for the oo CLI.

Risk: Connector actions depend on the user's OOMOL account connection and Cardly authorization state.

Mitigation: Run authentication or connection setup only after an action fails with a matching auth, scope, expiration, or app readiness error.

## Reference(s):

- [ClawHub Cardly skill page](https://clawhub.ai/oomol/skills/oo-cardly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cardly homepage](https://www.card.ly)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
