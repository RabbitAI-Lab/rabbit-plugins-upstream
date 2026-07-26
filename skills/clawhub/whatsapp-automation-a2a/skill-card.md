## Description: <br>
Automate WhatsApp outreach workflows with AI lead mining, bulk and scheduled messaging, channel broadcasts, review collection, CRM pipeline tracking, and integrations for MCP and Custom GPT actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alex-tradequo](https://clawhub.ai/user/alex-tradequo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External business users, marketers, sales teams, agencies, and developers use this skill to manage WhatsApp outreach, leads, reviews, automation schedules, and AI assistant integrations. It is intended for authenticated workflows where the user is authorized to message, monitor, export, or process the relevant WhatsApp contacts and business data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live outreach automation can send bulk, scheduled, or AI-generated WhatsApp messages to unintended recipients. <br>
Mitigation: Use approval mode and phone whitelisting, and preview recipients and message text before bulk or scheduled sends. <br>
Risk: Contact extraction, group monitoring, exports, and admin operations can expose WhatsApp business data. <br>
Mitigation: Install only when the publisher is trusted with live WhatsApp business data, use a dedicated least-privilege key, and avoid importing or exporting group members without consent. <br>
Risk: Schedules, webhooks, A2A endpoints, API keys, AI profiles, document indexes, and review collectors can continue operating after initial setup. <br>
Mitigation: Regularly audit these resources and revoke, disable, or rotate anything no longer needed. <br>


## Reference(s): <br>
- [MoltFlow Homepage](https://molt.waiflow.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/alex-tradequo/skills/whatsapp-automation-a2a) <br>
- [AI Agent Integrations](integrations.md) <br>
- [MoltFlow MCP Endpoint](https://apiv2.waiflow.app/mcp) <br>
- [MoltFlow A2A Discovery](https://apiv2.waiflow.app/.well-known/agent.json) <br>
- [MoltFlow ERC-8004 Agent Card](https://molt.waiflow.app/.well-known/erc8004-agent.json) <br>
- [MoltFlow Python SDK](https://github.com/moltflow/moltflow-python) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with curl, JSON, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MoltFlow authentication through OAuth or MOLTFLOW_API_KEY for live actions; the artifact is documentation-only and bundles no executable files.] <br>

## Skill Version(s): <br>
2.16.4 (source: server release metadata; artifact frontmatter reports 2.16.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
