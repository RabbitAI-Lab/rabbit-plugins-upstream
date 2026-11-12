## Description:

当用户提供红果剧名、剧集链接或 series_id，需要短剧口碑复盘、剧情争议分析、角色反馈整理或多部剧观众评价对比时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can review audience feedback for 1–3 specified Red Fruit short dramas using limited comment samples, with recurring themes, comment evidence, sample scope, and follow-up checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an unpinned package through npx, which creates a supply-chain risk; the security scan also had partial coverage because three local references could not be resolved.

Mitigation: Review the full package and its unresolved references, pin a reviewed package version before installation, and limit credentials and access available to the runtime.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/hongguo-drama-review)
- [SocialDataX homepage and API key access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with sample scope, audience-feedback themes, comment evidence, and review suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers 1–3 specified series; defaults to at most 2 pages and 20 primary comments per series, with at most one page of replies for one key dispute; provides up to 3 follow-up suggestions.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
