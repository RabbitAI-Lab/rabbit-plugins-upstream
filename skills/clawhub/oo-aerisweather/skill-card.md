## Description:

Xweather lets an agent search and read Xweather weather data through an OOMOL-connected AerisWeather connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Xweather forecasts, current observations, and place resolution through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute scripts from the network.

Mitigation: Verify the oo CLI through OOMOL's official documentation, avoid piping remote scripts directly into a shell, and do not run installers from an elevated session unless independently confirmed necessary.

Risk: The connector depends on an authenticated OOMOL account and an active Xweather connection.

Mitigation: Run setup or reconnect steps only after an action fails with an authentication, connection, scope, credential, app, or billing error.

## Reference(s):

- [Xweather homepage](https://www.xweather.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aerisweather)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only weather data actions for forecast, observation, and place resolution.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
