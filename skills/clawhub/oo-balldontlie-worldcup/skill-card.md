## Description:

BALLDONTLIE World Cup helps an agent search and read FIFA World Cup data from fifa.balldontlie.io through the OOMOL balldontlie_worldcup connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve FIFA World Cup matches, teams, standings, rosters, player information, statistics, injuries, stadiums, and betting market data through an OOMOL-connected BALLDONTLIE account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions can lead users to execute remote installer scripts without local review.

Mitigation: Install the oo CLI only from a verified OOMOL channel, avoid elevated shells for remote installers, and review, pin, or verify installer contents before execution.

Risk: Connector use depends on an authenticated OOMOL account and connected BALLDONTLIE World Cup credential.

Mitigation: Run connector actions only after the user has installed the CLI, signed in, and connected the service, and use first-time setup steps only after a matching command failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-balldontlie-worldcup)
- [BALLDONTLIE World Cup homepage](https://fifa.balldontlie.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides schema inspection and read-oriented connector calls; returned data is provided by the OOMOL balldontlie_worldcup connector.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
