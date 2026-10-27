## Description:

使用用户指定的 B 站视频 URL、学习目标与 Easy WebBridge browserId，从网页当前可见的标题、章节和字幕整理可定位的章节笔记。适合学习复盘与资料归档；看不到字幕或摘要时仅交付可见标题、来源和缺项，不声称已看完或转录视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

External learners can use this skill with an AI agent to turn the currently visible chapters, captions, or summary on one Bilibili video page into study notes organized around a learning goal, with timestamps and page evidence. It reports missing material and does not claim to have watched or transcribed the video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separate browser bridge may interact with the selected browser environment, and draft editing can change page content.

Mitigation: Review the bridge software and prefer fixed installer or source versions. Select only the user-designated browserId; keep the workflow read-only unless draft editing is explicitly authorized.

Risk: Notes can be incomplete when captions, chapters, or summaries are not visible; bundled fixtures are offline examples rather than live collection results.

Mitigation: Limit notes to visible material, report missing content and collection scope, and do not claim to have watched or transcribed the video.

## Reference(s):

- [Easy WebBridge](https://github.com/xxjrq/easy-webbridge)
- [Easy WebBridge Gitee mirror](https://gitee.com/xxjrq/easy-webbridge)
- [EasyBR official download page](https://www.ebrower.com/down.html)
- [EasyBR GitHub release v1.7.8](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)
- [OpenCLI Bilibili adapter reference](https://github.com/jackwener/OpenCLI/blob/main/docs/adapters/browser/bilibili.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table of timestamped chapter or subtitle notes with page evidence, plus collection scope and missing-material notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only currently visible page material; at most 100 visible chapter or subtitle rows per run.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
