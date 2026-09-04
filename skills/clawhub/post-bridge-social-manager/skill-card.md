## Description:

Create, schedule, and manage social media posts across Instagram, TikTok, YouTube, X, LinkedIn, Facebook, Pinterest, Threads, and Bluesky via the Post Bridge API, including media upload, post creation, scheduling, platform-specific configs, draft mode, analytics, and post result tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackfriks](https://clawhub.ai/user/jackfriks)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, schedule, update, delete, and review social media posts across connected Post Bridge accounts from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or schedule posts to real connected social accounts.

Mitigation: Confirm before live posting or scheduling unless the user explicitly asks to publish immediately, and use draft mode when intent is unclear.

Risk: The skill uses a Post Bridge API key that can act on connected accounts.

Mitigation: Install and configure it only when the user is comfortable letting an agent use that key, and stop if no valid key is available.

Risk: Media files, captions, account identifiers, and scheduling metadata are sent to Post Bridge.

Mitigation: Review selected accounts, media, captions, and scheduling details before sending them to the service.

Risk: Optional video workflows can run local commands, move files, or add cron jobs.

Mitigation: Ask for confirmation with exact commands, paths, or crontab lines before taking those optional local actions.

## Reference(s):

- [Post Bridge website](https://post-bridge.com)
- [Post Bridge API reference](https://api.post-bridge.com/reference)
- [Post Bridge API key settings](https://www.post-bridge.com/dashboard/api-keys)
- [Post Bridge MCP](https://post-bridge.com/mcp)
- [ClawHub skill listing](https://clawhub.ai/jackfriks/skills/post-bridge-social-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command execution returns JSON responses from Post Bridge operations when used through the CLI or API.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
