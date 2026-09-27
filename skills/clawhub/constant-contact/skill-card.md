## Description:

Constant Contact API integration with managed OAuth for reading and managing contacts, email campaigns, contact lists, tags, custom fields, segments, bulk operations, and marketing analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, developers, and support teams use this skill to inspect and manage Constant Contact marketing data through Maton-authenticated API calls. It is suited for read/list workflows by default and explicit, reviewed write actions such as contact updates, list changes, campaign scheduling, or bulk operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable API calls can create, update, delete, or bulk-modify Constant Contact resources.

Mitigation: Default to read/list calls, verify resource identifiers first, and require explicit user approval with the target, payload, and intended effect before any write.

Risk: Campaign sending or scheduling can deliver email to external recipients and may be irreversible.

Mitigation: Preview the campaign and confirm recipients, subject, content, timing, and consequences before sending or scheduling.

Risk: Contacts and reports may contain personal data and marketing engagement history.

Mitigation: Request the narrowest fields and records needed, avoid broad exports, and do not forward contact data to third-party hosts without explicit approval for that transfer.

Risk: Connections, functions, triggers, and destinations can create ongoing access or automation.

Mitigation: Review every connection, function, trigger, and destination before approval, prefer platform-hosted destinations, use restrictive network policy for functions, and revoke or delete unused resources when finished.

Risk: Long-lived credentials or raw tokens could be exposed if handled outside the documented OAuth and credential-store flow.

Mitigation: Use Maton OAuth where possible, avoid printing or exporting credentials, and prefer stored profiles over environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Constant Contact V3 API Overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API Reference](https://developer.constantcontact.com/api_reference/index.html)
- [Constant Contact Technical Overview](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)
- [Constant Contact Contacts Overview](https://developer.constantcontact.com/api_guide/contacts_overview.html)
- [Constant Contact Email Campaigns Guide](https://developer.constantcontact.com/api_guide/email_campaigns_get_started.html)
- [Constant Contact Contact Lists Overview](https://v3.developer.constantcontact.com/api_guide/lists_overview.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time trigger catalogue](references/time/triggers.md)
- [GitHub trigger catalogue](references/github/triggers.md)
- [Google Mail trigger catalogue](references/google-mail/triggers.md)
- [Slack trigger catalogue](references/slack/triggers.md)
- [Stripe trigger catalogue](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for write, send, bulk, connection, function, and trigger actions.]

## Skill Version(s):

1.2.4 (source: server release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
