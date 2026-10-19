## Description:

分析百度贴吧帖子和评论，生成附有原话及来源的用户需求、产品痛点、购买顾虑和常见问题报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, product teams and marketers use this skill to examine Baidu Tieba discussions and summarize user needs, pain points, purchase concerns and FAQs with traceable post and comment evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the latest unpinned npm package exposes users to changes in a third-party dependency.

Mitigation: Review and pin a trusted package version, then run it in a constrained environment.

Risk: The skill uses a SocialDataX API key for read-only research requests.

Mitigation: Use a revocable key and keep unrelated secrets out of the runtime environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/tieba-demand-insights)
- [SocialDataX API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown report with cited post and comment excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample scope, evidence strength and gaps; may retain partial results if a request is interrupted.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
