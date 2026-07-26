## Description: <br>
AccuWeather lets agents search AccuWeather locations and retrieve current conditions, daily forecasts, and hourly forecasts through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to look up AccuWeather locations and retrieve current, daily, or hourly weather data through the oo CLI after their AccuWeather connection is configured in OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL's oo CLI and an OOMOL-managed AccuWeather connection, which may require installing the CLI and persisting an OOMOL login. <br>
Mitigation: Install and connect only in environments where OOMOL account access is acceptable, and run authentication or connection setup only when a command reports an auth or connection error. <br>
Risk: Weather lookups can return incorrect results if an action is called with an outdated schema or the wrong AccuWeather location key. <br>
Mitigation: Inspect the live connector schema before each action and resolve or confirm the intended location key before requesting conditions or forecasts. <br>


## Reference(s): <br>
- [ClawHub AccuWeather Skill](https://clawhub.ai/oomol/skills/oo-accuweather) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [AccuWeather](https://www.accuweather.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output from the oo CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before running AccuWeather actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
