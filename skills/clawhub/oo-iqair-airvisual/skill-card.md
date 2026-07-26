## Description: <br>
IQAir AirVisual helps an agent retrieve current air-quality and weather data, nearest supported city data, and supported location lists through an OOMOL-connected IQAir AirVisual account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer IQAir AirVisual requests without calling the API directly, including current city conditions, nearest-city conditions by IP or coordinates, and supported country, state, and city discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IQAir AirVisual queries run through OOMOL as an intermediary and require an IQAir API key connected to the user's OOMOL account. <br>
Mitigation: Install and use the skill only when that account connection and intermediary access are acceptable for the deployment. <br>
Risk: Nearest-city lookups can involve location or IP-derived context. <br>
Mitigation: Use city-specific lookups when possible, and avoid nearest-city requests when location disclosure is not appropriate. <br>
Risk: First-time setup may require installing the oo CLI with a remote installer. <br>
Mitigation: Review the oo CLI installer before running it if the CLI is not already installed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-iqair-airvisual) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [IQAir AirVisual homepage](https://www.iqair.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; actions in this release are read-only air-quality, weather, and supported-location lookups.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version and metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
