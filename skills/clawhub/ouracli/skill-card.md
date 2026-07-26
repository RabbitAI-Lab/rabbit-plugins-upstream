## Description: <br>
Access Oura Ring health data using the ouracli CLI tool. Use when user asks about "oura data", "sleep stats", "activity data", "heart rate", "readiness score", "stress levels", or wants health metrics from their Oura Ring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visionik](https://clawhub.ai/user/visionik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to retrieve and analyze their Oura Ring health metrics through the ouracli command-line interface. It supports activity, sleep, readiness, heart rate, SpO2, stress, workout, session, tag, rest-mode, personal-info, and combined data queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retrieve sensitive Oura health and profile data, especially when broad date ranges or the all command are used. <br>
Mitigation: Use narrow commands and date ranges, avoid the all command unless full retrieval is intended, and treat JSON or HTML reports as sensitive health records. <br>
Risk: The PERSONAL_ACCESS_TOKEN grants access to the user's Oura account data if exposed. <br>
Mitigation: Keep the token out of prompts, logs, source control, and generated reports; store it only in the documented secrets location. <br>


## Reference(s): <br>
- [Oura Ring Data ClawHub Page](https://clawhub.ai/visionik/skills/ouracli) <br>
- [Oura Personal Access Tokens](https://cloud.ouraring.com/personal-access-tokens) <br>
- [Oura API v2](https://api.ouraring.com/v2) <br>
- [dashdash Specification](https://github.com/visionik/dashdash) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, JSON, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI outputs in JSON, Markdown, HTML, dataframe, and tree formats] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a PERSONAL_ACCESS_TOKEN for Oura API access; JSON is recommended for agent analysis.] <br>

## Skill Version(s): <br>
0.1.0 (source: pyproject.toml, CHANGELOG, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
