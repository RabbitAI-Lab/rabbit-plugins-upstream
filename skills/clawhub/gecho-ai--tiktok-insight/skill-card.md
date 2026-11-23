## Description:

Runs asynchronous TikTok product, trend, competitor, and content insight jobs with Gecho Bridge MCP and checks job status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to start and monitor TikTok insight jobs for product opportunity analysis, trend discovery, competitor research, and content strategy. It is intended for workflows where the Gecho Bridge MCP server, Gecho Chrome extension, and an active TikTok web session are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho Bridge MCP, the Gecho Chrome extension, and a logged-in TikTok browser session, so browser-session data access depends on those external components.

Mitigation: Review the Gecho Bridge package, Chrome extension permissions, and account/session requirements before installation or use.

Risk: Insight jobs may fail or stall when the MCP server, extension login, TikTok login, browser tab, network, or CAPTCHA state is not ready.

Mitigation: Confirm the MCP server is configured, the extension is online, TikTok web is logged in, and any CAPTCHA or login wall is resolved before starting or checking a job.

## Reference(s):

- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Website](https://gecho.ai/)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Gecho insight job ID, setup commands, status updates, or concise result summaries depending on tool availability and job state.]

## Skill Version(s):

1.1.38 (source: ClawHub release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
