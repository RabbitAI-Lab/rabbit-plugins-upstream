## Description:

GoHighLevel (GHL) Integration connects AI agents to the GoHighLevel API v2 for contact management, opportunity pipeline updates, unanswered lead triage, workflow triggers, multi-channel messaging, and webhook lead ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and sales teams use this skill to configure GoHighLevel credentials, inspect CRM state, triage unanswered leads, move opportunities through pipelines, and prepare customer messaging workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for powerful GHL and Meta credentials and can support high-impact CRM actions.

Mitigation: Use least-privilege tokens, start in a sandbox GHL location, and avoid production credentials until gateway operator and data handling terms are clear.

Risk: The evidence reports externally hosted or unaudited execution paths and referenced local scripts.

Mitigation: Independently audit and pin any gateway endpoint or local script before running it in a real customer environment.

Risk: Outbound messages and CRM mutations can affect customers or alter sales records.

Mitigation: Require explicit human approval before sending messages, moving opportunities, deleting records, or changing structural workflows.

Risk: Webhook ingestion can expose CRM workflows if configured without authentication or transport protection.

Mitigation: Use HTTPS authenticated webhooks and isolate requests by GHL location before enabling live lead ingestion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/ghl-integration)
- [Habilis MCP gateway homepage](https://xvix.com.br)
- [GoHighLevel API v2 integration insights](references/ghl_api_v2_insights.md)
- [Instagram follow-gate and GHL sync pattern](references/instagram_follow_gate_ghl_sync.md)
- [STEVO WhatsApp reference](references/stevo-whatsapp.md)
- [Unanswered leads triage patterns](references/unanswered_leads_triaging_patterns.md)
- [Zero-touch orchestration and webhook architecture](references/zero_touch_and_webhooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and API-call patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose CRM mutations, webhook setup, or outbound message actions that require credential scope review and user approval.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
