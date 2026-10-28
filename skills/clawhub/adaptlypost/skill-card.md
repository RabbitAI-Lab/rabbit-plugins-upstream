## Description:

Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest, YouTube and Google Business Profile accounts connected to AdaptlyPost, and read their analytics. Use only when the user has an AdaptlyPost account and asks to draft, schedule or publish a post on those accounts, upload media for such a post, list the connected accounts, check a post's status, or ask about views, likes, comments, followers or top posts on them. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account can use the skill to manage posts on their connected social accounts, upload media, check post status, and review analytics. It is intended for social publishing workflows, not standalone caption writing or general social media advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-connection links can grant broader access than intended.

Mitigation: Request a private link limited to the intended platform and account count, with a short expiry.

Risk: Persistent webhooks can expose workspace events to their recipient, and uploaded media becomes publicly reachable before posting.

Mitigation: Approve webhooks only for trusted recipients that need ongoing events, remove them when no longer needed, and upload only media the user has approved for public access.

## Reference(s):

- [AdaptlyPost API reference](artifact/references/api-reference.md)
- [Platform configuration reference](artifact/references/platform-configs.md)
- [AdaptlyPost](https://adaptlypost.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Concise text or Markdown responses, with curl commands and JSON request or response data when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post details, status, and analytics returned by the connected service.]

## Skill Version(s):

1.21.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
