## Description: <br>
Interact with the Maestro API to create tasks, list tasks, and send room messages using the configured OpenClaw Maestro connection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohammadsheikhian](https://clawhub.ai/user/mohammadsheikhian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to operate a configured Maestro account from an agent by creating tasks, listing tasks, and sending room messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task descriptions and room messages are sent to the configured Maestro API. <br>
Mitigation: Use the skill only with authorized Maestro accounts and avoid sending secrets or sensitive data unless that is intended and authorized. <br>
Risk: Incorrect or exposed Maestro configuration could leak credentials or send requests to the wrong workspace. <br>
Mitigation: Read credentials only from channels.omadeus, validate baseUrl, apiKey, and openClawMemberId before requests, and never print or hardcode these values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohammadsheikhian/skills/omadeus) <br>
- [Publisher profile](https://clawhub.ai/user/mohammadsheikhian) <br>


## Skill Output: <br>
**Output Type(s):** [API calls, text, guidance] <br>
**Output Format:** [Concise Markdown or plain text summaries of Maestro API operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns readable results and summarized errors; does not dump raw JSON or expose configured secrets.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
