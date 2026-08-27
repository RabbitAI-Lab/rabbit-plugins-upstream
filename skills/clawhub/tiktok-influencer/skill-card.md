## Description:

Collect public TikTok creator videos through Gecho Bridge MCP, returning metadata, captions, engagement metrics, publish times, and links when the required Chrome extension, TikTok session, and MCP server are available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social media analysts use this skill to collect and summarize public video data from a specific TikTok creator profile through the Gecho Bridge MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a live Chrome session, the Gecho extension, and the Gecho Bridge MCP server.

Mitigation: Install and review the extension and MCP package before use, keep TikTok open only in an intended browser session, and stop if login, CAPTCHA, verification, or blocked-page prompts appear.

Risk: Creator research results may be sensitive when saved locally.

Mitigation: Use a private save directory and avoid shared or synced folders for collected TikTok creator data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with setup commands and saved JSON file paths when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs summarize selected creator-video results and avoid pasting the full raw JSON into chat.]

## Skill Version(s):

1.1.37 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
