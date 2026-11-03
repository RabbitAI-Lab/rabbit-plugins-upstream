## Description:

Manage social posts and analytics across platforms connected to an AdaptlyPost account, including drafting, scheduling, publishing, account management, recurring posts, and webhooks with the user's required approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account use this skill to draft, schedule, publish, edit, and review posts on their connected social accounts, manage account and recurring-post settings, and read analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media is publicly reachable as soon as it is uploaded, including before a post is created.

Mitigation: Confirm the exact user-named media file before upload and avoid uploading sensitive material.

Risk: A registered webhook receives workspace-wide events, including post text, media URLs, account names, and AI image prompts.

Mitigation: Register only a URL supplied by the user after explaining the data it will receive and getting explicit approval; delete the webhook when it is no longer needed.

Risk: An API token can act on the connected accounts allowed by its workspace role.

Mitigation: Use a dedicated, revocable token with the lowest role needed, and connect only necessary accounts.

Risk: With plain curl, approval safeguards depend on the agent following the skill instructions.

Mitigation: Require explicit confirmation before each post or other high-impact action, and default uncertain or unattended posts to drafts.

## Reference(s):

- [AdaptlyPost API reference](references/api-reference.md)
- [Platform configuration reference](references/platform-configs.md)
- [AdaptlyPost API OpenAPI document](https://post.adaptlypost.com/post/api/v1/openapi.json)
- [AdaptlyPost ClawHub release](https://clawhub.ai/tarasshyn/skills/adaptlypost)

## Skill Output:

**Output Type(s):** [API calls, Text, Shell commands]

**Output Format:** [API request data and concise text responses, with curl commands where needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Post, account, and webhook actions follow the skill's explicit user approval requirements.]

## Skill Version(s):

1.27.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
