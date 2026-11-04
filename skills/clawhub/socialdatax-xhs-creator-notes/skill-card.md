## Description:

用于小红书博主数据、小红书博主笔记、账号内容列表、近期发布、内容调研和创作者内容分析。覆盖 Xiaohongshu / XHS / RedNote creator notes，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要研究小红书创作者及其近期笔记的用户，获取账号笔记列表并支持内容调研、风格分析、创作者对比和账号跟踪。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or files could be exposed to downloaded software or in shared content.

Mitigation: Use a reviewed, fixed CLI version; expose only needed credentials and files; keep API keys out of chat and version control.

Risk: Large creator note requests can increase usage charges.

Mitigation: Set explicit page or item limits for each request.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-notes)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Creator note data as JSON, with concise text or Markdown summaries and command or configuration guidance as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator note results may include titles or descriptions, summaries, publish times, interaction counts, media links, and content types when available.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
