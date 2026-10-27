## Description:

用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can search Xiaohongshu/XHS/RedNote posts for topic discovery, content planning, competitor research, market observation, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX and API calls may consume paid credits.

Mitigation: Avoid confidential topics unless sharing them is intended, and check expected usage before searching.

Risk: The skill depends on an external package and an API credential.

Mitigation: Use a reviewed, pinned package version and provide only the required SOCIALDATAX_API_KEY.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown summaries and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only search; summarize fetched results and distinguish visible evidence from interpretation.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
