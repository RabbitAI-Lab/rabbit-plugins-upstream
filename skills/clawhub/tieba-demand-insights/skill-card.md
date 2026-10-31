## Description:

当用户需要做百度贴吧用户需求研究、产品痛点归纳、购买顾虑整理或常见问题分析时使用。输入产品关键词、吧名或帖子链接，基于帖子与楼层讨论输出带原话依据的需求报告。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向产品经理、市场研究人员和内容团队，用于从百度贴吧帖子与楼层讨论中整理用户需求、产品痛点、购买顾虑和常见问题，并形成带来源依据的研究报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, forum names, and post identifiers or URLs are sent to SocialDataX and may reveal research interests.

Mitigation: Avoid confidential or sensitive query inputs.

Risk: SocialDataX requests may incur usage charges, and the CLI dependency is downloaded at runtime.

Mitigation: Start with a small sample, consider usage charges, and prefer a reviewed fixed CLI version over @latest.

## Reference(s):

- [SocialDataX AI and API Key Portal](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown research report with short quotations, post and comment references, evidence strength, and suggested follow-up actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports sample counts and scope, distinguishes observations from interpretations, and notes missing evidence; sample mentions are not population estimates.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
