## Description:

Google Business Profile API integration with managed OAuth for reading and managing business accounts, locations, hours, attributes, reviews, photos, local posts, verification status, and performance metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to audit or update Google Business Profile listings, read customer reviews, manage listing media and posts, and retrieve search or engagement insights through a managed Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change public Google Business Profile listings, including fields customers see on Google Search and Maps.

Mitigation: Confirm every write with the user, including the exact target location by title and address and the exact value to be changed.

Risk: Approved Maton automations can persist after the immediate task is complete.

Mitigation: Create functions, triggers, and destinations only after separate user approval, keep destinations narrow, and delete connections, functions, or triggers that are no longer needed.

Risk: Long-lived API keys can be exposed through shell history, logs, child processes, or pasted output when raw HTTP is used.

Mitigation: Prefer OAuth through the Maton CLI, send keys only to api.maton.ai when raw HTTP is unavoidable, and rotate any key that may have been exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/google-business-profile)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Business Profile APIs Overview](https://developers.google.com/my-business/ref_overview)
- [Google Account Management API](https://developers.google.com/my-business/reference/accountmanagement/rest)
- [Google Business Information API](https://developers.google.com/my-business/reference/businessinformation/rest)
- [Google Performance API](https://developers.google.com/my-business/reference/performance/rest)
- [Google Verifications API](https://developers.google.com/my-business/reference/verifications/rest)
- [Google Legacy v4 API](https://developers.google.com/my-business/reference/rest)
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

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Maton CLI or raw HTTPS calls; writes, new connections, hosted functions, and automation targets require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
