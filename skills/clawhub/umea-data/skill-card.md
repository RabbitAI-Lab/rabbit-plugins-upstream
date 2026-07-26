## Description: <br>
Query public Umeå kommun open data about locations, facilities, demographics, environment, infrastructure, and building permits with geospatial support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simskii](https://clawhub.ai/user/simskii) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer natural-language or scripted lookup questions against public Umeå municipal datasets, including playgrounds, EV charging stations, beaches, trails, WiFi, building permits, demographics, and environmental data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls a public municipal API and depends on local curl and jq availability. <br>
Mitigation: Confirm network access to the Umeå Open Data API and verify curl and jq are installed before relying on local scripts. <br>
Risk: The nearest-location command may fail because scripts/nearby.sh references a missing distance.jq helper. <br>
Mitigation: Avoid the nearest-location workflow until distance.jq is supplied or the package is fixed; use direct dataset queries as a fallback. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/simskii/skills/umea-data) <br>
- [Umeå Open Data API](https://opendata.umea.se/api/v2/) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries use public API calls and may depend on curl and jq for local script execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
