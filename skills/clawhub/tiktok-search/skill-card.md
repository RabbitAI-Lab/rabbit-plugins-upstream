## Description:

Search TikTok videos, collect creator videos, and run product, trend, competitor, and content insights through Gecho Bridge MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social media researchers use this skill to search TikTok videos, collect creator metadata, and start product, trend, competitor, or content insight jobs through Gecho Bridge MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho's MCP server, Chrome extension, and a logged-in TikTok browser session.

Mitigation: Install only if comfortable with that workflow, keep the extension logged in intentionally, and review Gecho extension and npm package provenance before use.

Risk: Search and insight jobs can export result JSON files to a local save directory.

Mitigation: Use a workspace save directory and review exported files before sharing or committing them.

Risk: TikTok login walls, CAPTCHA, frozen browser tabs, or missing MCP tools can prevent searches or insight jobs from running.

Mitigation: Confirm MCP configuration, Node/npx availability, Gecho extension login, and an active TikTok web session before starting a job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-search)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize TikTok result metadata, report saved JSON file paths, or return asynchronous insight job IDs.]

## Skill Version(s):

1.1.36 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
