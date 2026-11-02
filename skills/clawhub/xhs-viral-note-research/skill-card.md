## Description:

当用户给出小红书关键词、赛道、人群或产品方向，想看热门高互动笔记样本，并拆解标题结构、内容角度、互动信号、创作灵感和选题参考时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员、营销人员和创作者可围绕关键词或选题方向检索小红书公开笔记样本，并据此整理标题钩子、内容角度、互动信号和后续选题参考。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and may reveal confidential or personal information.

Mitigation: Use topic keywords that do not contain confidential or personal information.

Risk: Search requests may consume paid API credits.

Mitigation: Set a suitable page and item limit and monitor expected credit use before searching.

Risk: The skill uses an external npm package and an API key.

Mitigation: Review the dependency before execution and protect SOCIALDATAX_API_KEY.

## Reference(s):

- [SocialDataX AI and API key access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown research report with a sample table and structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample-based analysis is limited to the requested search pages and item cap; it does not promise complete platform coverage.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
