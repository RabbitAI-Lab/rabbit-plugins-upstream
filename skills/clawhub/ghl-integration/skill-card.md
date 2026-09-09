## Description:

Integrates agents with GoHighLevel API v2 for contact management, pipeline updates, unanswered-lead triage, multi-channel messaging, and webhook-based lead ingestion through the Habilis gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

External CRM operators, agencies, and developers use this skill to automate GoHighLevel contact handling, opportunity movement, unanswered-lead triage, outbound follow-up, and webhook-based lead intake.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live CRM mutations, workflow enrollment, Kanban movement, and outbound messaging.

Mitigation: Require human confirmation for outbound messages, destructive actions, workflow changes, and CRM mutations; limit API scopes to the minimum needed.

Risk: The skill uses API credentials, location IDs, manager phone numbers, gateway tokens, and local helper scripts.

Mitigation: Store secrets outside shell history and committed files, prefer short-lived credentials, rotate exposed tokens, and verify all local scripts before production use.

Risk: Webhook and gateway setup can expose lead data or accept forged events if deployed without transport and request validation.

Mitigation: Use HTTPS, signed or otherwise verified webhooks, tenant-specific routing, and explicit validation before accepting events into CRM workflows.

Risk: Broad conversation searches can mix third-party broadcasts with real leads or advertising audit data.

Mitigation: Filter group and broadcast-like senders, keep conversation links separate from ad landing page audits, and require source checks before reporting campaign findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/ghl-integration)
- [Habilis gateway](https://xvix.com.br)
- [Habilis MCP endpoint](https://xvix.com.br/api/mcp)
- [Support and developer portal](https://portal.sthub.com.br)
- [GoHighLevel API v2 Integration Insights](references/ghl_api_v2_insights.md)
- [GHL API v2 - Custom Provider (STEVO / WhatsApp QR) & Contact Resolution Reference](references/stevo-whatsapp.md)
- [GHL Unanswered Leads Triaging & Pattern Recognition](references/unanswered_leads_triaging_patterns.md)
- [Zero-Touch Orchestration & Dynamic Webhook Architecture](references/zero_touch_and_webhooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, environment variables, JSON/API examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational cautions for CRM mutation, outbound messaging, credentials, webhooks, and local helper scripts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
