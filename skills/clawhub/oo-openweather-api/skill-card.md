## Description:

OpenWeather helps agents handle OpenWeather requests, including reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate OpenWeather through the OOMOL openweather_api connector, including weather, forecast, air-pollution, geocoding, map tile, UV index, and station workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that first-time setup directs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path and prefer a trusted, versioned, verifiable package or inspect and verify the installer before running it.

Risk: The skill can perform write and destructive OpenWeather station actions.

Mitigation: Confirm the exact payload, target, and effect with the user before running actions tagged write or destructive.

## Reference(s):

- [OpenWeather homepage](https://openweathermap.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OpenWeather icon](https://static.oomol.com/logo/third-party/OpenWeather%20API.svg)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openweather-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may return JSON data and metadata from the oo connector run command.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
