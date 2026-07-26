## Description: <br>
Access user-consented Fulcra context data including biometrics, sleep, activity, calendar, location, and the Fulcra metric catalog through the hosted MCP server or Fulcra CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to connect private Fulcra sessions to user-consented biometrics, sleep, activity, calendar, location, file, and metric catalog context. It is for bounded read-side context workflows; write workflows should use companion skills such as fulcra-annotations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward sensitive personal Fulcra data, including health, calendar, location, and file context. <br>
Mitigation: Keep use in private sessions, ask before reads, and limit each request to the smallest relevant metric set and time window. <br>
Risk: OAuth/session tokens or credential files could expose private Fulcra data if logged, pasted, or published. <br>
Mitigation: Protect tokens and credential files, share only user-facing device-flow login details, and never publish raw secrets or auth material. <br>
Risk: Calendar, location, health, or file records could be exposed through public examples, reports, screenshots, or shared chats. <br>
Mitigation: Use synthetic data for public artifacts unless the user explicitly approves the exact real data disclosure and destination. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arc-claw-bot/skills/fulcra-context) <br>
- [Fulcra Platform](https://fulcradynamics.com) <br>
- [Fulcra Developer Docs](https://docs.fulcradynamics.com) <br>
- [Fulcra OpenAPI](https://api.fulcradynamics.com/openapi.json) <br>
- [Hosted Fulcra MCP endpoint](https://mcp.fulcradynamics.com/mcp) <br>
- [Fulcra Python Client](https://github.com/fulcradynamics/fulcra-api-python) <br>
- [Fulcra Context MCP Server](https://github.com/fulcradynamics/fulcra-context-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-focused guidance; no executable helper scripts are included in the ClawHub package.] <br>

## Skill Version(s): <br>
1.4.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
