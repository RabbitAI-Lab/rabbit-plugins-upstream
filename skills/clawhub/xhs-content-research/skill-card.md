## Description:

面向内容运营、品牌调研和创作者的小红书内容研究辅助技能，适用于选题分析、关键词观察、趋势判断、竞品内容对比和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、品牌研究者和创作者可按关键词检索小红书内容，整理选题趋势、竞品对比和可追溯样本。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to SocialDataX, and requests can consume paid credits.

Mitigation: Avoid confidential queries and set page or item limits.

Risk: Returned note URLs can contain query parameters needed to access a result.

Mitigation: Preserve complete URLs when needed to revisit a result, and share them only as appropriate.

Risk: The CLI examples use the latest package version, which can change over time.

Mitigation: Consider pinning a reviewed CLI version.

## Reference(s):

- [SocialDataX 服务与 API Key 管理](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX 官方充值页面](https://socialdatax.com/dashboard/billing)
- [ClawHub 技能发布页](https://clawhub.ai/devinchen2014/skills/xhs-content-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries with result titles, author or account names, links or content IDs, and follow-up angles.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scope follows the supplied query and paging or time limits; returned note URLs retain their original query parameters.]

## Skill Version(s):

0.1.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
