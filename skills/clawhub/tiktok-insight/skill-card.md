## Description:

Run async TikTok product, trend, competitor, and content insight jobs with Gecho Bridge MCP, and check job status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start TikTok product, trend, competitor, and content insight jobs through Gecho Bridge MCP, then check asynchronous job status and summarize completed insight results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, and the user's logged-in TikTok browser session.

Mitigation: Install only after confirming trust in Gecho Bridge and the Chrome extension, and keep TikTok access under the user's active browser session.

Risk: A skill-only install cannot run TikTok insight jobs without the external MCP server and browser prerequisites.

Mitigation: Configure Gecho Bridge MCP, install and log in to the Gecho Chrome extension, and keep TikTok web logged in before starting insight jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-insight)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and short status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Gecho insight jobId, setup commands, saved result path, or completed insight summary when returned by the MCP tools.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
