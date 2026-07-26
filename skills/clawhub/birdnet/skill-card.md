## Description: <br>
Query BirdNET-Go bird detections. View recent birds, search by species, get detection details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rappo](https://clawhub.ai/user/rappo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to query a BirdNET-Go instance for recent bird detections, species searches, detection details, species information, and daily activity summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests to a configured BirdNET-Go endpoint can expose species, timestamps, weather data, and query activity, especially over plain HTTP. <br>
Mitigation: Configure the URL to a trusted endpoint you control, and prefer localhost or HTTPS where available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rappo/skills/birdnet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Plain text summaries produced from BirdNET-Go API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq, reads the local BirdNET-Go URL from ~/.clawdbot/credentials/birdnet/config.json when present, and does not require an API key for local access.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
