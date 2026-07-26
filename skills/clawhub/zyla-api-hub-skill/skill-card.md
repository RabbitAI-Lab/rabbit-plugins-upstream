## Description: <br>
Zyla API Hub Skill \u2014 Turn your OpenClaw AI agent into a real-world operator with access to Zyla API Hub APIs for weather, finance, translation, email validation, geolocation, and related tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alebrega](https://clawhub.ai/user/alebrega) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to discover Zyla API Hub services, configure a Zyla API key, and have an OpenClaw agent call selected APIs for common data and automation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent make broad Zyla API calls that may incur usage-based costs. <br>
Mitigation: Use a dedicated or restricted Zyla API key, monitor billing and usage, and require explicit approval for paid or mutating API calls. <br>
Risk: Requests may send user-provided data to Zyla or downstream API providers. <br>
Mitigation: Avoid sensitive inputs unless the API call requires them and the user has approved that data sharing. <br>
Risk: The Zyla API key may be exposed through chat-visible configuration text, logs, or screenshots. <br>
Mitigation: Configure the key through environment or config storage, do not paste raw keys in chat, avoid sharing logs or screenshots containing keys, and rotate the key if exposed. <br>


## Reference(s): <br>
- [Zyla API Hub OpenClaw Connect](https://zylalabs.com/openclaw/connect) <br>
- [Zyla API Hub](https://zylalabs.com) <br>
- [ClawHub skill page](https://clawhub.ai/alebrega/skills/zyla-api-hub-skill) <br>
- [Publisher profile](https://clawhub.ai/user/alebrega) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance, shell commands, configuration snippets, and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Zyla API response data, rate-limit headers, usage status, and billing-related usage signals returned by Zyla endpoints.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
