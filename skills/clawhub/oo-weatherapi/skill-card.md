## Description:

WeatherAPI (weatherapi.com) connector skill for searching locations and reading current weather, forecasts, astronomy, and timezone data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve WeatherAPI data through an OOMOL-connected account, including current conditions, forecasts, astronomy, timezone details, and location search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes mutable remote shell installer commands without integrity verification.

Mitigation: Install the oo CLI only from official signed packages or documented package-manager instructions where possible, verify installer source and integrity, and avoid running curl-to-shell or PowerShell iex commands from an elevated shell.

Risk: WeatherAPI access depends on OOMOL mediating the connection and credentials.

Mitigation: Use the connector only when OOMOL-mediated credential handling is acceptable for the deployment environment.

## Reference(s):

- [ClawHub WeatherAPI Skill](https://clawhub.ai/oomol/skills/oo-weatherapi)
- [WeatherAPI Homepage](https://www.weatherapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live WeatherAPI connector schemas before building request payloads; WeatherAPI credentials are mediated through OOMOL.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
