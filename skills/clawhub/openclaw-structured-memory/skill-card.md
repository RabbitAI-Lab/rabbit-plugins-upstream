## Description: <br>
Qordinate gives an OpenClaw agent durable structured memory for documents, contacts, tasks, reminders, web search, and connected apps through an MCP server authenticated with an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[singhcoder](https://clawhub.ai/user/singhcoder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to connect an agent to Qordinate for persistent tasks, contacts, documents, reminders, web search, and app-connected workflows. It is most useful when agent state needs to survive across sessions and be shared with the user's Qordinate account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad ongoing authority over private Qordinate data, connected apps, documents, automations, and reminders. <br>
Mitigation: Use a dedicated or expiring Qordinate API key, connect only necessary apps, and require explicit user confirmation before deletes, overwrites, sharing, automations, reminders, or third-party app actions. <br>
Risk: Long-lived access can persist after the original task is complete. <br>
Mitigation: Periodically review active automations, shared documents, stored data, connected apps, and API key validity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/singhcoder/skills/openclaw-structured-memory) <br>
- [Qordinate MCP server endpoint](https://api.qordinate.ai/mcp) <br>
- [Qordinate app](https://app.qordinate.ai) <br>
- [Qordinate WhatsApp channel](https://qordinate.ai/whatsapp) <br>
- [Qordinate Telegram channel](https://qordinate.ai/telegram) <br>
- [Qordinate Slack channel](https://qordinate.ai/slack) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, text, markdown] <br>
**Output Format:** [Markdown guidance with MCP configuration details and natural-language query examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MCP client support, curl, and QORDINATE_API_KEY. The MCP tool accepts a query string and optional session_id.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
