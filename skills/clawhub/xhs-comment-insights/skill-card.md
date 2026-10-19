## Description:

分析用户提供的小红书笔记评论与回复，提炼反馈主题、痛点、购买顾虑、未满足需求和行动建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、产品调研人员、品牌团队和创作者可分析指定小红书笔记的评论及回复，整理用户需求、常见问题和可执行建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime npm package can change between uses and receives the user's SocialDataX API key.

Mitigation: Use a reviewed, pinned package version or preinstalled CLI; enable access only when you trust the package.

Risk: Comments from a single note or partial pages may not reflect broader audience views.

Mitigation: Report the note and pagination coverage, and keep observed comments distinct from inferred themes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings distinguish quoted comments from interpretation and state the sample coverage.]

## Skill Version(s):

0.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
