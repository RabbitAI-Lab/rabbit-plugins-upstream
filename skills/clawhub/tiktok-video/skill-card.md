## Description:

Get TikTok video detail data and comments from a known TikTok video URL with the official Gecho Bridge MCP tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social-media analysts use this skill to collect metadata, comments, replies, and engagement context for one known TikTok video URL through the Gecho Bridge MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a third-party Gecho MCP package and Chrome extension connected to a logged-in TikTok browser session.

Mitigation: Install only after reviewing the Gecho package, extension, and account-session requirements, and keep authentication or CAPTCHA resolution manual in Chrome.

Risk: Raw TikTok video and comment data may be saved as local JSON and could contain sensitive or regulated information.

Mitigation: Choose an appropriate writable save directory, limit sharing of raw result files, and review local retention before using collected data.

Risk: TikTok page state, login walls, private or deleted videos, regional blocks, or limited comment exposure can make results partial or unavailable.

Mitigation: Report page state and available counts exactly, avoid fabricating missing fields or comments, and retry only after the user resolves access issues in Chrome.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-video)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub and README](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON, Files, Markdown]

**Output Format:** [Markdown guidance with shell command blocks and structured TikTok video detail/comment data, optionally saved as local JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a single Gecho MCP job per turn; targetCount is capped at 200 comments and replies; outputs depend on data available in the live logged-in TikTok browser session.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
