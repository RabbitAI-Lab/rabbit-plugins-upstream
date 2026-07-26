## Description: <br>
OpenClaw skill for Facebook Messenger Platform workflows, including messaging, webhooks, and Page inbox operations using direct HTTPS requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to plan and operate Facebook Messenger Platform integrations, including Send API requests, webhook handling, permissions, tokens, and Page messaging workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messenger App Secrets, Page access tokens, verify tokens, webhook payloads, and recipient IDs are sensitive. <br>
Mitigation: Store secrets securely, avoid logging private conversation data, and limit token access to the minimum required permissions. <br>
Risk: Live Messenger sends or webhook handlers can affect real users if tested directly in production. <br>
Mitigation: Test with a development Page or approved recipients before sending live messages. <br>
Risk: Webhook spoofing or replayed events can lead to unauthorized processing. <br>
Mitigation: Validate webhook signatures and keep webhook handlers idempotent. <br>


## Reference(s): <br>
- [Messenger Platform Overview](artifact/references/messenger-api-overview.md) <br>
- [Messaging (Send API)](artifact/references/messaging.md) <br>
- [Permissions and Tokens](artifact/references/permissions-and-tokens.md) <br>
- [Webhooks](artifact/references/webhooks.md) <br>
- [Conversation Patterns](artifact/references/conversation-patterns.md) <br>
- [Webhook Event Map](artifact/references/webhook-event-map.md) <br>
- [HTTP Request Templates](artifact/references/request-templates.md) <br>
- [Facebook Graph API base URL](https://graph.facebook.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with HTTP request examples and JSON payload snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning guidance, permissions checklists, request templates, and operational guardrails.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata, released 2026-02-05) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
