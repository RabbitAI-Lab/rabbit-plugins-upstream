## Description:

Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, Mastodon, TikTok, Threads, LinkedIn, Facebook, Pinterest and YouTube accounts connected to AdaptlyPost, and read their analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, social media, and operations teams use this skill to draft, schedule, publish, retry, and review posts and analytics for social accounts already connected to AdaptlyPost. It is intended for users who have an AdaptlyPost account and a dedicated API token for the accounts they want an agent to operate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token delegates access to every social account in its AdaptlyPost account group.

Mitigation: Use a dedicated, revocable API token and keep the connected account group limited to accounts the agent should operate.

Risk: Publishing, retrying, and some scheduled actions can make content public under the user's connected social accounts.

Mitigation: Require explicit user confirmation for content, platforms, accounts, timing, and visibility before write calls, and prefer drafts when the user is uncertain.

Risk: Uploaded media can become reachable at a public URL before a post is created or published.

Mitigation: Confirm exact file paths, upload only user-named media files, avoid broad personal folders, and refuse non-media or sensitive files.

Risk: Connect links, webhook secrets, and API tokens can grant access or reveal account workflow details if exposed.

Mitigation: Treat these values as sensitive, avoid public channels and logs, and revoke connect links after use.

## Reference(s):

- [AdaptlyPost skill page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API reference](references/api-reference.md)
- [Platform-specific configs reference](references/platform-configs.md)
- [AdaptlyPost OpenClaw plugin](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl commands, JSON request bodies, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and the ADAPTLYPOST_API_KEY environment variable for API calls.]

## Skill Version(s):

1.7.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
