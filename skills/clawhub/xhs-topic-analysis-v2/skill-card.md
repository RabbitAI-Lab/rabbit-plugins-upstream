## Description:

帮助内容运营、品牌调研人员和创作者检索小红书内容样本，分析选题方向与内容角度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、品牌调研人员和创作者用它搜索小红书笔记样本，梳理热门选题、内容角度及可继续研究的问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned npm package at runtime.

Mitigation: Review before installing and use a pinned, vetted version of the SocialDataX CLI.

Risk: Returned Xiaohongshu links may include xsec_token and be sensitive or trackable when shared or stored.

Mitigation: Avoid sharing or storing full tokenized links unless those exact links are needed and the recipient understands the risk.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-topic-analysis-v2)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary of search samples and topic analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include note titles, authors, original links or IDs, analysis angles, and follow-up questions; paginated searches may return partial results.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
