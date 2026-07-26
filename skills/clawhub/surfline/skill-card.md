## Description: <br>
Get surf forecasts and current conditions from Surfline public endpoints with no login; use it to look up Surfline spot IDs, fetch spot forecasts and conditions, and summarize favorite spots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[miguelcarranza](https://clawhub.ai/user/miguelcarranza) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to find Surfline spot IDs, retrieve concise surf condition reports, and summarize configured favorite surf spots from public Surfline data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and spot IDs are sent to Surfline public services. <br>
Mitigation: Use only location queries and spot IDs that are appropriate to share with Surfline. <br>
Risk: Cached forecast data and favorites configuration may remain on the local machine. <br>
Mitigation: Delete local Surfline cache and configuration files when no longer needed, or set a dedicated cache directory for easier cleanup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/miguelcarranza/skills/surfline) <br>
- [Surfline public services endpoint](https://services.surfline.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Plain text summaries and JSON forecast payloads, with shell command examples for running the scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public Surfline endpoints and basic local caching; no login or API key is required.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
