## Description:

分析当前小红书热榜及相关热门笔记样本，并整理可执行的内容选题建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容策划者和小红书创作者可用它查看当前热榜，并结合热门笔记样本整理选题方向、标题钩子和内容角度。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests may consume account credits, and returned note links can contain token parameters.

Mitigation: Protect the SOCIALDATAX_API_KEY and share tokenized note links deliberately.

Risk: The security review covers the skill instructions, not changes to the npm package or hosted service.

Mitigation: Review and pin the package version before use.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis with trend signals, topic ideas, note samples, title hooks, content angles, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are based on the current hot list and returned public note results; full-platform coverage and engagement outcomes are not guaranteed.]

## Skill Version(s):

0.1.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
