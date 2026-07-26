## Description: <br>
Monitor solar weather conditions including geomagnetic storms, solar flares, aurora forecasts, and solar wind data using NOAA Space Weather Prediction Center real-time data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and operators use this skill to check current space-weather conditions, forecasts, aurora outlooks, solar-wind readings, and NOAA SWPC alerts from the command line or through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included Python script contacts NOAA's public SWPC service for live space-weather data. <br>
Mitigation: Install and run the skill only in environments where outbound access to NOAA SWPC public endpoints is acceptable. <br>
Risk: Live space-weather readings and forecasts may change as NOAA updates source data. <br>
Mitigation: Treat generated conditions and forecasts as current-at-query-time operational guidance and re-check NOAA data before time-sensitive decisions. <br>


## Reference(s): <br>
- [Solar Weather Monitor Skill Page](https://clawhub.ai/capt-marbles/skills/solar-weather) <br>
- [NOAA Space Weather Prediction Center](https://www.swpc.noaa.gov/) <br>
- [NOAA SWPC Services API](https://services.swpc.noaa.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Terminal text or JSON, with Markdown usage examples in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command output depends on live NOAA SWPC API responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
