## Description:

Helps agents retrieve astronomical and astrology calculations through a connected FreeAstroAPI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can ask an agent to look up celestial events, calculate astrology charts and calendars, or find city coordinates and timezones through FreeAstroAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can share birth, location, date, or name data through OOMOL with FreeAstroAPI.

Mitigation: Share only information needed for the requested calculation and use the connector only if comfortable with OOMOL as an intermediary.

Risk: The optional CLI setup includes a pipe-to-shell installer and account connection steps.

Mitigation: Review the installer or official install guide before use, and start login or connection setup only after an authentication or connection error.

## Reference(s):

- [FreeAstroAPI skill on ClawHub](https://clawhub.ai/oomol/skills/oo-freeastroapi)
- [FreeAstroAPI homepage](https://www.freeastroapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with command examples and summarized calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector results depend on the requested action and connected account plan.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
