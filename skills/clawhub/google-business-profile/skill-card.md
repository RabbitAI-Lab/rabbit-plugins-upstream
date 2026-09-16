## Description:

Google Business Profile API integration with managed OAuth for reading and managing business accounts, locations, hours, attributes, reviews, photos, local posts, verification status, and performance metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators, support teams, and developers use this skill to audit and update Google Business Profile listings, review customer feedback, manage listing media and posts, and pull search or engagement insights through a Maton-managed connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public listing changes can affect information customers see on Google Search and Maps.

Mitigation: Require explicit user confirmation of the specific business location, exact fields, payload, and intended effect before any write or delete operation.

Risk: Package installation or raw API-key usage can expose account credentials if the source or handling is not trusted.

Mitigation: Use trusted, pinned Maton CLI or SDK versions, prefer OAuth, and avoid printing, persisting, logging, or passing API keys on command lines.

Risk: Hosted functions, triggers, and destinations can create persistent automated side effects or data forwarding.

Mitigation: Approve the handler, connection, destination host, payload fields, and persistence behavior before creating automation; delete unused functions, triggers, and destinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/google-business-profile)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Business Profile APIs Overview](https://developers.google.com/my-business/ref_overview)
- [Google Account Management API](https://developers.google.com/my-business/reference/accountmanagement/rest)
- [Google Business Information API](https://developers.google.com/my-business/reference/businessinformation/rest)
- [Google Performance API](https://developers.google.com/my-business/reference/performance/rest)
- [Google Verifications API](https://developers.google.com/my-business/reference/verifications/rest)
- [Google Business Profile Legacy v4 API](https://developers.google.com/my-business/reference/rest)
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

**Output Format:** [Markdown guidance with inline shell commands, code snippets, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Google Business Profile API request guidance, Maton CLI commands, OAuth or API-key setup steps, hosted function examples, trigger setup guidance, and safety checks for writes or automation.]

## Skill Version(s):

1.2.1 (source: server release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
