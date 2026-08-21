## Description:

输入抖音视频链接后，用 HotBee 接口采集公开视频数据、转写文案、评论和封面/图集，并生成本地 HTML 拆解报告、评论 CSV/JSON、文案 Markdown 和报告卡片 SVG。

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、营销分析人员和开发者使用此 skill 将用户主动提供的公开抖音视频链接转换为可检查的本地中文分析包，用于视频拆解、评论洞察、文案提取和复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store public comments, transcripts, raw responses, and report files locally.

Mitigation: Review generated files before sharing and avoid committing output, raw responses, comments, or transcripts to a public repository.

Risk: The skill sends the user-provided Douyin video/share URL and accessible media URLs to HotBee.

Mitigation: Use it only when the user is comfortable sharing those URLs with HotBee and understands that comments or transcripts may require HotBee permissions or plan quota.

Risk: The skill relies on a local HotBee API key for protected comment and transcript capabilities.

Mitigation: Keep HOTBEE_API_KEY private and do not place credentials in prompts, public documents, front-end code, or shared output.

## Reference(s):

- [HotBee 抖音视频报告 on ClawHub](https://clawhub.ai/shanye1402-hash/skills/hotbee-douyin-video-report)
- [HotBee 视频解析契约](references/hotbee-analysis-contract.md)
- [HotBee Skills](https://www.hotbee.cn/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Chinese guidance plus generated local HTML, CSV, JSON, Markdown, SVG, and media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided public Douyin link and may require a local HOTBEE_API_KEY for comments and transcripts.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
