## Description:

Connects an agent to Xingpan API to calculate astrology charts, retrieve chart configuration, and read daily horoscopes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can ask an agent to calculate natal, relationship, transit, and return charts or retrieve Xingpan configuration and daily horoscopes through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup suggests running a remote oo CLI installer without integrity checks or explicit approval.

Mitigation: Do not allow an agent to run the remote installer automatically; follow trusted official installation instructions with verification or explicitly approve the exact installation step.

## Reference(s):

- [Xingpan API](https://xingpan.vip/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Xingpan API skill on ClawHub](https://clawhub.ai/oomol/skills/oo-xingpan)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Natural-language answers or structured Xingpan API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Natal chart results may include SVG when requested.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
