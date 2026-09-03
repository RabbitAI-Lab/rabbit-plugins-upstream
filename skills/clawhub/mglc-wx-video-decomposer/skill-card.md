## Description:

基于曼格云 API 的视频号视频拆解。输入视频号分享链接或本地视频，两阶段产出作品元信息、互动数据、视觉深度拆解和 AI 分析层，并导出 Markdown、Excel 和 HTML 看板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, and content analysts use this skill to analyze WeChat Channels video posts or local video files, estimate paid API use before execution, and generate evidence-grounded content, structure, audience, and operations reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for a ManGeYun API key and can save it locally.

Mitigation: Configure WM_API_KEY through a protected environment variable or local secret/config file instead of pasting the key into chat, and rotate the key if it was exposed.

Risk: Video content and related raw API responses are sent to the ManGeYun or related analysis service.

Mitigation: Use the skill only for videos the user is comfortable uploading to that service, and avoid confidential or restricted content unless the service terms and data handling are acceptable.

Risk: Raw API responses and generated Markdown, Excel, JSON, and HTML reports may remain on disk.

Mitigation: Review generated files for sensitive content and delete or protect local raw data and reports after delivery.

Risk: Paid API calls can consume account balance when analysis proceeds after estimation.

Mitigation: Review the estimate and selected visual-analysis mode before execution, and confirm cost-sensitive runs explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/mglc-wx-video-decomposer)
- [Publisher profile](https://clawhub.ai/user/dunkong)
- [Analysis schema](artifact/references/analysis-schema.md)
- [ManGeYun API reference](artifact/references/api.md)
- [ManGeYun API service](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON analysis data, and generated Markdown, Excel, and self-contained HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a ManGeYun API key; paid API calls are estimated before execution and may upload video content to the analysis service.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists v0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
