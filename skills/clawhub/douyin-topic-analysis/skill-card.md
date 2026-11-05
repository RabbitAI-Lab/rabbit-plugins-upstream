## Description:

当用户需要做抖音选题、抖音内容选题、短视频选题策划、爆款角度拆解、内容方向规划或选题素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容运营、品牌调研人员和创作者，按关键词或选题方向检索抖音热榜及作品样本，并整理标题、作者、链接或内容 ID，辅助规划内容方向和后续追问。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and may consume paid credits.

Mitigation: Avoid confidential queries unless intended; begin with one page and expand only when needed.

Risk: The runtime package implementation was not bundled for inspection.

Mitigation: Review and preferably pin the npm package version before execution.

Risk: A locally stored API key could be exposed if committed or shared.

Mitigation: Store the key using the client's secret facility and keep local credential files out of version control.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown summarizing Douyin samples, their titles and authors, links or content IDs, and suggested angles for follow-up.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
