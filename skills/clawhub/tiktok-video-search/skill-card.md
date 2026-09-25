## Description:

Search TikTok videos by keyword with Gecho Bridge MCP and return video metadata, creators, engagement metrics, and links. Requires the Gecho Chrome extension, an active TikTok session, and the Gecho Bridge MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run keyword-level TikTok video searches through Gecho Bridge MCP, then collect video metadata, creator names, engagement metrics, links, and local JSON result files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects Gecho to a logged-in TikTok browser session through the Gecho Chrome extension and MCP workflow.

Mitigation: Use an account and browser profile appropriate for the data being collected, and review the Gecho MCP package and Chrome extension before use in environments with stricter privacy requirements.

Risk: TikTok search metadata may be saved to a local result file.

Mitigation: Choose a save directory appropriate for the collected data and avoid shared or sensitive locations unless that storage is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-video-search)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and summaries of JSON video metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report a saved local JSON result path. Requires node/npx, Gecho Bridge MCP, the Gecho Chrome extension, and an active logged-in TikTok browser session; ClawHub metadata lists darwin, linux, and win32/windows support.]

## Skill Version(s):

1.1.38 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
