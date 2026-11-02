## Description:

Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest, YouTube, Google Business Profile and Telegram accounts connected to AdaptlyPost, and read their analytics. Use only when the user has an AdaptlyPost account and asks to draft, schedule, publish, edit or delete a post on those accounts, upload media for such a post, pause, resume or delete a recurring post, list, re-check or disconnect the connected accounts, check a post's status, create a link for someone else to connect an account, register a webhook at a URL they give, or ask about views, likes, comments, followers or top posts on them. Every delete, disconnect, connect link and webhook needs the user's explicit yes first. Do not use for writing captions without posting, general social media advice, or accounts that are not connected to AdaptlyPost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account can use the skill to manage social posts and connected accounts across supported platforms, and to review post status and analytics. Posting, uploads, and account or webhook changes require the confirmations described in the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Posts are public, and uploaded media becomes public as soon as it is uploaded, including when the post remains a draft.

Mitigation: Confirm the exact post content, accounts, timing, and visibility before posting; verify the user-named media file before upload and prefer drafts when uncertain.

Risk: A webhook receives all workspace events, and with curl approval rules depend on the agent following them.

Mitigation: Register only a URL provided by the user after explaining the workspace-wide event scope and obtaining explicit approval; use a dedicated token and limit connected accounts.

## Reference(s):

- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform Configuration Reference](references/platform-configs.md)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API](https://post.adaptlypost.com/post/api/v1)
- [AdaptlyPost OpenClaw plugin integration](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Social post drafts and status or analytics summaries, with API request examples and setup guidance where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific post settings and media references.]

## Skill Version(s):

1.26.0 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
