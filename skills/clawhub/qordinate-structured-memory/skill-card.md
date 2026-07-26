## Description: <br>
Qordinate lets OpenClaw agents use WhatsApp, Telegram, or Slack to store and retrieve durable lists, facts, tasks, and reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[singhcoder](https://clawhub.ai/user/singhcoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when an OpenClaw agent needs durable external memory for user facts, lists, tasks, contacts, resources, and reminders through Qordinate chat integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may persist user information to an external Qordinate account through chat apps without enough consent, privacy, or deletion guidance. <br>
Mitigation: Require user confirmation before storing sensitive memory, avoid secrets, OTPs, credentials, financial, health, legal, and confidential business data, and verify Qordinate's retention and deletion controls before use. <br>
Risk: The skill depends on a linked Qordinate account and external WhatsApp, Telegram, or Slack access. <br>
Mitigation: Use the skill only after the user has completed Qordinate setup and confirmed the channel the agent is allowed to message. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/singhcoder/skills/qordinate-structured-memory) <br>
- [Publisher profile](https://clawhub.ai/user/singhcoder) <br>
- [Qordinate](https://qordinate.ai) <br>
- [Qordinate Slack connection](https://qordinate.ai/slack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with natural-language message examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces chat-message phrasing for agents to create, update, and query Qordinate lists.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
