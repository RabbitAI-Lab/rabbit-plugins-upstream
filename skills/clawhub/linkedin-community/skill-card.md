## Description:

Helps manage LinkedIn organization pages, posts, comments, reactions, and analytics through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Community managers and marketing teams use this skill to draft and manage LinkedIn posts and conversations, look up organizations, and review page, follower, and share statistics with an authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, editing, deleting, commenting, or reacting can change public LinkedIn content.

Mitigation: Confirm the exact account or organization and intended effect with the user before each write.

Risk: An exposed API key or overly broad connection can allow unintended account access.

Mitigation: Use managed OAuth, request only necessary scopes, and do not expose API keys.

Risk: Hosted functions and triggers can continue acting or forwarding events after setup.

Mitigation: Obtain separate approval, limit automation to the requested task, and remove it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [LinkedIn Community Management overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [LinkedIn Share Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/share-statistics)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with API examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize authorized LinkedIn data and propose actions for user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
