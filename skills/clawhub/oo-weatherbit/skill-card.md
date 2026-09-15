## Description:

Weatherbit (weatherbit.io). Use this skill for any Weatherbit request, including searching and reading weather data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current Weatherbit observations and daily or hourly forecasts through the OOMOL oo CLI after their Weatherbit connection is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions can execute remote installer scripts for the OOMOL oo CLI.

Mitigation: Review OOMOL's official installation documentation first, prefer a signed or package-managed installation path when available, and avoid running remote installer scripts automatically or with elevated privileges.

Risk: Weatherbit actions depend on an installed, authenticated OOMOL oo CLI and a connected Weatherbit account.

Mitigation: Run normal Weatherbit query actions only after the CLI is trusted, installed, signed in, and connected; use setup steps only after a matching authentication or connection failure.

## Reference(s):

- [Weatherbit homepage](https://www.weatherbit.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-weatherbit)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Weatherbit action schemas before execution and returns Weatherbit connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
