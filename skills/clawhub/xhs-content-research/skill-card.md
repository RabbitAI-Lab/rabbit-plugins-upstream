## Description:

面向内容运营、品牌调研和创作者的小红书内容研究辅助技能。适用于 RedNote / XHS / Xiaohongshu（小红书）内容研究、选题分析、关键词观察、趋势判断、竞品内容对比和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、品牌研究者和创作者可用它按关键词搜索小红书内容，整理内容样本、创作者信息和链接，并分析选题角度、趋势及受众反馈。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and may use paid credits.

Mitigation: Avoid confidential search terms and set page or item limits.

Risk: The SocialDataX API key could be exposed if included in generated content.

Mitigation: Keep the key in the user's environment and out of prompts, output, and generated files.

Risk: The @latest package reference may change after review.

Mitigation: Prefer a reviewed fixed package version for repeatable use.

## Reference(s):

- [SocialDataX skill and API information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-content-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with structured search-result summaries and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the query and retrieved pages; preserve returned note_url and note_id values exactly.]

## Skill Version(s):

0.1.12 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
