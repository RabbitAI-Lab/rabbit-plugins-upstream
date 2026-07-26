## Description: <br>
Conversational interface for AIDA to get building status, control devices, optimize objectives, and run diagnostics through authenticated REST APIs. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ak-khalis](https://clawhub.ai/user/ak-khalis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and demo operators use this skill to connect OpenClaw-style conversational intents to AIDA smart-building status, control, optimization, and diagnostic workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated control and optimization intents can affect live smart-building operations. <br>
Mitigation: Use trusted AIDA endpoints, least-privilege API tokens, and human approval before control or optimization actions. <br>
Risk: Fallback replies may appear successful when an API call fails. <br>
Mitigation: Verify action results against AIDA telemetry or API status before treating a reply as completed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ak-khalis/skills/aida) <br>


## Skill Output: <br>
**Output Type(s):** [Text] <br>
**Output Format:** [Text response returned in a reply field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return fallback status text if the AIDA API call fails.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
