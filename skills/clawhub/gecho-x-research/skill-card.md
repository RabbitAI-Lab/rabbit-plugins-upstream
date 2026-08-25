## Description:

Search X (Twitter) posts and retrieve known post details and replies through the official Gecho Bridge MCP tools for keyword monitoring, post research, author context, engagement signals, and reply analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to discover X posts by keyword, inspect known posts and replies, compare engagement signals, and summarize representative social-media context through Gecho Bridge MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow connects agent activity to a logged-in Chrome and X session through the Gecho extension.

Mitigation: Install and use it only when that account linkage is acceptable, and resolve login walls, CAPTCHA, verification prompts, rate limits, and blocked pages manually in Chrome.

Risk: Saved raw post and reply JSON may contain personal data from posts, authors, and replies.

Mitigation: Save results only in trusted directories, avoid pasting full raw JSON into chat, and delete result files when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/gecho-x-research)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries with optional local JSON result files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful workflows summarize posts, authors, engagement, representative replies, and saved paths without pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
