## Description:

LinkedIn Community Management API integration with managed OAuth for managing organization pages, posts, comments, reactions, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business operators use this skill to connect a LinkedIn Community Management account through Maton, perform approved LinkedIn page and content operations, and retrieve organization, follower, page, and share analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn business access can read or change organization content and analytics.

Mitigation: Confirm the exact LinkedIn organization or account, use the narrowest available scope, and require explicit user approval before creating connections or performing writes.

Risk: Raw or long-lived API keys can be exposed through environment variables or copied into logs.

Mitigation: Prefer OAuth through the Maton CLI and OS credential store; use raw HTTP or MATON_API_KEY only when the CLI cannot be installed and handle credentials as secrets.

Risk: Hosted functions or triggers can create persistent automation that forwards sensitive data.

Mitigation: Review each function and trigger before enabling it, prefer DENY_ALL network policy for LinkedIn functions, and approve any persistent destination or non-LinkedIn event source explicitly.

## Reference(s):

- [LinkedIn Community Skill Listing](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Maton](https://maton.ai)
- [LinkedIn Community Management Overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
- [Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api)
- [Reactions API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/reactions-api)
- [Organization Lookup API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/organization-lookup-api)
- [Follower Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/follower-statistics)
- [Page Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/page-statistics)
- [Share Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics)
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

**Output Type(s):** [guidance, shell commands, API calls, code, configuration]

**Output Format:** [Markdown with inline bash, Python, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid LinkedIn Community Management connection.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
