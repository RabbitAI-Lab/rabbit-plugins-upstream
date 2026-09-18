## Description:

OpenWeather helps agents retrieve weather, forecast, air-pollution, geocoding, UV index, map-tile, and weather-station data through an OOMOL-connected OpenWeather account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to answer OpenWeather requests and run OpenWeather connector actions for current conditions, forecasts, geocoding, pollution, UV index, map tiles, and station management. State-changing actions require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path asks users to run remote shell or PowerShell installer pipelines.

Mitigation: Review the installer before use and prefer a verified, signed, or package-manager installation method for the oo CLI.

Risk: Write and destructive OpenWeather actions can modify or delete account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub OpenWeather skill page](https://clawhub.ai/oomol/skills/oo-openweather-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OpenWeather homepage](https://openweathermap.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata; map-tile responses may include Base64 PNG bytes.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
