## Description:

Run async TikTok product, trend, competitor, and content insight jobs with Gecho Bridge MCP, and check job status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start TikTok insight jobs for product opportunities, trends, competitors, and content angles, then check job status and summarize completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho's MCP bridge and Chrome extension connected to a logged-in TikTok browser session.

Mitigation: Install only after reviewing Gecho's extension and MCP setup, and keep manual control of browser logins, CAPTCHA, and session state.

Risk: TikTok insight jobs are asynchronous and may return only a jobId until processing completes.

Mitigation: Start a single insight job per turn and use the status-check workflow later to retrieve running, error, or completed results.

Risk: The skill alone cannot run TikTok insight jobs without the MCP server, Chrome extension, and logged-in browser prerequisites.

Mitigation: Confirm Node.js, npx, Gecho Bridge MCP, the Gecho Chrome extension, and an active TikTok web session before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-insight)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Website](https://gecho.ai/)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline shell commands and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May start one asynchronous TikTok insight job and return a jobId for later status checks.]

## Skill Version(s):

1.1.36 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
