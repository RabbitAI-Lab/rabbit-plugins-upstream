## Description:

LinkedIn Community Management API integration with managed OAuth for managing organization pages, posts, comments, reactions, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, social media operators, and agent workflows use this skill to manage LinkedIn organization pages, posts, comments, reactions, and analytics through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public posting, editing, deleting, commenting, and reacting can affect the selected LinkedIn person or organization identity.

Mitigation: Confirm the action, target resource, intended content, and LinkedIn identity with the user before any write operation.

Risk: Maton or provider credentials could be exposed if tokens or API keys are printed, logged, persisted, or passed on a command line.

Mitigation: Prefer Maton OAuth through the CLI credential store; never print or persist credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: When multiple Maton profiles or LinkedIn connections exist, an ambiguous default could send a request to the wrong account or organization.

Mitigation: Verify the active Maton connection and target LinkedIn organization before acting, and specify the connection or profile where ambiguity exists.

Risk: LinkedIn API responses may contain untrusted content or instructions.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into shell commands, and let the user choose follow-up actions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [LinkedIn Community Management Overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [LinkedIn Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api)
- [LinkedIn Reactions API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/reactions-api)
- [LinkedIn Organization Lookup API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/organization-lookup-api)
- [LinkedIn Follower Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/follower-statistics)
- [LinkedIn Page Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/page-statistics)
- [LinkedIn Share Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with CLI commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before write operations or new connection authorization.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
