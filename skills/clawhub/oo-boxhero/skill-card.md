## Description:

BoxHero helps an agent search and read BoxHero inventory data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve BoxHero inventory items, locations, and linked team information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute arbitrary local code.

Mitigation: Install the oo CLI only through a trusted, verified method and avoid letting an agent automatically run curl-to-bash or PowerShell installer commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-boxhero)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [BoxHero Homepage](https://www.boxhero-app.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented BoxHero actions include item lookup, team information, item listing with filters and pagination, and location listing.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
