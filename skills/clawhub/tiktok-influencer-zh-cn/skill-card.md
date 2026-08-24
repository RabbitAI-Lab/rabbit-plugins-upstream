## Description:

通过 Gecho Bridge MCP 采集 TikTok 创作者的公开视频，返回视频元数据、文案、互动指标、发布时间和链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social-media researchers use this skill to collect and summarize public TikTok creator video metadata through the Gecho Bridge browser-extension workflow. It is intended for single-creator video research, content pattern analysis, and retrieving saved local JSON results when the Gecho MCP service and logged-in browser session are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a logged-in TikTok browser session and the Gecho Chrome extension.

Mitigation: Install and use it only when you are comfortable connecting Gecho Bridge to that browser session.

Risk: Creator research results may be saved locally in the workspace.

Mitigation: Use an explicit save_dir on shared or managed machines, and avoid saving data you do not want retained.

Risk: TikTok login checks, verification prompts, regional notices, or page blockers can prevent collection.

Mitigation: Resolve those prompts manually in Chrome before running the skill, and stop rather than fabricating results when the tool returns empty data or an error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer-zh-cn)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw + TikTok Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes + TikTok Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise result summaries; collected creator data may be saved locally as JSON by the Gecho MCP tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes the most useful fields from successful runs and avoids pasting full raw JSON into the chat.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
