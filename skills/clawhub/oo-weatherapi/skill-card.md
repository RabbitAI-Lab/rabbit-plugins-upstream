## Description:

WeatherAPI lets agents query WeatherAPI data through an OOMOL-connected oo CLI connector for weather, forecast, astronomy, timezone, and location search requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current weather, forecasts, astronomy data, timezone information, and WeatherAPI-supported location search results through an OOMOL-managed connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute scripts from OOMOL delivery URLs.

Mitigation: Review installer delivery before use; prefer official installation documentation, package-manager installation, or a downloaded installer with version and integrity verification.

Risk: WeatherAPI actions depend on a connected OOMOL account, valid WeatherAPI credentials, and available billing credit.

Mitigation: Run operational actions only after the oo CLI, authentication, connection status, and billing state are confirmed or after a command returns a matching setup error.

## Reference(s):

- [WeatherAPI homepage](https://www.weatherapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [WeatherAPI skill on ClawHub](https://clawhub.ai/oomol/skills/oo-weatherapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns WeatherAPI data from OOMOL-managed connector calls.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
