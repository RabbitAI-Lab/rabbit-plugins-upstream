## Description:

Posty schedules and publishes social posts from the command line to Facebook, Instagram, X, LinkedIn, TikTok, YouTube, Threads, Bluesky, Telegram, Discord and Slack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[norbertlevente](https://clawhub.ai/user/norbertlevente)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social-media operators use this skill to guide authenticated Posty CLI workflows for discovering connected channels, preparing media, scheduling or publishing posts, and checking analytics across supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated social-media publishing can post, schedule, alter status, or delete content through granted channels.

Mitigation: Use scoped API keys or carefully approved device login, grant only needed workspaces and channels, and review content before publishing or deleting posts.

Risk: Credential misuse could expose authorized Posty workspaces or channels.

Mitigation: Prefer least-privilege keys, rotate lost or overbroad keys, and avoid storing broad credentials in shared environments.

Risk: Incorrect media, channel, or provider settings can cause rejected posts or unintended drafts.

Mitigation: Confirm authentication, connected integrations, required provider settings, and Posty-uploaded media URLs before creating posts.

Risk: Unpinned CLI installation may change behavior in sensitive environments.

Mitigation: Consider pinning the trusted package or source revision before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/norbertlevente/skills/posty)
- [Posty website](https://posty.hu)
- [Posty API base](https://api.posty.hu)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output from Posty CLI is expected to be JSON on stdout, with status and errors on stderr.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
