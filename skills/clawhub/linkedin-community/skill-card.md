## Description:

LinkedIn Community manages LinkedIn organization pages, posts, comments, reactions, and analytics through the Maton CLI with managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing operators, and social media teams use this skill to inspect LinkedIn organizations and posts, retrieve analytics, and prepare or execute confirmed changes through Maton-authenticated LinkedIn Community Management API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn posts, comments, reactions, edits, or deletions can affect public content and organizational reputation.

Mitigation: Require explicit user confirmation for every write operation, including the target identity, resource, payload, and intended effect.

Risk: OAuth tokens or Maton API keys could be exposed if copied, printed, logged, or passed on command lines.

Mitigation: Prefer Maton CLI OAuth, keep credentials in the operating system credential store, never inspect stored secrets, and use the documented stdin-based raw HTTP fallback only when the CLI is unavailable.

Risk: Actions could be applied to the wrong LinkedIn account, organization, or Maton connection.

Mitigation: Verify the active Maton profile, connection, LinkedIn identity, and organization before performing writes, and specify the connection when more than one exists.

Risk: Content returned by LinkedIn or Maton may include untrusted text that attempts to influence later agent behavior.

Mitigation: Treat API responses as data, validate identifiers and payloads, and do not execute or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-community)
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

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance, Markdown, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid LinkedIn Community Management connection.]

## Skill Version(s):

1.1.0 (source: server release evidence, created 2026-08-26T07:27:33Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
