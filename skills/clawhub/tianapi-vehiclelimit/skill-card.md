## Description: <br>
Queries vehicle restriction information for cities across China, including plate-number limits, restricted areas, active times, and penalty standards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to answer city vehicle-limit queries in China by passing a city name or city code to TianAPI and presenting the returned restriction rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The TianAPI key can be exposed if passed directly on the command line or stored carelessly. <br>
Mitigation: Prefer TIANAPI_VEHICLELIMIT_KEY as an environment variable, avoid command-line key arguments, and protect any .env file. <br>
Risk: Each lookup sends the API key plus city or city code to TianAPI. <br>
Mitigation: Use the skill only when sharing that query data with TianAPI is acceptable. <br>
Risk: Vehicle-restriction data may be unavailable, stale, or incomplete for a requested city. <br>
Mitigation: Check returned error codes and verify current local rules before relying on results for consequential travel or compliance decisions. <br>


## Reference(s): <br>
- [TianAPI Vehicle Limit API Documentation](https://www.tianapi.com/apiview/246) <br>
- [TianAPI Vehicle Limit API Endpoint](https://apis.tianapi.com/vehiclelimit/index) <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-vehiclelimit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_VEHICLELIMIT_KEY; queries use either a city name or city code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
