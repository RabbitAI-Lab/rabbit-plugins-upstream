## Description:

Schedule, publish, and review posts on supported social platforms through an AdaptlyPost account, and read post status and analytics for connected accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account use this agent to manage connected social accounts: draft, schedule, publish, and review posts, check delivery status, and read analytics. It is not for general caption writing or accounts not connected to AdaptlyPost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default account-connection links can expose unrelated workspace accounts and permit unlimited connections.

Mitigation: Set PRIVATE visibility, limit selected platforms and account count, use a short expiry, and revoke the link after use.

Risk: Uploaded media becomes publicly accessible immediately, and webhooks receive workspace-wide events.

Mitigation: Confirm media is suitable for public access before uploading; verify webhook signatures and handle only the events needed.

## Reference(s):

- [AdaptlyPost website](https://adaptlypost.com)
- [AdaptlyPost skill listing](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [API reference](references/api-reference.md)
- [Platform configurations](references/platform-configs.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Guidance, Analysis]

**Output Format:** [JSON API requests and responses, with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create externally visible posts or upload publicly accessible media; publishing requires explicit confirmation.]

## Skill Version(s):

1.20.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
