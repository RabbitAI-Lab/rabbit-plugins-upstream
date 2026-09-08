## Description:

基于曼格云 API 的视频号视频拆解。输入视频号分享链接或本地视频，两阶段产出作品元信息、互动数据、视觉拆解和 AI 分析，并导出 Markdown、Excel 和 HTML 看板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze WeChat Channels video links or local video files, then produce evidence-backed content diagnostics, audience assumptions, viral attribution, scoring, and operational recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide a paid Mangu Cloud API key and may save it in plaintext configuration.

Mitigation: Prefer a local secret mechanism or environment variable for WM_API_KEY; delete or rotate the key if it was shared in chat.

Risk: Selected videos and metadata are sent to Mangu Cloud or related processing services for analysis.

Mitigation: Use only videos the user is comfortable processing through those services, and avoid sensitive or confidential media unless appropriate approvals exist.

Risk: Generated HTML reports can request the original cover image from finder.video.qq.com when viewed.

Mitigation: Review generated HTML before sharing and avoid opening or publishing reports when external image requests would expose sensitive context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/mglc-wx-video-decomposer)
- [曼格云视频号视频拆解 API 目录](references/api.md)
- [AI 分析层 Schema](references/analysis-schema.md)
- [Mangu Cloud API service](https://api.we-media.cn?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report, Excel workbook, HTML dashboard, JSON analysis files, and concise agent guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Mangu Cloud API key and user confirmation before paid API calls.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports v0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
