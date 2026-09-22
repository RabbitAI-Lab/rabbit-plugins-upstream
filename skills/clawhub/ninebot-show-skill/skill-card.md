## Description:

Read-only Ninebot/九号 electric vehicle status and reporting skill for querying vehicle state, rides, location, and optional visualizations through a locally authenticated ninecli session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzzhe2333](https://clawhub.ai/user/zzzhe2333)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Ninebot/九号 vehicle battery, range, charging, smart-service, ride, and location data from a local ninecli session. It is intended for read-only status checks, daily reports, and optional static map or ride-track outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can delete and replace an existing ninebot-show-skill target directory without prompting.

Mitigation: Review the install target and OPENCLAW_WORKSPACE value before installation, and back up or remove any existing directory intentionally.

Risk: Runtime commands can process sensitive vehicle location data, including exact address, coordinates, maps, and ride trails.

Mitigation: Use privacy=off when location processing is not needed, and request exact, coordinate, map, or trail outputs only when location sharing is acceptable.

Risk: Optional location, map, and weather features may share location-related data with AMap, OpenStreetMap tile providers, or wttr.in.

Mitigation: Avoid exact address, coordinate, map, trail, or weather commands when third-party location disclosure is not acceptable.

Risk: Ninebot account credentials, SMS codes, cookies, tokens, or BLE secrets are sensitive and should not be exposed to an agent chat.

Mitigation: Keep Ninebot authentication local through ninecli and do not paste credential material into chat or public skill files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzzhe2333/skills/ninebot-show-skill)
- [Publisher profile](https://clawhub.ai/user/zzzhe2333)
- [Configuration guide](references/configuration.md)
- [Network privacy guide](references/network-privacy.md)
- [Safe example data](references/example-data.md)
- [Privacy and publishing checklist](PRIVACY.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON report options, and generated image files for maps or ride tracks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May process sensitive vehicle location data locally and can optionally generate static map or ride visualization files.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
