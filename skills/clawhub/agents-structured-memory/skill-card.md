## Description: <br>
Qordinate gives OpenClaw agents a chat-native way to store long-term facts, tasks, lists, and reminders through WhatsApp, Telegram, or Slack. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[singhcoder](https://clawhub.ai/user/singhcoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill when an OpenClaw agent needs durable external memory for tasks, contacts, leads, resources, facts, and reminders without maintaining its own database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected agent memory may be sent to Qordinate through WhatsApp, Telegram, or Slack and persist outside the local agent environment. <br>
Mitigation: Define what the agent may save and avoid secrets, credentials, regulated data, confidential client material, or anything that should not persist externally. <br>
Risk: The skill depends on the user connecting a Qordinate account to a supported messaging platform before the agent can use it reliably. <br>
Mitigation: Confirm the user has completed Qordinate account and channel setup before storing or retrieving long-term memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/singhcoder/skills/agents-structured-memory) <br>
- [Qordinate](https://qordinate.ai) <br>
- [Qordinate WhatsApp setup](https://qordinate.ai/whatsapp) <br>
- [Qordinate Telegram setup](https://qordinate.ai/telegram) <br>
- [Qordinate Slack setup](https://qordinate.ai/slack) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Configuration] <br>
**Output Format:** [Markdown guidance with plain-language message examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only skill; it does not produce code or shell commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
