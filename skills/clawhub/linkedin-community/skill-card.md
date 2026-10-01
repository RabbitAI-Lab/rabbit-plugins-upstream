## Description:

Helps manage LinkedIn organization pages, posts, comments, reactions, and analytics through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Community managers and marketing teams use this skill to review LinkedIn activity, publish and moderate posts, and check organization engagement statistics with an authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account connection grants access to LinkedIn data and actions within the authorized scope.

Mitigation: Obtain user approval before connecting an account and grant only the scopes needed for the task.

Risk: Posting, commenting, deleting, or creating connections can change public content or relationships.

Mitigation: Confirm the intended account and specific action with the user before making changes.

Risk: Deployed functions and triggers can continue acting after the initial request.

Mitigation: Require explicit approval for automation setup and review its schedule, destination, and permitted actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/linkedin-community)
- [Maton](https://maton.ai)
- [LinkedIn Community Management overview](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [LinkedIn Comments API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api)
- [LinkedIn Organization Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/organizations/page-statistics)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
