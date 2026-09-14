## Description:

GoHighLevel provides managed Private Integration Token access for CRM, sales pipelines, calendars, conversations, payments, and marketing automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and manage GoHighLevel contacts, opportunities, calendars, conversations, invoices, products, workflows, and related CRM data through an authenticated Maton connection. It supports read/list-first workflows and user-approved writes or automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive GoHighLevel CRM and business data through the user's authorized connection.

Mitigation: Install only for accounts where this access is acceptable, use least-privilege GoHighLevel scopes where available, and verify the intended account or location before acting.

Risk: Write, delete, connection, or automation setup actions can change CRM records, messaging state, invoices, workflows, or long-running trigger behavior.

Mitigation: Confirm every modifying operation with the exact resource ID, payload, destination, and intended effect before execution.

Risk: API-key or raw HTTP use can expose long-lived credentials if handled outside the CLI credential store.

Mitigation: Prefer OAuth through the Maton CLI, send API keys only to api.maton.ai when raw HTTP is unavoidable, and avoid logging raw responses or credentials.

Risk: CLI or SDK installation does not include package hashes in the evidence.

Mitigation: Install in an isolated environment and upgrade pinned tooling deliberately after reviewing release notes.

## Reference(s):

- [GoHighLevel Skill Page](https://clawhub.ai/byungkyu/skills/highlevel-api)
- [Maton Homepage](https://maton.ai)
- [GoHighLevel API Documentation](https://highlevel.stoplight.io/docs/integrations/)
- [GoHighLevel Marketplace](https://marketplace.gohighlevel.com/docs/)
- [Private Integration Token Guide](https://marketplace.gohighlevel.com/docs/integrations/custom-token)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API call proposals, resource identifiers, connection guidance, and hosted automation snippets; write, delete, connection, and automation actions require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
