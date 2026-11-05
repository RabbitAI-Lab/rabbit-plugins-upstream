## Description:

用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, and content teams use this skill to search Xiaohongshu/XHS/RedNote posts by keyword for topic discovery, competitor research, content planning, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries may include confidential information.

Mitigation: Use non-confidential search terms suited to the intended Xiaohongshu research.

Risk: The SocialDataX API key could be exposed through local files or version control.

Mitigation: Store the key in a local secret store and keep it out of version control.

Risk: The external CLI package was not verified, and a moving latest release can change after review.

Mitigation: Use a reviewed, pinned CLI release with limited permissions.

Risk: Search requests may consume paid credits.

Mitigation: Keep searches within the requested research scope and monitor account credit usage.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are summarized as visible evidence and interpretation; result coverage is limited to fetched pages.]

## Skill Version(s):

0.1.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
