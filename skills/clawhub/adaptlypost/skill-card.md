## Description:

Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest, YouTube and Google Business Profile accounts connected to AdaptlyPost, and read their analytics. Use only when the user has an AdaptlyPost account and asks to draft, schedule or publish a post on those accounts, upload media for such a post, list the connected accounts, check a post's status, or ask about views, likes, comments, followers or top posts on them. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account use this skill to manage connected social accounts: draft, schedule, publish, review, and analyze posts across supported platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection links may have broad access by default.

Mitigation: Set PRIVATE visibility, restrict allowed platforms and account count, use a short expiry, and revoke the link after use.

Risk: An API token with excessive permissions can enable unintended account or publishing actions.

Mitigation: Use a Contributor token for drafts and an Editor token only when publishing is needed; avoid Admin access unless onboarding requires it.

Risk: Uploaded media may become publicly accessible, and webhook events may reach an untrusted destination.

Mitigation: Upload only media ready to be public and send webhook events only to a trusted destination.

## Reference(s):

- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform Configurations](references/platform-configs.md)
- [AdaptlyPost API](https://post.adaptlypost.com/post/api/v1)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [API-backed social account and post actions with concise text or structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May draft, schedule, publish, edit, or delete social posts when authorized.]

## Skill Version(s):

1.19.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
