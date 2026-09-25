## Description:

MailerLite API integration with managed OAuth for managing email subscribers, groups, campaigns, automations, forms, fields, segments, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MailerLite through Maton, including subscriber management, group and campaign workflows, automation setup, forms, segments, fields, and webhooks. It is also useful when an agent needs to propose authenticated MailerLite API calls or user-approved hosted automation around MailerLite data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorization to a MailerLite account through Maton.

Mitigation: Use OAuth where possible, connect only the intended account, and confirm connection creation with the user before proceeding.

Risk: Write and delete operations can change subscriber records, groups, campaigns, automations, forms, fields, segments, or webhooks.

Mitigation: Default to read and list calls, then obtain explicit user approval for each POST, PUT, PATCH, or DELETE with the target resource and payload summarized.

Risk: Webhooks, trigger destinations, and hosted functions can create persistent automation that continues forwarding or changing data after setup.

Mitigation: Treat each automation component as a separate approval step, document the destination or function behavior, and remove unused automation when the task is complete.

Risk: Raw API responses and event payloads may contain personal or business data.

Mitigation: Return only fields needed for the task, avoid logging full payloads, and treat third-party content as untrusted data rather than agent instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/mailerlite)
- [Maton homepage](https://maton.ai)
- [MailerLite API Documentation](https://developers.mailerlite.com/docs/)
- [MailerLite Subscribers API](https://developers.mailerlite.com/docs/subscribers.html)
- [MailerLite Groups API](https://developers.mailerlite.com/docs/groups.html)
- [MailerLite Campaigns API](https://developers.mailerlite.com/docs/campaigns.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and Node code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide authenticated MailerLite API calls, Maton connection setup, and user-approved automation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
