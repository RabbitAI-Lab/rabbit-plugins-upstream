## Description: <br>
Get Croatian weather data, forecasts, and alerts from DHMZ (meteo.hr) - no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[faleksic](https://clawhub.ai/user/faleksic) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for Croatian current weather, forecasts, alerts, sea conditions, agricultural data, and hydrological data from public DHMZ-related XML feeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent makes live requests to public Croatian weather sites, so results depend on network availability and the current content of those public feeds. <br>
Mitigation: Use the skill when live public weather data is acceptable, provide a city explicitly when precision matters, and review the returned weather data before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/faleksic/skills/dhmz-weather) <br>
- [DHMZ XML data for users](https://meteo.hr/proizvodi.php?section=podaci&param=xml_korisnici) <br>
- [DHMZ official site](https://meteo.hr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized weather data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; fetches public XML data from DHMZ-related Croatian weather sites; source data is in Croatian.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
