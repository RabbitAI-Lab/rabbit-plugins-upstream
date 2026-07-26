## Description: <br>
Provides chess FEN validation and ASCII board visualization for MCP-compatible assistants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and MCP-compatible assistant users use this skill to submit a chess FEN string and receive an ASCII board visualization or API response that can be summarized for the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an external API key and persists it to a local .env file. <br>
Mitigation: Use it only in environments where storing the XBY_APIKEY locally is acceptable, and rotate or remove the key when access is no longer needed. <br>
Risk: FEN requests are routed through a third-party service rather than processed locally. <br>
Mitigation: Use this skill only if xiaobenyang.com is trusted for the submitted chess positions; use a local-only FEN renderer when remote processing is unnecessary. <br>
Risk: The security summary flags a mismatch between the claimed chess use case and the third-party API wrapper. <br>
Mitigation: Review the skill behavior and upstream service before deployment, especially in shared or production assistant environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/xby-chess) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration] <br>
**Output Format:** [Text summary of JSON returned by the external API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential before use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
