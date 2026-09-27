## Description:

Kit (formerly ConvertKit) API integration with managed OAuth for managing subscribers, forms, tags, sequences, broadcasts, custom fields, purchase records, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Kit email-marketing workflows through Maton-managed authentication, including subscriber management, tagging, sequences, broadcasts, webhooks, and purchase records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting Maton-managed access to a Kit account can expose email-marketing data through approved account operations.

Mitigation: Install only when this access model is acceptable, use least-privilege Kit authorization where available, and review the target account before connection.

Risk: Writes can send broadcasts, alter automations, modify subscriber records, delete resources, or expose purchase data.

Mitigation: Default to read and list operations, then require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE.

Risk: Webhooks and trigger destinations can create persistent forwarding of subscriber, event, or purchase data to another host.

Mitigation: Confirm the exact destination, data fields, owner of the host, and persistence of forwarding before creation or update; remove destinations that are no longer needed.

Risk: Raw HTTP use with MATON_API_KEY can leak a long-lived credential through logs, shell history, or child processes.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, read the key from the environment only, never print or persist it, and rotate it if exposed.

## Reference(s):

- [Kit Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kit)
- [Maton](https://maton.ai)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with inline shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Kit authorization.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
