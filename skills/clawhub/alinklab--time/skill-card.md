## Description: <br>
Provides current-time lookup and time conversion between IANA time zones through a third-party time protocol service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve the current time for a specific IANA time zone or convert a 24-hour time between source and target IANA time zones. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may contact a third-party service and handle an API key despite being presented as a time and timezone tool. <br>
Mitigation: Install only after reviewing the third-party API behavior and avoid providing sensitive or reusable credentials. <br>
Risk: The artifact persists the API key in a local .env file. <br>
Mitigation: Review or remove local secret persistence before use and rotate any credential that may have been exposed. <br>
Risk: The server security verdict is suspicious because the advertised time functionality includes generic remote-call and credential collection behavior. <br>
Mitigation: Review and scan the skill before deployment, and restrict network access to approved endpoints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alinklab/skills/time) <br>
- [XiaoBenYang API Key Site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API Endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance, Text] <br>
**Output Format:** [Markdown or plain text summarizing JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and calls a third-party API for time and timezone operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
