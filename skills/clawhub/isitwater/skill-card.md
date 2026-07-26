## Description: <br>
Check if geographic coordinates are over water or land using the IsItWater API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johnnagro](https://clawhub.ai/user/johnnagro) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users can use this skill to have an agent check whether latitude and longitude coordinates are over water or land, inspect returned geographic features, and check IsItWater account balance before larger lookup batches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an IsItWater API key for API calls. <br>
Mitigation: Prefer the ISITWATER_API_KEY environment variable, keep any OpenClaw config file private, and avoid sharing logs or snippets that contain the key. <br>
Risk: Water lookup requests consume IsItWater credits. <br>
Mitigation: Use the account-info endpoint to check balance before large batches and confirm that lookups should proceed. <br>
Risk: Place-name requests require geocoding before the IsItWater API can be called. <br>
Mitigation: Resolve place names to latitude and longitude first, then review the coordinates before making paid lookup requests. <br>


## Reference(s): <br>
- [IsItWater](https://isitwater.com) <br>
- [IsItWater ClawHub page](https://clawhub.ai/johnnagro/skills/isitwater) <br>
- [AgentSkills Spec](https://agentskills.io) <br>
- [OpenClaw Skills Docs](https://docs.openclaw.ai/tools/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an IsItWater API key and may include guidance for environment-variable or OpenClaw configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
