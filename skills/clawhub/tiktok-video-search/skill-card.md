## Description:

Search TikTok videos by keyword with Gecho Bridge MCP, returning video metadata, creators, engagement metrics, and links for users with the Gecho Chrome extension, an active TikTok session, and the Gecho Bridge MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social media researchers use this skill to run keyword-level TikTok video searches through Gecho Bridge and summarize creators, engagement metrics, links, and saved result files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow connects Gecho Bridge and the Chrome extension to a logged-in TikTok browser session.

Mitigation: Before installing or running searches, confirm the user is comfortable using a logged-in TikTok session through the official Gecho Bridge workflow.

Risk: Saved raw search results may reveal sensitive research interests or account-derived content.

Mitigation: Use a user-selected save_dir with appropriate access controls, or delete saved result files after use.

Risk: Searches depend on the Gecho Bridge MCP server, Gecho Chrome extension, and active TikTok browser session being available.

Mitigation: Provide setup guidance when prerequisites are missing and avoid inventing or retrying results when the official tool is unavailable or returns no data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-video-search)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [API Calls, Configuration instructions, Shell commands, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples and structured TikTok search results returned as JSON plus saved local result files when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful searches summarize the top 3 to 5 results and include a saved file path when available.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
