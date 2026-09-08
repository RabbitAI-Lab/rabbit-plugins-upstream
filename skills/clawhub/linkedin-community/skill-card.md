## Description:

LinkedIn Community Management API integration with managed OAuth for managing organization pages, posts, comments, reactions, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to help an agent make LinkedIn Community Management API calls for organization pages, posts, comments, reactions, analytics, and related account lookups. It is suited to workflows where the agent should default to read/list operations and ask for confirmation before creating connections or changing LinkedIn content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help publish, edit, or delete LinkedIn posts, comments, and reactions.

Mitigation: Review every proposed write, deletion, connection creation, or public post before approving it, including the target resource, content, and LinkedIn identity.

Risk: Authentication may involve long-lived credentials if API keys are used instead of OAuth.

Mitigation: Prefer OAuth through the Maton CLI, avoid exposing tokens or API keys, and use credential checks that do not print secret values.

Risk: Actions may apply to the wrong Maton connection or LinkedIn organization when multiple accounts are available.

Mitigation: Verify the intended Maton connection and LinkedIn organization before acting, and specify the connection when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, code snippets, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK-oriented guidance; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
