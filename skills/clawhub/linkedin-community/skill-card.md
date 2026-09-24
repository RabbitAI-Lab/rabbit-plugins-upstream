## Description:

LinkedIn Community Management API integration with managed OAuth for managing organization pages, posts, comments, reactions, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to operate LinkedIn Community Management workflows through Maton, including reading analytics and creating or managing posts, comments, reactions, organization lookups, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify public LinkedIn posts, comments, and reactions through the connected account.

Mitigation: Confirm the exact LinkedIn identity, target resource, content, and intended effect with the user before every write operation.

Risk: LinkedIn OAuth access and Maton API keys can expose account capabilities if mishandled.

Mitigation: Prefer OAuth, keep credentials in the platform or operating-system credential store, and never print, persist, or forward access tokens or API keys.

Risk: Triggers and destinations create persistent automation and ongoing data forwarding.

Mitigation: Create them only for a specific approved workflow, disclose the destination host and payload fields, prefer Maton-controlled destinations, and remove unused automations.

Risk: External content and trigger payloads may contain sensitive data or adversarial instructions.

Mitigation: Treat returned content as untrusted data, forward only fields needed for the task, and never execute local handlers or commands from untrusted payload content without separate user review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Maton homepage](https://maton.ai)
- [LinkedIn Community Management Overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [LinkedIn Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api)
- [LinkedIn Reactions API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/reactions-api)
- [LinkedIn Organization Lookup API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/organization-lookup-api)
- [LinkedIn Follower Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/follower-statistics)
- [LinkedIn Page Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/page-statistics)
- [LinkedIn Share Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and small code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and LinkedIn authorization; outputs should be reviewed before writes or persistent automation are created.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
