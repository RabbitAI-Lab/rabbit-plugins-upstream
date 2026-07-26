## Description: <br>
Control Home Assistant smart home devices using the Assist (Conversation) API by passing natural-language requests to Home Assistant's built-in NLU for fast, token-efficient control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[developmentcats](https://clawhub.ai/user/developmentcats) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this OpenClaw skill to control or query Home Assistant-connected smart devices with natural language. The agent sends the request to Home Assistant Assist, then relays the human-readable response or suggests Home Assistant configuration improvements for Assist errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent operate real Home Assistant devices, including safety-sensitive devices. <br>
Mitigation: Require manual confirmation for locks, doors, garage doors, alarms, covers, HVAC, appliances, and other safety-sensitive actions. <br>
Risk: A Home Assistant long-lived token could grant broad API access if exposed. <br>
Mitigation: Use a dedicated least-privilege Home Assistant account or token, and keep the token out of chats, logs, and source control. <br>
Risk: Unencrypted Home Assistant server connections could expose credentials or commands. <br>
Mitigation: Prefer HTTPS for HASS_SERVER. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/developmentcats/skills/homeassistant-assist) <br>
- [Home Assistant Conversation API Docs](https://developers.home-assistant.io/docs/intent_conversation_api/) <br>
- [Home Assistant Long-Lived Access Tokens](https://developers.home-assistant.io/docs/auth_api/#long-lived-access-token) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash commands, JSON configuration snippets, and natural-language response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl plus HASS_SERVER and HASS_TOKEN environment variables.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata and CHANGELOG, released 2026-02-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
